
import streamlit as st
# from views import mim_dashboard,incident_details, incident_summary, similar_historical_incidents
from views import similar_historical_incidents
from config.styles import CSS_STYLES
from utils.session_state import initialize_session_state
from config.settings import Settings
from datetime import datetime
from services.incident_manager import IncidentManager
from services.detail_extractor import IncidentDetailExtractor
from ui.counter import create_timer_app, create_status_cards
import pandas as pd
import streamlit.components.v1 as components
from services.groq_extractor import GroqDetailExtractor
import logging
from ui.exec_timer import create_exec_timer, initialize_exec_timer, start_exec_timer
 
from streamlit_navigation_bar import st_navbar
from datetime import datetime, timedelta
 
from services.email_processor import EmailProcessor
 
# #from st_pages import Page, show_pages, add_page_title
# from st_pages import add_page_title, get_nav_from_toml
 
 
 
 
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
 

# def initialize_session_state():
#     # Add to existing initialization
#     if 'last_mim_refresh' not in st.session_state:
#         st.session_state.last_mim_refresh = datetime.now()

# def check_auto_refresh():
#     if not hasattr(st.session_state, 'last_mim_refresh'):
#         st.session_state.last_mim_refresh = datetime.now()
#         return False
    
#     current_time = datetime.now()
#     time_difference = current_time - st.session_state.last_mim_refresh
    
#     # Check if an hour has passed
#     if time_difference >= timedelta(hours=1):
#         st.session_state.last_mim_refresh = current_time
#         return True
#     return False

def get_priority_indicator(transcript):
    """
    Determine the priority level based on the first priority indicator found in the transcript.
    Returns tuple of (priority_text, color)
    """
    if not transcript:
        return None, None
        
    transcript_lower = ' ' + transcript.lower() + ' '
    
    # Dictionary of priority patterns and their corresponding (priority_text, color)
    priority_patterns = {
        # P1 patterns
        " major incident ": ("P1", "#FF0000"),
        " mi ": ("P1", "#FF0000"),
        "(mi)": ("P1", "#FF0000"),
        "-mi-": ("P1", "#FF0000"),
        "mi-": ("P1", "#FF0000"),
        "-mi ": ("P1", "#FF0000"),
        # P2 patterns
        " possible major incident ": ("P2", "#FFA500"),
        " pmi ": ("P2", "#FFA500"),
        "(pmi)": ("P2", "#FFA500"),
        "-pmi-": ("P2", "#FFA500"),
        "pmi-": ("P2", "#FFA500"),
        "-pmi ": ("P2", "#FFA500"),
        " p2 ": ("P2", "#FFA500"),
        "(p2)": ("P2", "#FFA500"),
        "-p2-": ("P2", "#FFA500"),
        "p2-": ("P2", "#FFA500"),
        "-p2 ": ("P2", "#FFA500")
    }
    
    # Find all occurrences of priority patterns and their positions
    found_priorities = []
    for pattern, priority_info in priority_patterns.items():
        pos = transcript_lower.find(pattern)
        if pos != -1:
            found_priorities.append((pos, priority_info))
    
    # If any priorities were found, return the one that appears first in the text
    if found_priorities:
        found_priorities.sort(key=lambda x: x[0])  # Sort by position
        return found_priorities[0][1]  # Return the priority_info of the first occurrence
        
    return None, None


def show_executive_dashboard():
    # Enhanced CSS with more colors
    st.markdown("""
        <style>
        .main {
            padding: 1rem !important;
        }
        .compact-box {
            background-color: #f8f9fa;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 8px;
            margin: 4px 0;
            font-size: 0.9em;
        }
        .priority-indicator {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 15px;
            font-weight: bold;
            margin-left: 15px;
            font-size: 1.2em;
        }
        .status-header {
            background-color: #4169E1;
            color: white;
            padding: 8px;
            border-radius: 5px;
            margin: 4px 0;
        }
        .impact-box {
            background-color: #9370DB;
            color: white;
            padding: 8px;
            border-radius: 5px;
            margin: 4px 0;
        }
        .business-impact-box {
            background-color: #6A5ACD;
            color: white;
            padding: 8px;
            border-radius: 5px;
            margin: 4px 0;
        }
        .communication-box {
            background-color: #7B68EE;
            color: white;
            padding: 8px;
            border-radius: 5px;
            margin: 4px 0;
        }
        .bridge-box {
            background: linear-gradient(135deg, #40E0D0, #4169E1);
            color: white;
            padding: 8px;
            border-radius: 5px;
            margin: 4px 0;
        }
        .title-box {
            background-color: #40E0D0;
            color: white;
            padding: 8px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .incident-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
            padding: 10px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .duration-box {
            border: 2px solid #ff4444;
            border-radius: 50%;
            padding: 10px 15px;
            color: #ff4444;
            font-weight: bold;
            font-size: 1.2em;
        }
        .blue-header {
            background-color: #0066cc;
            color: white;
            padding: 10px;
            border-radius: 5px 5px 0 0;
            margin: 4px 0 0 0;
        }
        .white-content {
            background-color: white;
            border: 1px solid #ddd;
            padding: 10px;
            border-radius: 0 0 5px 5px;
            margin: 0 0 10px 0;
        }
        .purple-box {
            background-color: #8a2be2;
            color: white;
            padding: 8px;
            margin: 4px 0;
            border-radius: 5px;
        }
        /* Additional dashboard styling */
        .dashboard-metrics {
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 15px;
        }
        .incident-status {
            font-weight: bold;
            padding: 5px 10px;
            border-radius: 3px;
            display: inline-block;
        }
        .status-active {
            background-color: #dc3545;
            color: white;
        }
        .metric-card {
            background: white;
            padding: 15px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }
        .metric-title {
            color: #666;
            font-size: 0.9em;
            margin-bottom: 5px;
        }
        .metric-value {
            font-size: 1.2em;
            font-weight: bold;
            color: #333;
        }
        .upload-section {
            padding: 20px;
            border-radius: 5px;
            background-color: #f8f9fa;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

     # Check for emails and process them periodically
    if st.button("Check for Incident Emails"):
        start_exec_timer()
        new_incidents = st.session_state.email_processor.process_emails()
        if new_incidents:
            for incident in new_incidents:
                st.success(f"New Incident Detected: {incident.get('incident_id', 'Unknown')}")
                st.session_state.detailed_issue_info = incident
                
 
   
    with st.sidebar:
        st.markdown("### 📂 Document Upload")
        uploaded_file = st.file_uploader("Upload Incident Document", type=['docx'], key="main_uploader")
       
       
        if uploaded_file:
            try:
                # Start timer when file is uploaded
                #start_exec_timer()
 
             
                   
                    # st.session_state.current_phase = 1 #new
                    # st.session_state.current_phase_start = datetime.now() #new
 
 
                incident_manager = IncidentManager()
                document_text = incident_manager.read_docx(uploaded_file)
                st.session_state.transcript = document_text
               
               
                if 'settings' in st.session_state:
                    # Original OpenAI extraction
                    detailed_extractor = IncidentDetailExtractor(st.session_state.settings.OPENAI_API_KEY)
                    incident_data = detailed_extractor.extract_detailed_issue_info(document_text)
                   
                    if incident_data:
                        # Additional Groq extraction
                        try:
                            groq_extractor = GroqDetailExtractor(st.session_state.settings.GROQ_API_KEY)
                            groq_details = groq_extractor.extract_description_and_actions(document_text)
                           
                            if groq_details:
                                # Update description and workaround
                                if 'issue_description' not in incident_data:
                                    incident_data['issue_description'] = {}
                               
                                incident_data['issue_description']['description'] = groq_details.get('description',
                                    incident_data.get('issue_description', {}).get('description', ''))
                                incident_data['issue_description']['workaround'] = groq_details.get('workaround',
                                    incident_data.get('issue_description', {}).get('workaround', ''))
                               
                                # Update next actions if available from Groq
                                if groq_details.get('next_actions'):
                                    incident_data['next_actions'] = groq_details['next_actions']
                           
                        except Exception as groq_error:
                            logging.error(f"Groq extraction failed: {str(groq_error)}")
                            # Continue with original OpenAI data if Groq fails
                           
                        st.session_state.detailed_issue_info = incident_data
                        st.sidebar.success("✅ Document processed successfully!")
                    else:
                        st.sidebar.error("Failed to extract incident details")
            except Exception as e:
                st.sidebar.error(f"Error: {str(e)}")
 
    # Title
    # priority_text, priority_color = None, None
    # if hasattr(st.session_state, 'transcript'):
    #     priority_text, priority_color = get_priority_indicator(st.session_state.transcript)
    
    # st.markdown('<div class="title-box"><h1>🎯 EXECUTIVE DASHBOARD - MAJOR INCIDENT MANAGEMENT</h1></div>', unsafe_allow_html=True)

    # if priority_text and priority_color:
    #     title_html += f'<span class="priority-indicator" style="background-color: {priority_color}; color: white;">{priority_text}</span>'
    
    # title_html += '</h1></div>'

    
    # st.markdown(title_html, unsafe_allow_html=True)
    # col1, col2 = st.columns([2, 2])
    title_html = '<div class="title-box"><h1>🎯 EXECUTIVE DASHBOARD - MAJOR INCIDENT MANAGEMENT'
    
    # Check for priority indicator
    priority_text, priority_color = None, None
    if hasattr(st.session_state, 'transcript'):
        priority_text, priority_color = get_priority_indicator(st.session_state.transcript)
    
    if priority_text and priority_color:
        title_html += f'<span class="priority-indicator" style="background-color: {priority_color}; color: white;">{priority_text}</span>'
    
    title_html += '</h1></div>'
    
    st.markdown(title_html, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 8])

    
    # should_auto_refresh = check_auto_refresh()
    # if should_auto_refresh and 'has_mim_updates' in st.session_state and st.session_state.has_mim_updates:
    #     st.session_state.detailed_issue_info = st.session_state.mim_edited_data.copy()
    #     st.session_state.has_mim_updates = False
    #     st.success("MIM Updates automatically loaded!")
    
    # # Existing manual refresh functionality
    # if 'has_mim_updates' in st.session_state and st.session_state.has_mim_updates:
    #     with col1:
    #         if st.button("Load MIM Updates", type="primary", key="manual_mim_refresh"):
    #             st.session_state.detailed_issue_info = st.session_state.mim_edited_data.copy()
    #             st.session_state.has_mim_updates = False
    #             st.session_state.last_mim_refresh = datetime.now()
    #     with col2:
    #         st.success("Successfully loaded updates from MIM Dashboard!")
            
    # else:
    #     st.button("Load MIM Updates", disabled=True, key="disabled_mim_refresh")
    
    # # Add refresh timer display
    # if hasattr(st.session_state, 'last_mim_refresh'):
    #     next_refresh = st.session_state.last_mim_refresh + timedelta(hours=1)
    #     time_until_refresh = next_refresh - datetime.now()
    #     minutes_until_refresh = max(0, int(time_until_refresh.total_seconds() / 60))
        
    #     st.markdown(f"""
    #         <div style='text-align: right; color: #666; font-size: 0.8em;'>
    #             Next auto-refresh in: {minutes_until_refresh} minutes
    #         </div>
    #     """, unsafe_allow_html=True)

    
    if 'has_mim_updates' in st.session_state and st.session_state.has_mim_updates:
            with col1:
                if st.button("Load MIM Updates", type="primary"):
                    # Update executive dashboard with MIM changes
                    st.session_state.detailed_issue_info = st.session_state.mim_edited_data.copy()
                    st.session_state.has_mim_updates = False
            with col2:
                    st.success("New updates from MIM Dashboard!")
                
    else:
            st.button("Load MIM Updates", disabled=True)

    # if 'detailed_issue_info' in st.session_state and st.session_state.detailed_issue_info:

 
    # Check for incident data in session state with proper null checks
    if 'detailed_issue_info' in st.session_state and st.session_state.detailed_issue_info is not None:
        incident_data = st.session_state.detailed_issue_info
       
        # Clean location handling with proper null checks
        all_locations = set()  # Using set to automatically handle duplicates
       
        # Collect locations from all possible fields
        issue_location = incident_data.get('issue_location', '')
        affected_location = incident_data.get('affected_location', '')
       
        if issue_location:
            all_locations.update(loc.strip() for loc in issue_location.replace(' and ', ', ').split(','))
        if affected_location:
            all_locations.update(loc.strip() for loc in affected_location.replace(' and ', ', ').split(','))
           
        # Clean and standardize locations with proper filtering
        cleaned_locations = sorted(set(
            loc.strip().replace('Bangalore', 'Bengaluru').title()
            for loc in all_locations
            if loc and loc.strip() and loc.strip() != 'N/A'
        ))
       
        # Format locations for display
        location_str = ' and '.join(cleaned_locations) if cleaned_locations else ''
 
       
      # Get incident details with proper null checks
        incident_id = incident_data.get('incident_id', '')
        issue_description = incident_data.get('short_description', '')
        priority = incident_data.get('priority_level', '')
       
        # Create header text with clean format
        header_text = f"{incident_id} - {issue_description}"
        if location_str:
            header_text += f" at {location_str}"
       
       
     
        incident_id = incident_data.get('incident_id', '')
        issue_description = incident_data.get('short_description', '')
        priority = incident_data.get('priority_level', '')
       
        # Create header text with clean format
        header_text = f"{incident_id} - {issue_description}"
        if location_str:
            header_text += f" at {location_str}"
 
 
 
 
        header_text = f"{incident_id} - {issue_description}"
        if location_str:
            header_text += f" at {location_str}"
           
        timer_html = create_exec_timer()
 
       
 
    
 
       
        # Main content in two columns
        main_col1, main_col2 = st.columns([7, 3])
       
        with main_col1:
            # Current Status
            st.markdown('<div class="blue-header">🔄 Current Status</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="white-content">{incident_data.get("description", "N/A")}</div>', unsafe_allow_html=True)
           
           
 
            st.markdown('<div class="blue-header">⏭️ Next Actions:</div>', unsafe_allow_html=True)
            next_actions = incident_data.get('next_actions', [])
            if next_actions:
                formatted_actions = "<div class='white-content'>"
                for action in next_actions:
                    # Clean and properly capitalize the action
                    clean_action = (action.replace('*', '')
                                       .replace('•', '')
                                       .strip()
                                       .replace('dba', 'DBA')
                                       .replace('dr', 'DR')
                                       .replace('sap', 'SAP')
                                       .replace('erp', 'ERP')
                                       .replace('sre', 'SRE')
                                       .replace('unix', 'UNIX'))
                   
                    # Add bullet point and line break
                    formatted_actions += f"• {clean_action}<br><br>"
               
                formatted_actions += "</div>"
                st.markdown(formatted_actions, unsafe_allow_html=True)
            else:
                st.markdown("<div class='white-content'>No immediate actions required</div>", unsafe_allow_html=True)
           
           
            st.markdown('<div class="blue-header">⚠️ Issue Description</div>', unsafe_allow_html=True)
 
           
           
 
            # Get and format description with bullet points from Groq extraction
            system_info = incident_data.get('issue_description', {}).get('description', 'No description available')
            root_cause = "Technical details being analyzed"  # We'll derive this from the Groq description
            timing = "Timing details being extracted"  # We'll derive this from the Groq description
            impact = "Impact details being assessed"  # We'll derive this from the Groq description
 
            formatted_description = f"""
                <div class="white-content">
                    <strong>{header_text}</strong><br><br>
                    {system_info}<br><br>
                    <strong>Work Around:</strong> {incident_data.get('issue_description', {}).get('workaround', 'No workaround currently available').capitalize()}
                </div>
            """
 
            st.markdown(formatted_description, unsafe_allow_html=True)
                       
            # Business Impact
            st.markdown('<div class="blue-header">💼 Business Impact</div>', unsafe_allow_html=True)
           
            # Applications
            st.markdown('<div class="purple-box">Application (s)</div>', unsafe_allow_html=True)
            services = incident_data.get('impacted_services', [])
            st.markdown(f"""
            <div class="white-content">
                <strong>Top Services Impacted: </strong>{', '.join(services) if services else 'N/A'}
            </div>
            """, unsafe_allow_html=True)
           
            # Geography
            st.markdown('<div class="purple-box">Geography (S)</div>', unsafe_allow_html=True)
            st.markdown(f"""
            <div class="white-content">
                <strong>Sites Impacted: </strong>{location_str if location_str else 'N/A'}
            </div>
            """, unsafe_allow_html=True)
           
            # Process/Activities
            st.markdown('<div class="purple-box">Process / Activities Impacted</div>', unsafe_allow_html=True)
            st.markdown(f"""
            <div class="white-content">
                <strong>Activities Impacted: </strong>{incident_data.get('activities_impacted', 'N/A')}
            </div>
            """, unsafe_allow_html=True)
           
            # Key Stakeholders
            st.markdown('<div class="purple-box">Key Stakeholder Engaged</div>', unsafe_allow_html=True)
            participants = incident_data.get('participants', [])
            st.markdown(f"""
            <div class="white-content">
                {', '.join(participants) if participants else 'N/A'}
            </div>
            """, unsafe_allow_html=True)
       
        with main_col2:
           
            st.markdown('<div class="blue-header">📢 MIM Communication Status</div>', unsafe_allow_html=True)
           
            communications_df = pd.DataFrame([
                ['Open Comms (Hyper Link)', '1', '7:00 AM', 'Published'],
                ['Update 1 (Hyper Link)', '3', 'TBD', 'Not Published'],
                ['Update 2 (Hyper Link)', '2', '7:30 AM', 'Published'],
                ['Update 3 (Hyper Link)', '4', 'TBD', 'Not Published']
            ], columns=['Communications', 'Order', 'Time', 'Status'])
           
            st.table(communications_df.assign(hack='').set_index('hack'))
           
            # Bridge Details
            bridge_info = incident_data.get('bridge_details')
            if bridge_info:
                st.markdown('<div class="blue-header">🌐 Bridge Details</div>', unsafe_allow_html=True)
                st.markdown(f"""
                <div class="white-content">
                    <strong>Business Bridge:</strong><br>
                    Platform: {bridge_info.get('platform', 'N/A')}<br>
                    Meeting ID: {bridge_info.get('meeting_id', 'N/A')}<br>
                    Passcode: {bridge_info.get('passcode', 'N/A')}
                </div>
                """, unsafe_allow_html=True)
 
            st.markdown('<div class="blue-header">🔗 Key Process Links</div>', unsafe_allow_html=True)
           
            process_links = [
                "Announcement Portal Link",
                "GCC Calendar Link",
                "Executive Communication Process",
                "MIM Process Document",
                "Easy Learn Session Training",
                "Change Management Process",
                "Problem Management Process",
                "P1s Do/Don't's"
            ]
           
            links_html = "<div class='white-content'>"
            for link in process_links:
                links_html += f"""
                <div style="padding: 8px 0;">
                    <a href="#" style="color: #0066cc; text-decoration: none; display: block;">
                        {link}
                    </a>
                </div>"""
            links_html += "</div>"
           
            st.markdown(links_html, unsafe_allow_html=True)
           
 
    else:
        st.info("Please upload an incident document using the panel on the left")
 
def editable(): 
    if 'detailed_issue_info' in st.session_state:
        incident_data = st.session_state.detailed_issue_info
        
        # Initialize required session state variables
        if 'recipients' not in st.session_state:
            st.session_state.recipients = []
        if 'show_process_button' not in st.session_state:
            st.session_state.show_process_button = True
        
        # Create timer app
        with st.container():
            create_timer_app()

    # Synchronize data with the Executive Dashboard
    if 'detailed_issue_info' in st.session_state:
        if not st.session_state.get('mim_edited_data'):
            # Copy data from Executive Dashboard if MIM Dashboard is empty
            st.session_state.mim_edited_data = st.session_state.detailed_issue_info
    else:
        # If no Executive Dashboard data, display a warning and exit
        st.info("Please upload an incident document in the Executive Dashboard first")
        return

    # Display the MIM Dashboard title
    st.markdown('<div class="title-box"><h1>🎯 MIM DASHBOARD - EDIT MODE</h1></div>', unsafe_allow_html=True)
    
    #st.session_state.mim_edited_data = st.session_state.detailed_issue_info
    # Get incident details from MIM Dashboard state
    incident_data = st.session_state.mim_edited_data
    incident_id = incident_data.get('incident_id', '')
    issue_description = incident_data.get('short_description', '')

    # Process and clean locations
    all_locations = set()
    issue_location = incident_data.get('issue_location', '')
    affected_location = incident_data.get('affected_location', '')
    
    if issue_location:
        all_locations.update(loc.strip() for loc in issue_location.replace(' and ', ', ').split(','))
    if affected_location:
        all_locations.update(loc.strip() for loc in affected_location.replace(' and ', ', ').split(','))
    
    cleaned_locations = sorted(set(
        loc.strip().replace('Bangalore', 'Bengaluru').title()
        for loc in all_locations
        if loc and loc.strip() and loc.strip() != 'N/A'
    ))
    
    location_str = ' and '.join(cleaned_locations) if cleaned_locations else ''
    
    # Create header text
    header_text = f"{incident_id} - {issue_description}"
    if location_str:
        header_text += f" at {location_str}"

    # Main content in two columns
    main_col1, main_col2 = st.columns([7, 3])
    
    with main_col1:
        # Current Status
        st.markdown('<div class="blue-header">🔄 Current Status</div>', unsafe_allow_html=True)
        current_status = st.text_area(
            "Edit Current Status",
            value=incident_data.get("description", ""),
            key="edit_current_status",
            height=100
        )
        st.session_state.mim_edited_data["description"] = current_status

        # Next Actions
        st.markdown('<div class="blue-header">⏭️ Next Actions:</div>', unsafe_allow_html=True)
        next_actions = incident_data.get('next_actions', [])
        next_actions_text = "\n".join(filter(None, next_actions)) if next_actions else ""
        updated_actions = st.text_area(
            "Edit Next Actions (one per line)",
            value=next_actions_text,
            key="edit_next_actions",
            height=150
        )
        st.session_state.mim_edited_data["next_actions"] = [action for action in updated_actions.split("\n") if action.strip()]

        # Issue Description
        st.markdown('<div class="blue-header">⚠️ Issue Description</div>', unsafe_allow_html=True)
        
        description = st.text_area(
            "Edit Description",
            value=incident_data.get('issue_description', {}).get('description', ''),
            key="edit_description",
            height=150
        )
        workaround = st.text_area(
            "Edit Workaround",
            value=incident_data.get('issue_description', {}).get('workaround', ''),
            key="edit_workaround",
            height=100
        )
        st.session_state.mim_edited_data['issue_description'] = {
            'description': description,
            'workaround': workaround
        }

        # Business Impact
        st.markdown('<div class="blue-header">💼 Business Impact</div>', unsafe_allow_html=True)
        # Applications
        services = incident_data.get('impacted_services', [])
        services_text = ", ".join(filter(None, services)) if services else ""
        updated_services = st.text_input(
            "Edit Impacted Services (comma-separated)",
            value=services_text,
            key="edit_services"
        )
        st.session_state.mim_edited_data["impacted_services"] = [s.strip() for s in updated_services.split(",") if s.strip()]
        # Geography
        st.markdown('<div class="purple-box">Geography (S)</div>', unsafe_allow_html=True)
        locations = st.session_state.mim_edited_data.get('affected_locations', [])
        locations_text = ", ".join(locations) if locations else ""
        updated_locations = st.text_input(
            "Edit Sites Impacted (comma-separated)",
            value=locations_text,
            key="edit_locations"
        )
        st.session_state.mim_edited_data["affected_locations"] = [
            loc.strip() for loc in updated_locations.split(",") if loc.strip()
        ]

        # Process/Activities
        st.markdown('<div class="purple-box">Process / Activities Impacted</div>', unsafe_allow_html=True)
        activities = st.text_area(
            "Edit Activities Impacted",
            value=st.session_state.mim_edited_data.get('activities_impacted', ''),
            key="edit_activities",
            height=100
        )
        st.session_state.mim_edited_data["activities_impacted"] = activities

        # Key Stakeholders
        st.markdown('<div class="purple-box">Key Stakeholder Engaged</div>', unsafe_allow_html=True)
        participants = st.session_state.mim_edited_data.get('participants', [])
        participants_text = ", ".join(participants) if participants else ""
        updated_participants = st.text_input(
            "Edit Stakeholders (comma-separated)",
            value=participants_text,
            key="edit_stakeholders"
        )
        st.session_state.mim_edited_data["participants"] = [
            p.strip() for p in updated_participants.split(",") if p.strip()
        ]

    with main_col2:
        st.markdown('<div class="blue-header">📢 MIM Communication Status</div>', unsafe_allow_html=True)
        communications_df = pd.DataFrame([
            ['Open Comms (Hyper Link)', '1', '7:00 AM', 'Published'],
            ['Update 1 (Hyper Link)', '3', 'TBD', 'Not Published'],
            ['Update 2 (Hyper Link)', '2', '7:30 AM', 'Published'],
            ['Update 3 (Hyper Link)', '4', 'TBD', 'Not Published']
        ], columns=['Communications', 'Order', 'Time', 'Status'])
        st.table(communications_df.assign(hack='').set_index('hack'))


        st.markdown('<div class="blue-header">🌐 Bridge Details</div>', unsafe_allow_html=True)
        if 'bridge_details' not in st.session_state.mim_edited_data:
            st.session_state.mim_edited_data['bridge_details'] = {}
            
        platform = st.text_input(
            "Platform",
            value=st.session_state.mim_edited_data.get('bridge_details', {}).get('platform', ''),
            key="edit_platform"
        )
        meeting_id = st.text_input(
            "Meeting ID",
            value=st.session_state.mim_edited_data.get('bridge_details', {}).get('meeting_id', ''),
            key="edit_meeting_id"
        )
        passcode = st.text_input(
            "Passcode",
            value=st.session_state.mim_edited_data.get('bridge_details', {}).get('passcode', ''),
            key="edit_passcode"
        )
        
        st.session_state.mim_edited_data['bridge_details'] = {
            'platform': platform,
            'meeting_id': meeting_id,
            'passcode': passcode
        }

        # Key Process Links
        st.markdown('<div class="blue-header">🔗 Key Process Links</div>', unsafe_allow_html=True)
        
        process_links = [
            "Announcement Portal Link",
            "GCC Calendar Link",
            "Executive Communication Process",
            "MIM Process Document",
            "Easy Learn Session Training",
            "Change Management Process",
            "Problem Management Process",
            "P1s Do/Don't's"
        ]
        
        links_html = "<div class='white-content'>"
        for link in process_links:
            links_html += f"""
            <div style="padding: 8px 0;">
                <a href="#" style="color: #0066cc; text-decoration: none; display: block;">
                    {link}
                </a>
            </div>"""
        links_html += "</div>"
        
        st.markdown(links_html, unsafe_allow_html=True)


    # Save button to persist changes in the session state
    if st.button("Save MIM Changes", key="save_mim_changes"):
        st.session_state.has_mim_updates = True
        st.success("Changes saved in MIM Dashboard. Use 'Load MIM Updates' in Executive Dashboard to apply changes.")

    similar_historical_incidents.show()


#     main()
def main():

    st.set_page_config(page_title="Executive Dashboard", page_icon="🎯", layout="wide", initial_sidebar_state="expanded")
    
    # Initialize session state
    initialize_session_state()
    initialize_exec_timer()
    
    if 'settings' not in st.session_state:
        st.session_state.settings = Settings()
    
    # Initialize MIM-specific state variables
    if 'has_mim_updates' not in st.session_state:
        st.session_state.has_mim_updates = False
    
    if 'mim_edited_data' not in st.session_state:
        st.session_state.mim_edited_data = {}
    
    # New: Initialize Email Processor
    if 'email_processor' not in st.session_state:
        st.session_state.email_processor = EmailProcessor(
            username=st.session_state.settings.EMAIL_USERNAME,
            password=st.session_state.settings.EMAIL_PASSWORD
        )
    
     
   
    # Sidebar styling
    st.markdown("""
        <style>
        .css-1d391kg {
            background-color: #40E0D0;
        }
        .sidebar .sidebar-content {
            background-color: #40E0D0;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown(CSS_STYLES, unsafe_allow_html=True)

    # Create navigation tabs
    tab_names = ["Executive Dashboard", "MIM Dashboard"]
    tabs = st.tabs(tab_names)

    # Routing logic
    with tabs[0]:
        show_executive_dashboard()
    with tabs[1]:
        editable()

if __name__ == "__main__":
    main()