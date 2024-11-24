# # app.py
# import streamlit as st
# from views import incident_details, incident_summary, similar_historical_incidents  # Changed from 'pages' to 'views'
# from config.styles import CSS_STYLES
# from utils.session_state import initialize_session_state
# from config.settings import Settings

# def main():
#     st.set_page_config(
#         page_title="Major Incident Management",
#         page_icon="🚨",
#         layout="wide"
#     )
#     st.markdown(CSS_STYLES, unsafe_allow_html=True)

#     # Initialize session state
#     initialize_session_state()
#     if 'settings' not in st.session_state:
#         st.session_state.settings = Settings()

#     # Sidebar navigation
#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio("Go to", ["Incident Details", "Incident Summary", "Similar Historical Incidents"])

#     # Page routing
#     if page == "Incident Details":
#         incident_details.show()
#     elif page == "Incident Summary":
#         incident_summary.show()
#     else:
#         similar_historical_incidents.show()

# if __name__ == "__main__":
#     main()

# import streamlit as st
# from History.Similar_Incidents3 import EnhancedIncidentAnalysisSystem
# from config.settings import Settings

# def show():
#     st.title("🔍 Similar Historical Incidents")

#     if 'detailed_issue_info' in st.session_state:
#         # Concatenate detailed issue info into a single string
#         incident_description = " ".join(
#             f"{key}: {value}" for key, value in st.session_state.detailed_issue_info.items()
#         )

#         # Initialize the analysis system
#         analysis_system = EnhancedIncidentAnalysisSystem(
#             groq_api_key=Settings().GROQ_API_KEY,
#             historical_incidents_file='C:\\Users\\arkapoor.ext\\Downloads\\UnileverPOC-main\\UnileverPOC-main\\History\\Incidents_4X3.xlsx'
#         )

#         # Perform analysis
#         result = analysis_system.analyze_incident(incident_description)

#         # Display root cause analysis
#         st.subheader("Root Cause Analysis")
#         for key, value in result['current_incident']['analysis'].items():
#             st.markdown(f"**{key}:** {value}")

#         # Display similar incidents
#         st.subheader("Similar Incidents")
#         for incident in result['similar_incidents']:
#             st.markdown(f"**Incident ID:** {incident['incident_id']}")
#             st.markdown(f"**Similarity Score:** {incident['similarity_score']}")
#             st.markdown(f"**Description:** {incident['description']}")
#             st.markdown(f"**Actions Taken:** {incident['actions_taken']}")
#             st.markdown(f"**Participants:** {incident['participants']}")
#             st.markdown("---")

#         # Export button
#         if st.button("Export Analysis"):
#             # Convert result to a downloadable format
#             st.download_button(
#                 label="Download Analysis",
#                 data=str(result),
#                 file_name="similar_incidents_analysis.txt",
#                 mime="text/plain"
#             )
#     else:
#         st.warning("Please process an incident document first.")











# import streamlit as st
# from datetime import datetime

# def setup_page():
#     st.set_page_config(
#         page_title="Major Incident Management",
#         page_icon="🚨",
#         layout="wide"
#     )
    
#     # Custom CSS for styling
#     st.markdown("""
#         <style>
#         .incident-box {
#             border: 1px solid #ddd;
#             border-radius: 5px;
#             padding: 15px;
#             margin: 10px 0;
#         }
#         .status-header {
#             background-color: #0066cc;
#             color: white;
#             padding: 10px;
#             border-radius: 5px;
#         }
#         .impact-section {
#             background-color: #f8f9fa;
#             padding: 10px;
#             border-radius: 5px;
#         }
#         .communication-table {
#             width: 100%;
#         }
#         .priority-badge {
#             background-color: #ff4444;
#             color: white;
#             padding: 5px 10px;
#             border-radius: 15px;
#             float: right;
#         }
#         </style>
#     """, unsafe_allow_html=True)

# def display_incident_header():
#     col1, col2 = st.columns([4, 1])
#     with col1:
#         st.title("INT0XXXXX- Network Connectivity Issue at Chennai, India")
#     with col2:
#         st.markdown("""
#             <div style='text-align: right;'>
#                 <p>10:41:05</p>
#                 <p class='priority-badge'>Priority 1</p>
#             </div>
#         """, unsafe_allow_html=True)

# def display_current_status():
#     st.markdown("<div class='status-header'><h3>🔄 Current Status</h3></div>", unsafe_allow_html=True)
#     st.markdown("""
#         * On July 19, 2024, at 04:09 UTC, a CrowdStrike Windows sensor update caused 
#           a logic error, leading to widespread system crashes (BSOD) across 2,000+ 
#           Unilever Windows hosts (version 7.11).
#     """)

# def display_next_actions():
#     st.markdown("<div class='status-header'><h3>📋 Next Actions</h3></div>", unsafe_allow_html=True)
#     st.markdown("""
#         * On July 19, 2024, at 04:09 UTC, a CrowdStrike Windows sensor update caused 
#           a logic error, leading to widespread system crashes (BSOD) across 2,000+ 
#           Unilever Windows hosts (version 7.11).
#     """)

# def display_issue_description():
#     st.markdown("<div class='status-header'><h3>⚙️ Issue Description</h3></div>", unsafe_allow_html=True)
#     st.markdown("""
#         * A post-incident analysis with GPS and HCL revealed a critical gap Mod2 servers 
#           lack proper backup measures, handled by respective Service Owners.
#         * Work Around: Unlike fully backed-up Mod1 servers managed by HCL (Details in Slide 4)
#     """)

# def display_business_impact():
#     st.markdown("<div class='status-header'><h3>👥 Business Impact</h3></div>", unsafe_allow_html=True)
    
#     # Services Impacted
#     st.subheader("Services Impacted")
#     st.markdown("""
#         **Application (4)**
#         * Top Services Impacted: Automation Factory (RPA), SAP Printing Services, 
#           Hyper-V Infrastructure, Citrix, Group Share & other Foundational Services
#     """)
    
#     # Geography
#     st.markdown("""
#         **Geography (5)**
#         * Sites Impacted: Production scheduling, Order
#     """)
    
#     # Process/Activities
#     st.markdown("""
#         **Process/Activities Impacted**
#         * Activities Impacted: Production scheduling, Order Processing, 
#           Product Shipment, Invoicing, Printing & reporting
#     """)
    
#     # Key Stakeholders
#     st.markdown("""
#         **Key Stakeholder engaged**
#         * MIM, SAP basis, Market IT, Application SO etc
#     """)

# def display_communication_status():
#     st.markdown("<div class='status-header'><h3>📢 MIM Communication Status</h3></div>", unsafe_allow_html=True)
    
#     # Create a DataFrame for the communication table
#     communications_data = {
#         'Communications': ['Open Comms (Hyper Link)', 'Update 1 (Hyper Link)', 
#                          'Update 2 (Hyper Link)', 'Update 3 (Hyper Link)'],
#         'Order': ['1', '3', '2', '4'],
#         'Time': ['7:00 AM', 'TBD', '7:30 AM', 'TBD'],
#         'Status': ['Published', 'Not Published', '', '']
#     }
    
#     st.table(communications_data)

# def main():
#     setup_page()
#     display_incident_header()
    
#     col1, col2 = st.columns(2)
#     with col1:
#         display_current_status()
#     with col2:
#         display_next_actions()
        
#     display_issue_description()
    
#     col3, col4 = st.columns(2)
#     with col3:
#         display_business_impact()
#     with col4:
#         display_communication_status()

# if __name__ == "__main__":
#     main()









# # app.py
# import streamlit as st
# from views import incident_details, incident_summary, similar_historical_incidents
# from datetime import datetime
# from config.settings import Settings

# def setup_page():
#     st.set_page_config(
#         page_title="Major Incident Management",
#         page_icon="🚨",
#         layout="wide"
#     )
    
#     # Custom CSS for styling
#     st.markdown("""
#         <style>
#         .status-header {
#             background-color: #0066cc;
#             color: white;
#             padding: 10px;
#             border-radius: 5px;
#         }
#         .priority-badge {
#             background-color: #ff4444;
#             color: white;
#             padding: 5px 10px;
#             border-radius: 15px;
#             float: right;
#         }
#         </style>
#     """, unsafe_allow_html=True)

# def initialize_session_state():
#     # Initialize settings
#     if 'settings' not in st.session_state:
#         st.session_state.settings = Settings()
    
#     # Initialize the basic required fields
#     if 'incident_data' not in st.session_state:
#         st.session_state.incident_data = {}
    
#     # Initialize detailed_issue_info
#     if 'detailed_issue_info' not in st.session_state:
#         st.session_state.detailed_issue_info = {}

#     # Ensure all required fields exist
#     default_fields = {
#         'title': 'Network Connectivity Issue at Chennai, India',
#         'incident_number': 'INT0XXXXX',
#         'location': 'Chennai, India',
#         'time': '10:41:05',
#         'priority_level': '1',
#         'status': 'System crashes across 2,000+ hosts',
#         'actions': 'Investigating CrowdStrike Windows sensor update issue',
#         'description': ['Critical gap in Mod2 servers backup measures'],
#         'impact': {
#             'applications': 'RPA, SAP Services',
#             'geography': 'Chennai production sites',
#             'activities': 'Production scheduling',
#             'stakeholders': 'MIM, SAP team'
#         },
#         'comms': []
#     }

#     # Update any missing fields with defaults
#     for key, value in default_fields.items():
#         if key not in st.session_state.incident_data:
#             st.session_state.incident_data[key] = value

# def safe_get(dict_obj, key, default=''):
#     """Safely get a value from a dictionary."""
#     return dict_obj.get(key, default)

# def incident_dashboard():
#     try:
#         data = st.session_state.incident_data
#         display_incident_header(data)
        
#         col1, col2 = st.columns(2)
#         with col1:
#             display_current_status(data)
#         with col2:
#             display_next_actions(data)
            
#         display_issue_description(data)
        
#         col3, col4 = st.columns(2)
#         with col3:
#             display_business_impact(data)
#         with col4:
#             display_communication_status(data)
#     except Exception as e:
#         st.error(f"Error displaying dashboard: {str(e)}")
#         st.write("Current session state:", st.session_state)

# def display_incident_header(data):
#     col1, col2 = st.columns([4, 1])
#     with col1:
#         title = safe_get(data, 'title', 'Incident Title Not Available')
#         incident_number = safe_get(data, 'incident_number', 'No ID')
#         st.title(f"{incident_number}- {title}")
#     with col2:
#         time = safe_get(data, 'time', 'Time not set')
#         priority = safe_get(data, 'priority_level', '?')
#         st.markdown(f"""
#             <div style='text-align: right;'>
#                 <p>{time}</p>
#                 <p class='priority-badge'>Priority {priority}</p>
#             </div>
#         """, unsafe_allow_html=True)

# def display_current_status(data):
#     st.markdown("<div class='status-header'><h3>🔄 Current Status</h3></div>", unsafe_allow_html=True)
#     status = safe_get(data, 'status', 'No status available')
#     st.markdown(f"* {status}")

# def display_next_actions(data):
#     st.markdown("<div class='status-header'><h3>📋 Next Actions</h3></div>", unsafe_allow_html=True)
#     actions = safe_get(data, 'actions', 'No actions specified')
#     st.markdown(f"* {actions}")

# def display_issue_description(data):
#     st.markdown("<div class='status-header'><h3>⚙️ Issue Description</h3></div>", unsafe_allow_html=True)
#     description = safe_get(data, 'description', ['No description available'])
#     if isinstance(description, list):
#         for issue in description:
#             st.markdown(f"* {issue}")
#     else:
#         st.markdown(f"* {description}")

# def display_business_impact(data):
#     st.markdown("<div class='status-header'><h3>👥 Business Impact</h3></div>", unsafe_allow_html=True)
    
#     impact = safe_get(data, 'impact', {})
    
#     st.subheader("Services Impacted")
#     st.markdown(f"""
#         **Application (4)**
#         * Top Services Impacted: {safe_get(impact, 'applications', 'None specified')}
#     """)
    
#     st.markdown(f"""
#         **Geography (5)**
#         * Sites Impacted: {safe_get(impact, 'geography', 'None specified')}
#     """)
    
#     st.markdown(f"""
#         **Process/Activities Impacted**
#         * Activities Impacted: {safe_get(impact, 'activities', 'None specified')}
#     """)
    
#     st.markdown(f"""
#         **Key Stakeholder engaged**
#         * {safe_get(impact, 'stakeholders', 'None specified')}
#     """)

# def display_communication_status(data):
#     st.markdown("<div class='status-header'><h3>📢 MIM Communication Status</h3></div>", unsafe_allow_html=True)
#     comms = safe_get(data, 'comms', [])
#     if comms:
#         st.table(comms)
#     else:
#         st.write("No communications logged")

# def main():
#     setup_page()
#     initialize_session_state()

#     # Sidebar navigation
#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio(
#         "Go to",
#         ["Incident Details", "Active Incident Dashboard", "Incident Summary", "Similar Historical Incidents"]
#     )

#     # Page routing
#     if page == "Incident Details":
#         incident_details.show()
#     elif page == "Active Incident Dashboard":
#         incident_dashboard()
#     elif page == "Incident Summary":
#         incident_summary.show()
#     else:
#         similar_historical_incidents.show()

# if __name__ == "__main__":
#     main()


# import streamlit as st
# from views import incident_details, incident_summary, similar_historical_incidents
# from config.styles import CSS_STYLES
# from utils.session_state import initialize_session_state
# from config.settings import Settings
# from datetime import datetime
# from services.incident_manager import IncidentManager

# def show_incident_dashboard():
#     st.markdown("""
#         <style>
#         .status-box {
#             padding: 10px;
#             border: 1px solid #ddd;
#             border-radius: 5px;
#             margin: 5px;
#         }
#         .impact-box {
#             background-color: #f0f0f0;
#             padding: 10px;
#             border-radius: 5px;
#             margin: 5px;
#         }
#         .communication-table {
#             width: 100%;
#             border-collapse: collapse;
#         }
#         .communication-table th, .communication-table td {
#             border: 1px solid #ddd;
#             padding: 8px;
#             text-align: left;
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     # File uploader
#     uploaded_file = st.file_uploader("Upload Incident Document", type=['docx'])
    
#     if uploaded_file:
#         try:
#             # Initialize IncidentManager and process document
#             incident_manager = IncidentManager()
#             document_text = incident_manager.read_docx(uploaded_file)
#             incident_data = incident_manager.extract_incident_details(document_text)
            
#             # Store in session state for other views
#             st.session_state.detailed_issue_info = incident_data
            
#             # Header with incident ID and timestamp
#             col1, col2 = st.columns([3, 1])
#             with col1:
#                 st.title(f"{incident_data['incident_id']} - {incident_data['short_description']}")
#             with col2:
#                 st.markdown(f"**Status**: {incident_data['status']}")
#                 st.markdown(f"**Time**: {incident_data['outage_time']}")

#             # Current Status and Next Actions
#             col1, col2 = st.columns(2)
#             with col1:
#                 st.subheader("Current Status")
#                 st.markdown(incident_data['description'])
#             with col2:
#                 st.subheader("Next Actions")
#                 st.markdown(f"Next update expected at: {incident_data['next_update']}")
#                 if 'bridge_details' in incident_data:
#                     st.markdown("### Bridge Details")
#                     st.markdown(f"Platform: {incident_data['bridge_details']['platform']}")
#                     st.markdown(f"Meeting ID: {incident_data['bridge_details']['meeting_id']}")
#                     st.markdown(f"Passcode: {incident_data['bridge_details']['passcode']}")

#             # Issue Description
#             st.subheader("Issue Description")
#             st.markdown(incident_data['description'])

#             # Business Impact and MIM Communication
#             col1, col2 = st.columns(2)
#             with col1:
#                 st.subheader("Business Impact")
                
#                 # Services Impacted
#                 st.markdown("**Services Impacted**")
#                 for service in incident_data['impacted_services']:
#                     st.markdown(f"* {service}")
                
#                 # Business Impact Description
#                 st.markdown("**Impact Details**")
#                 st.markdown(incident_data['business_impact'])
                
#                 # Resolution Teams
#                 st.markdown("**Resolution Teams**")
#                 for team in incident_data['resolution_teams']:
#                     st.markdown(f"* {team}")

#             with col2:
#                 st.subheader("MIM Communication Status")
#                 communication_data = {
#                     "Communications": ["Initial Notification"],
#                     "Time": [incident_data['mim_notified_time']],
#                     "Status": ["Published"],
#                     "Reported By": [incident_data['reported_by']]
#                 }
                
#                 import pandas as pd
#                 df = pd.DataFrame(communication_data)
#                 st.table(df)

#         except Exception as e:
#             st.error(f"Error processing document: {str(e)}")
#     else:
#         st.info("Please upload an incident document to view the dashboard.")

# def main():
#     st.set_page_config(
#         page_title="Major Incident Management",
#         page_icon="🚨",
#         layout="wide"
#     )
#     st.markdown(CSS_STYLES, unsafe_allow_html=True)
    
#     # Initialize session state
#     initialize_session_state()
#     if 'settings' not in st.session_state:
#         st.session_state.settings = Settings()
    
#     # Sidebar navigation with new dashboard option
#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio("Go to", [
#         "Incident Dashboard",
#         "Incident Details", 
#         "Incident Summary", 
#         "Similar Historical Incidents"
#     ])
    
#     # Page routing with new dashboard
#     if page == "Incident Dashboard":
#         show_incident_dashboard()
#     elif page == "Incident Details":
#         incident_details.show()
#     elif page == "Incident Summary":
#         incident_summary.show()
#     else:
#         similar_historical_incidents.show()

# if __name__ == "__main__":
#     main()




#COLOURFUL VIEW , BUT NOT COMPACT

# import streamlit as st
# from views import incident_details, incident_summary, similar_historical_incidents
# from config.styles import CSS_STYLES
# from utils.session_state import initialize_session_state
# from config.settings import Settings
# from datetime import datetime
# from services.incident_manager import IncidentManager

# def show_incident_dashboard():
#     # Custom CSS with colors matching the image
#     st.markdown("""
#         <style>
#         .main {
#             background-color: #ffffff;
#         }
#         .sidebar {
#             background-color: #40E0D0;
#         }
#         .incident-box {
#             background-color: #f8f9fa;
#             border: 1px solid #ddd;
#             border-radius: 5px;
#             padding: 15px;
#             margin: 10px 0;
#         }
#         .status-header {
#             background-color: #4169E1;
#             color: white;
#             padding: 10px;
#             border-radius: 5px;
#             margin: 5px 0;
#         }
#         .impact-box {
#             background-color: #9370DB;
#             color: white;
#             padding: 15px;
#             border-radius: 5px;
#             margin: 10px 0;
#         }
#         .communication-table {
#             width: 100%;
#             border-collapse: collapse;
#         }
#         .communication-table th, .communication-table td {
#             border: 1px solid #ddd;
#             padding: 8px;
#             text-align: left;
#         }
#         .info-card {
#             background-color: #9370DB;
#             color: white;
#             padding: 10px;
#             border-radius: 5px;
#             margin: 5px 0;
#         }
#         .title-box {
#             background-color: #40E0D0;
#             color: white;
#             padding: 10px;
#             border-radius: 5px;
#             margin-bottom: 20px;
#         }
#         /* Style for the file uploader */
#         .stFileUploader {
#             padding: 10px;
#             border: 2px dashed #40E0D0;
#             border-radius: 5px;
#             margin-bottom: 20px;
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     # Custom container for the title
#     st.markdown('<div class="title-box">', unsafe_allow_html=True)
#     st.title("INCIDENT MANAGEMENT DASHBOARD")
#     st.markdown('</div>', unsafe_allow_html=True)

#     # File uploader
#     uploaded_file = st.file_uploader("Upload Incident Document", type=['docx'])
    
#     if uploaded_file:
#         try:
#             # Initialize IncidentManager and process document
#             incident_manager = IncidentManager()
#             document_text = incident_manager.read_docx(uploaded_file)
#             incident_data = incident_manager.extract_incident_details(document_text)
            
#             # Store in session state for other views
#             st.session_state.detailed_issue_info = incident_data
            
#             # Header with incident ID and timestamp
#             st.markdown('<div class="status-header">', unsafe_allow_html=True)
#             col1, col2 = st.columns([3, 1])
#             with col1:
#                 st.markdown(f"### {incident_data['incident_id']} - {incident_data['short_description']}")
#             with col2:
#                 st.markdown(f"**Status**: {incident_data['status']}")
#                 st.markdown(f"**Time**: {incident_data['outage_time']}")
#             st.markdown('</div>', unsafe_allow_html=True)

#             # Current Status and Next Actions
#             col1, col2 = st.columns(2)
#             with col1:
#                 st.markdown('<div class="incident-box">', unsafe_allow_html=True)
#                 st.subheader("Current Status")
#                 st.markdown(incident_data['description'])
#                 st.markdown('</div>', unsafe_allow_html=True)
#             with col2:
#                 st.markdown('<div class="incident-box">', unsafe_allow_html=True)
#                 st.subheader("Next Actions")
#                 st.markdown(f"Next update expected at: {incident_data['next_update']}")
#                 if 'bridge_details' in incident_data:
#                     st.markdown("### Bridge Details")
#                     st.markdown(f"Platform: {incident_data['bridge_details']['platform']}")
#                     st.markdown(f"Meeting ID: {incident_data['bridge_details']['meeting_id']}")
#                     st.markdown(f"Passcode: {incident_data['bridge_details']['passcode']}")
#                 st.markdown('</div>', unsafe_allow_html=True)

#             # Issue Description
#             st.markdown('<div class="impact-box">', unsafe_allow_html=True)
#             st.subheader("Issue Description")
#             st.markdown(incident_data['description'])
#             st.markdown('</div>', unsafe_allow_html=True)

#             # Business Impact and MIM Communication
#             col1, col2 = st.columns(2)
#             with col1:
#                 st.markdown('<div class="impact-box">', unsafe_allow_html=True)
#                 st.subheader("Business Impact")
                
#                 # Services Impacted
#                 st.markdown("**Services Impacted**")
#                 for service in incident_data['impacted_services']:
#                     st.markdown(f"* {service}")
                
#                 # Business Impact Description
#                 st.markdown("**Impact Details**")
#                 st.markdown(incident_data['business_impact'])
                
#                 # Resolution Teams
#                 st.markdown("**Resolution Teams**")
#                 for team in incident_data['resolution_teams']:
#                     st.markdown(f"* {team}")
#                 st.markdown('</div>', unsafe_allow_html=True)

#             with col2:
#                 st.markdown('<div class="incident-box">', unsafe_allow_html=True)
#                 st.subheader("MIM Communication Status")
                
#                 # Create a styled table for communications
#                 communication_data = {
#                     "Communications": ["Open Comms (Hyper Link)", "Update 1 (Hyper Link)", 
#                                      "Update 2 (Hyper Link)", "Update 3 (Hyper Link)"],
#                     "Order": ["1", "3", "2", "4"],
#                     "Time": [incident_data['mim_notified_time'], "TBD", "7:30 AM", "TBD"],
#                     "Status": ["Published", "Not Published", "", ""]
#                 }
                
#                 import pandas as pd
#                 df = pd.DataFrame(communication_data)
#                 st.table(df)
#                 st.markdown('</div>', unsafe_allow_html=True)

#         except Exception as e:
#             st.error(f"Error processing document: {str(e)}")
#     else:
#         st.info("Please upload an incident document to view the dashboard.")

# def main():
#     st.set_page_config(
#         page_title="Major Incident Management",
#         page_icon="🚨",
#         layout="wide"
#     )
    
#     # Add custom styling for the sidebar
#     st.markdown("""
#         <style>
#         .css-1d391kg {
#             background-color: #40E0D0;
#         }
#         .sidebar .sidebar-content {
#             background-color: #40E0D0;
#         }
#         </style>
#     """, unsafe_allow_html=True)
    
#     st.markdown(CSS_STYLES, unsafe_allow_html=True)
    
#     # Initialize session state
#     initialize_session_state()
#     if 'settings' not in st.session_state:
#         st.session_state.settings = Settings()
    
#     # Sidebar navigation with new dashboard option
#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio("Go to", [
#         "Incident Dashboard",
#         "Incident Details", 
#         "Incident Summary", 
#         "Similar Historical Incidents"
#     ])
    
#     # Page routing with new dashboard
#     if page == "Incident Dashboard":
#         show_incident_dashboard()
#     elif page == "Incident Details":
#         incident_details.show()
#     elif page == "Incident Summary":
#         incident_summary.show()
#     else:
#         similar_historical_incidents.show()

# if __name__ == "__main__":
#     main()



#colourful with emojis, slightly compact

# import streamlit as st
# from views import incident_details, incident_summary, similar_historical_incidents
# from config.styles import CSS_STYLES
# from utils.session_state import initialize_session_state
# from config.settings import Settings
# from datetime import datetime
# from services.incident_manager import IncidentManager

# def show_incident_dashboard():
#     # Custom CSS for compact layout
#     st.markdown("""
#         <style>
#         /* Compact layout styles */
#         .main {
#             padding: 1rem !important;
#         }
#         .compact-box {
#             background-color: #f8f9fa;
#             border: 1px solid #ddd;
#             border-radius: 5px;
#             padding: 8px;
#             margin: 4px 0;
#             font-size: 0.9em;
#         }
#         .status-header {
#             background-color: #4169E1;
#             color: white;
#             padding: 8px;
#             border-radius: 5px;
#             margin: 4px 0;
#         }
#         .impact-box {
#             background-color: #9370DB;
#             color: white;
#             padding: 8px;
#             border-radius: 5px;
#             margin: 4px 0;
#         }
#         .title-box {
#             background-color: #40E0D0;
#             color: white;
#             padding: 8px;
#             border-radius: 5px;
#             margin-bottom: 10px;
#         }
#         /* Reduce padding and margins */
#         .stSelectbox, .stTextInput {
#             padding: 0 !important;
#             margin: 0 !important;
#         }
#         .row-widget {
#             padding: 0 !important;
#             margin: 0 !important;
#         }
#         /* Custom table styles */
#         .compact-table {
#             font-size: 0.85em;
#             margin: 4px 0;
#         }
#         .compact-table th, .compact-table td {
#             padding: 4px !important;
#         }
#         /* Reduce header sizes */
#         h1 {
#             font-size: 1.5em !important;
#             margin: 0 !important;
#             padding: 4px 0 !important;
#         }
#         h2 {
#             font-size: 1.2em !important;
#             margin: 0 !important;
#             padding: 4px 0 !important;
#         }
#         h3 {
#             font-size: 1.1em !important;
#             margin: 0 !important;
#             padding: 2px 0 !important;
#         }
#         /* Custom file uploader */
#         .stFileUploader {
#             padding: 5px !important;
#             border: 2px dashed #40E0D0;
#             border-radius: 5px;
#             margin-bottom: 10px !important;
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     # Compact file uploader
#     col1, col2, col3 = st.columns([2,1,1])
#     with col1:
#         uploaded_file = st.file_uploader("", type=['docx'])
    
#     if uploaded_file:
#         try:
#             incident_manager = IncidentManager()
#             document_text = incident_manager.read_docx(uploaded_file)
#             incident_data = incident_manager.extract_incident_details(document_text)
#             st.session_state.detailed_issue_info = incident_data
            
#             # Compact header with key information
#             st.markdown(f"""
#             <div class="status-header">
#                 <table width="100%">
#                     <tr>
#                         <td width="50%"><h2>{incident_data['incident_id']} - {incident_data['short_description']}</h2></td>
#                         <td width="25%">Status: {incident_data['status']}</td>
#                         <td width="25%">Time: {incident_data['outage_time']}</td>
#                     </tr>
#                 </table>
#             </div>
#             """, unsafe_allow_html=True)

#             # Three-column layout for key metrics
#             col1, col2, col3 = st.columns(3)
            
#             with col1:
#                 st.markdown('<div class="impact-box">', unsafe_allow_html=True)
#                 st.markdown("**🔄 Current Status**")
#                 st.markdown(incident_data['description'][:150] + "..." if len(incident_data['description']) > 150 else incident_data['description'])
#                 st.markdown('</div>', unsafe_allow_html=True)
                
#             with col2:
#                 st.markdown('<div class="impact-box">', unsafe_allow_html=True)
#                 st.markdown("**⚠️ Key Impacts**")
#                 st.markdown("• " + "\n• ".join(incident_data['impacted_services'][:3]))
#                 if len(incident_data['impacted_services']) > 3:
#                     st.markdown("*(+ more)*")
#                 st.markdown('</div>', unsafe_allow_html=True)
                
#             with col3:
#                 st.markdown('<div class="impact-box">', unsafe_allow_html=True)
#                 st.markdown("**👥 Resolution Teams**")
#                 st.markdown("• " + "\n• ".join(incident_data['resolution_teams'][:3]))
#                 if len(incident_data['resolution_teams']) > 3:
#                     st.markdown("*(+ more)*")
#                 st.markdown('</div>', unsafe_allow_html=True)

#             # Two-column layout for detailed information
#             col1, col2 = st.columns(2)
            
#             with col1:
#                 st.markdown('<div class="compact-box">', unsafe_allow_html=True)
#                 st.markdown("**🎯 Business Impact**")
#                 impact_summary = incident_data['business_impact'][:200] + "..." if len(incident_data['business_impact']) > 200 else incident_data['business_impact']
#                 st.markdown(impact_summary)
#                 st.markdown('</div>', unsafe_allow_html=True)

#             with col2:
#                 st.markdown('<div class="compact-box">', unsafe_allow_html=True)
#                 st.markdown("**📢 Communication Status**")
                
#                 # Simplified communication table
#                 comm_data = {
#                     "Update": ["Initial", "Update 1", "Update 2"],
#                     "Time": [incident_data['mim_notified_time'], "TBD", incident_data['next_update']],
#                     "Status": ["✅", "⏳", "🕒"]
#                 }
                
#                 import pandas as pd
#                 df = pd.DataFrame(comm_data)
#                 st.table(df)
#                 st.markdown('</div>', unsafe_allow_html=True)

#             # Bottom section for bridge details
#             if 'bridge_details' in incident_data:
#                 st.markdown('<div class="compact-box">', unsafe_allow_html=True)
#                 col1, col2, col3 = st.columns(3)
#                 with col1:
#                     st.markdown(f"**🔗 Bridge**: {incident_data['bridge_details']['platform']}")
#                 with col2:
#                     st.markdown(f"**🆔 Meeting ID**: {incident_data['bridge_details']['meeting_id']}")
#                 with col3:
#                     st.markdown(f"**🔑 Passcode**: {incident_data['bridge_details']['passcode']}")
#                 st.markdown('</div>', unsafe_allow_html=True)

#         except Exception as e:
#             st.error(f"Error: {str(e)}")
#     else:
#         st.info("Upload incident document to view dashboard")

# def main():
#     st.set_page_config(
#         page_title="Incident Management",
#         page_icon="🚨",
#         layout="wide",
#         initial_sidebar_state="collapsed"  # Start with collapsed sidebar for more space
#     )
    
#     # Sidebar styling
#     st.markdown("""
#         <style>
#         .css-1d391kg {
#             background-color: #40E0D0;
#         }
#         .sidebar .sidebar-content {
#             background-color: #40E0D0;
#         }
#         </style>
#     """, unsafe_allow_html=True)
    
#     st.markdown(CSS_STYLES, unsafe_allow_html=True)
#     initialize_session_state()
#     if 'settings' not in st.session_state:
#         st.session_state.settings = Settings()
    
#     # Sidebar navigation
#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio("Go to", [
#         "Incident Dashboard",
#         "Incident Details", 
#         "Incident Summary", 
#         "Similar Historical Incidents"
#     ])
    
#     # Page routing
#     if page == "Incident Dashboard":
#         show_incident_dashboard()
#     elif page == "Incident Details":
#         incident_details.show()
#     elif page == "Incident Summary":
#         incident_summary.show()
#     else:
#         similar_historical_incidents.show()

# if __name__ == "__main__":
#     main()

#executive dashbaord


# import streamlit as st
# from views import incident_details, incident_summary, similar_historical_incidents
# from config.styles import CSS_STYLES
# from utils.session_state import initialize_session_state
# from config.settings import Settings
# from datetime import datetime
# from services.incident_manager import IncidentManager

# def show_executive_dashboard():
#     # Custom CSS for compact layout
#     st.markdown("""
#         <style>
#         .main {
#             padding: 1rem !important;
#         }
#         .compact-box {
#             background-color: #f8f9fa;
#             border: 1px solid #ddd;
#             border-radius: 5px;
#             padding: 8px;
#             margin: 4px 0;
#             font-size: 0.9em;
#         }
#         .status-header {
#             background-color: #4169E1;
#             color: white;
#             padding: 8px;
#             border-radius: 5px;
#             margin: 4px 0;
#         }
#         .impact-box {
#             background-color: #9370DB;
#             color: white;
#             padding: 8px;
#             border-radius: 5px;
#             margin: 4px 0;
#         }
#         .title-box {
#             background-color: #40E0D0;
#             color: white;
#             padding: 8px;
#             border-radius: 5px;
#             margin-bottom: 10px;
#         }
#         .stSelectbox, .stTextInput {
#             padding: 0 !important;
#             margin: 0 !important;
#         }
#         .row-widget {
#             padding: 0 !important;
#             margin: 0 !important;
#         }
#         .compact-table {
#             font-size: 0.85em;
#             margin: 4px 0;
#         }
#         .compact-table th, .compact-table td {
#             padding: 4px !important;
#         }
#         h1 {
#             font-size: 1.5em !important;
#             margin: 0 !important;
#             padding: 4px 0 !important;
#         }
#         h2 {
#             font-size: 1.2em !important;
#             margin: 0 !important;
#             padding: 4px 0 !important;
#         }
#         h3 {
#             font-size: 1.1em !important;
#             margin: 0 !important;
#             padding: 2px 0 !important;
#         }
#         .stFileUploader {
#             padding: 5px !important;
#             border: 2px dashed #40E0D0;
#             border-radius: 5px;
#             margin-bottom: 10px !important;
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     # Title
#     st.markdown('<div class="title-box"><h1>EXECUTIVE DASHBOARD - MAJOR INCIDENT MANAGEMENT</h1></div>', unsafe_allow_html=True)

#     # Compact file uploader
#     col1, col2, col3 = st.columns([2,1,1])
#     with col1:
#         uploaded_file = st.file_uploader("", type=['docx'])
    
#     if uploaded_file:
#         try:
#             incident_manager = IncidentManager()
#             document_text = incident_manager.read_docx(uploaded_file)
#             incident_data = incident_manager.extract_incident_details(document_text)
#             st.session_state.detailed_issue_info = incident_data
            
#             # Compact header with key information
#             st.markdown(f"""
#             <div class="status-header">
#                 <table width="100%">
#                     <tr>
#                         <td width="50%"><h2>{incident_data['incident_id']} - {incident_data['short_description']}</h2></td>
#                         <td width="25%">Status: {incident_data['status']}</td>
#                         <td width="25%">Time: {incident_data['outage_time']}</td>
#                     </tr>
#                 </table>
#             </div>
#             """, unsafe_allow_html=True)

#             # Three-column layout for key metrics
#             col1, col2, col3 = st.columns(3)
            
#             with col1:
#                 st.markdown('<div class="impact-box">', unsafe_allow_html=True)
#                 st.markdown("**Current Status**")
#                 st.markdown(incident_data['description'][:150] + "..." if len(incident_data['description']) > 150 else incident_data['description'])
#                 st.markdown('</div>', unsafe_allow_html=True)
                
#             with col2:
#                 st.markdown('<div class="impact-box">', unsafe_allow_html=True)
#                 st.markdown("**Key Impacts**")
#                 st.markdown("• " + "\n• ".join(incident_data['impacted_services'][:3]))
#                 if len(incident_data['impacted_services']) > 3:
#                     st.markdown("*(+ additional services)*")
#                 st.markdown('</div>', unsafe_allow_html=True)
                
#             with col3:
#                 st.markdown('<div class="impact-box">', unsafe_allow_html=True)
#                 st.markdown("**Resolution Teams**")
#                 st.markdown("• " + "\n• ".join(incident_data['resolution_teams'][:3]))
#                 if len(incident_data['resolution_teams']) > 3:
#                     st.markdown("*(+ additional teams)*")
#                 st.markdown('</div>', unsafe_allow_html=True)

#             # Two-column layout for detailed information
#             col1, col2 = st.columns(2)
            
#             with col1:
#                 st.markdown('<div class="compact-box">', unsafe_allow_html=True)
#                 st.markdown("**Business Impact**")
#                 impact_summary = incident_data['business_impact'][:200] + "..." if len(incident_data['business_impact']) > 200 else incident_data['business_impact']
#                 st.markdown(impact_summary)
#                 st.markdown('</div>', unsafe_allow_html=True)

#             with col2:
#                 st.markdown('<div class="compact-box">', unsafe_allow_html=True)
#                 st.markdown("**Communication Status**")
                
#                 # Simplified communication table
#                 comm_data = {
#                     "Update": ["Initial", "Update 1", "Update 2"],
#                     "Time": [incident_data['mim_notified_time'], "TBD", incident_data['next_update']],
#                     "Status": ["Published", "Pending", "Scheduled"]
#                 }
                
#                 import pandas as pd
#                 df = pd.DataFrame(comm_data)
#                 st.table(df)
#                 st.markdown('</div>', unsafe_allow_html=True)

#             # Bottom section for bridge details
#             if 'bridge_details' in incident_data:
#                 st.markdown('<div class="compact-box">', unsafe_allow_html=True)
#                 col1, col2, col3 = st.columns(3)
#                 with col1:
#                     st.markdown(f"**Bridge Platform**: {incident_data['bridge_details']['platform']}")
#                 with col2:
#                     st.markdown(f"**Meeting ID**: {incident_data['bridge_details']['meeting_id']}")
#                 with col3:
#                     st.markdown(f"**Passcode**: {incident_data['bridge_details']['passcode']}")
#                 st.markdown('</div>', unsafe_allow_html=True)

#         except Exception as e:
#             st.error(f"Error: {str(e)}")
#     else:
#         st.info("Upload incident document to view executive dashboard")

# def main():
#     st.set_page_config(
#         page_title="Executive Dashboard",
#         page_icon="🚨",
#         layout="wide",
#         initial_sidebar_state="collapsed"
#     )
    
#     # Sidebar styling
#     st.markdown("""
#         <style>
#         .css-1d391kg {
#             background-color: #40E0D0;
#         }
#         .sidebar .sidebar-content {
#             background-color: #40E0D0;
#         }
#         </style>
#     """, unsafe_allow_html=True)
    
#     st.markdown(CSS_STYLES, unsafe_allow_html=True)
#     initialize_session_state()
#     if 'settings' not in st.session_state:
#         st.session_state.settings = Settings()
    
#     # Sidebar navigation
#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio("Go to", [
#         "Executive Dashboard",
#         "Incident Details", 
#         "Incident Summary", 
#         "Similar Historical Incidents"
#     ])
    
#     # Page routing
#     if page == "Executive Dashboard":
#         show_executive_dashboard()
#     elif page == "Incident Details":
#         incident_details.show()
#     elif page == "Incident Summary":
#         incident_summary.show()
#     else:
#         similar_historical_incidents.show()

# if __name__ == "__main__":
#     main()




# import streamlit as st
# from views.incident_details import show as show_details
# from views.incident_summary import show as show_summary
# from views.similar_historical_incidents import show as show_similar
# from config.styles import CSS_STYLES
# from utils.session_state import initialize_session_state
# from config.settings import Settings
# from datetime import datetime
# from services.incident_manager import IncidentManager

# import streamlit as st
# from views import incident_details, incident_summary, similar_historical_incidents
# from config.styles import CSS_STYLES
# from utils.session_state import initialize_session_state
# from config.settings import Settings
# from datetime import datetime
# from services.detail_extractor import IncidentDetailExtractor  # Add this import
# from services.incident_manager import IncidentManager
# from ui.shared_components import show_document_upload

# def show_executive_dashboard():
#     # Enhanced CSS with more colors
#     st.markdown("""
#         <style>
#         .main {
#             padding: 1rem !important;
#         }
#         .compact-box {
#             background-color: #f8f9fa;
#             border: 1px solid #ddd;
#             border-radius: 5px;
#             padding: 8px;
#             margin: 4px 0;
#             font-size: 0.9em;
#         }
#         .status-header {
#             background-color: #4169E1;
#             color: white;
#             padding: 8px;
#             border-radius: 5px;
#             margin: 4px 0;
#         }
#         .impact-box {
#             background-color: #9370DB;
#             color: white;
#             padding: 8px;
#             border-radius: 5px;
#             margin: 4px 0;
#         }
#         .business-impact-box {
#             background-color: #6A5ACD;
#             color: white;
#             padding: 8px;
#             border-radius: 5px;
#             margin: 4px 0;
#         }
#         .communication-box {
#             background-color: #7B68EE;
#             color: white;
#             padding: 8px;
#             border-radius: 5px;
#             margin: 4px 0;
#         }
#         .bridge-box {
#             background: linear-gradient(135deg, #40E0D0, #4169E1);
#             color: white;
#             padding: 8px;
#             border-radius: 5px;
#             margin: 4px 0;
#         }
#         .title-box {
#             background-color: #40E0D0;
#             color: white;
#             padding: 8px;
#             border-radius: 5px;
#             margin-bottom: 10px;
#         }
#         .stSelectbox, .stTextInput {
#             padding: 0 !important;
#             margin: 0 !important;
#         }
#         .row-widget {
#             padding: 0 !important;
#             margin: 0 !important;
#         }
#         .compact-table {
#             font-size: 0.85em;
#             margin: 4px 0;
#             background-color: rgba(255, 255, 255, 0.1);
#         }
#         .compact-table th, .compact-table td {
#             padding: 4px !important;
#             color: white;
#         }
#         h1 {
#             font-size: 1.5em !important;
#             margin: 0 !important;
#             padding: 4px 0 !important;
#         }
#         h2 {
#             font-size: 1.2em !important;
#             margin: 0 !important;
#             padding: 4px 0 !important;
#         }
#         h3 {
#             font-size: 1.1em !important;
#             margin: 0 !important;
#             padding: 2px 0 !important;
#         }
#         .stFileUploader {
#             padding: 5px !important;
#             border: 2px dashed #40E0D0;
#             border-radius: 5px;
#             margin-bottom: 10px !important;
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     # Title with emoji
#     st.markdown('<div class="title-box"><h1>🎯 EXECUTIVE DASHBOARD - MAJOR INCIDENT MANAGEMENT</h1></div>', unsafe_allow_html=True)

#     # File uploader
#     col1, col2, col3 = st.columns([2,1,1])
#     with col1:
#         uploaded_file = st.file_uploader("", type=['docx'])
    
#     if uploaded_file:
#         try:
#             incident_manager = IncidentManager()
#             document_text = incident_manager.read_docx(uploaded_file)
#             incident_data = incident_manager.extract_incident_details(document_text)
#             st.session_state.detailed_issue_info = incident_data
            
#             # Header with incident info
#             st.markdown(f"""
#             <div class="status-header">
#                 <table width="100%">
#                     <tr>
#                         <td width="50%"><h2>🚨 {incident_data['incident_id']} - {incident_data['short_description']}</h2></td>
#                         <td width="25%">🔄 Status: {incident_data['status']}</td>
#                         <td width="25%">⏰ Time: {incident_data['outage_time']}</td>
#                     </tr>
#                 </table>
#             </div>
#             """, unsafe_allow_html=True)

#             # Top metrics
#             col1, col2, col3 = st.columns(3)
            
#             with col1:
#                 st.markdown('<div class="impact-box">', unsafe_allow_html=True)
#                 st.markdown("**🔄 Current Status**")
#                 st.markdown(incident_data['description'][:150] + "..." if len(incident_data['description']) > 150 else incident_data['description'])
#                 st.markdown('</div>', unsafe_allow_html=True)
                
#             with col2:
#                 st.markdown('<div class="impact-box">', unsafe_allow_html=True)
#                 st.markdown("**⚠️ Key Impacts**")
#                 st.markdown("• " + "\n• ".join(incident_data['impacted_services'][:3]))
#                 if len(incident_data['impacted_services']) > 3:
#                     st.markdown("*(+ additional services)*")
#                 st.markdown('</div>', unsafe_allow_html=True)
                
#             with col3:
#                 st.markdown('<div class="impact-box">', unsafe_allow_html=True)
#                 st.markdown("**👥 Resolution Teams**")
#                 st.markdown("• " + "\n• ".join(incident_data['resolution_teams'][:3]))
#                 if len(incident_data['resolution_teams']) > 3:
#                     st.markdown("*(+ additional teams)*")
#                 st.markdown('</div>', unsafe_allow_html=True)

#             # Bottom section with enhanced colors
#             col1, col2 = st.columns(2)
            
#             with col1:
#                 st.markdown('<div class="business-impact-box">', unsafe_allow_html=True)
#                 st.markdown("**💼 Business Impact Analysis**")
#                 impact_summary = incident_data['business_impact'][:200] + "..." if len(incident_data['business_impact']) > 200 else incident_data['business_impact']
#                 st.markdown(impact_summary)
#                 st.markdown('</div>', unsafe_allow_html=True)

#             with col2:
#                 st.markdown('<div class="communication-box">', unsafe_allow_html=True)
#                 st.markdown("**📢 Communication Status**")
                
#                 # Enhanced communication table
#                 comm_data = {
#                     "Update": ["📝 Initial", "🔄 Update 1", "📌 Update 2"],
#                     "Time": [incident_data['mim_notified_time'], "TBD", incident_data['next_update']],
#                     "Status": ["✅ Published", "⏳ Pending", "🕒 Scheduled"]
#                 }
                
#                 import pandas as pd
#                 df = pd.DataFrame(comm_data)
#                 st.table(df)
#                 st.markdown('</div>', unsafe_allow_html=True)

#             # Bridge details with gradient background
#             if 'bridge_details' in incident_data:
#                 st.markdown('<div class="bridge-box">', unsafe_allow_html=True)
#                 col1, col2, col3 = st.columns(3)
#                 with col1:
#                     st.markdown(f"**🌐 Bridge Platform**: {incident_data['bridge_details']['platform']}")
#                 with col2:
#                     st.markdown(f"**🆔 Meeting ID**: {incident_data['bridge_details']['meeting_id']}")
#                 with col3:
#                     st.markdown(f"**🔑 Passcode**: {incident_data['bridge_details']['passcode']}")
#                 st.markdown('</div>', unsafe_allow_html=True)

#         except Exception as e:
#             st.error(f"Error: {str(e)}")
#     else:
#         st.info("📤 Upload incident document to view executive dashboard")

        
# def process_uploaded_document(uploaded_file):
#     """Process the uploaded document and store results in session state"""
#     try:
#         # Process with IncidentManager
#         incident_manager = IncidentManager()
#         document_text = incident_manager.read_docx(uploaded_file)
#         incident_data = incident_manager.extract_incident_details(document_text)
#         st.session_state.detailed_issue_info = incident_data
        
#         # Store transcript for other views
#         st.session_state.transcript = document_text
        
#         # Process with DetailExtractor if needed
#         if 'settings' in st.session_state:
#             detailed_extractor = IncidentDetailExtractor(st.session_state.settings.OPENAI_API_KEY)
#             detailed_info = detailed_extractor.extract_detailed_issue_info(document_text)
#             if detailed_info:
#                 st.session_state.detailed_issue_info.update(detailed_info)
                
#         return True
#     except Exception as e:
#         st.error(f"Error processing document: {str(e)}")
#         return False


# def main():
#     st.set_page_config(
#         page_title="Executive Dashboard",
#         page_icon="🎯",
#         layout="wide",
#         initial_sidebar_state="collapsed"
#     )
    
#     st.markdown(CSS_STYLES, unsafe_allow_html=True)
#     initialize_session_state()
#     if 'settings' not in st.session_state:
#         st.session_state.settings = Settings()
    
#     # Sidebar navigation
#     st.sidebar.title("🎯 Navigation")
#     page = st.sidebar.radio("Go to", [
#         "Executive Dashboard",
#         "Incident Details", 
#         "Incident Summary", 
#         "Similar Historical Incidents"
#     ])
    
# #     # Updated page routing with new function names
# #     if page == "Executive Dashboard":
# #         show_executive_dashboard()
# #     elif page == "Incident Details":
# #         show_details()
# #     elif page == "Incident Summary":
# #         show_summary()
# #     else:
# #         show_similar()

# # if __name__ == "__main__":
# #     main()

#     if page == "Executive Dashboard":
#         show_executive_dashboard()
#     elif page == "Incident Details":
#         incident_details.show()
#     elif page == "Incident Summary":
#         incident_summary.show()
#     else:
#         similar_historical_incidents.show()

# if __name__ == "__main__":
#     main()

import streamlit as st
from views import incident_details, incident_summary, similar_historical_incidents
from config.styles import CSS_STYLES
from utils.session_state import initialize_session_state
from config.settings import Settings
from datetime import datetime
from services.incident_manager import IncidentManager
from services.detail_extractor import IncidentDetailExtractor
import pandas as pd

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
        .stSelectbox, .stTextInput {
            padding: 0 !important;
            margin: 0 !important;
        }
        .row-widget {
            padding: 0 !important;
            margin: 0 !important;
        }
        .compact-table {
            font-size: 0.85em;
            margin: 4px 0;
            background-color: rgba(255, 255, 255, 0.1);
        }
        .compact-table th, .compact-table td {
            padding: 4px !important;
            color: white;
        }
        h1 {
            font-size: 1.5em !important;
            margin: 0 !important;
            padding: 4px 0 !important;
        }
        h2 {
            font-size: 1.2em !important;
            margin: 0 !important;
            padding: 4px 0 !important;
        }
        h3 {
            font-size: 1.1em !important;
            margin: 0 !important;
            padding: 2px 0 !important;
        }
        .stFileUploader {
            padding: 5px !important;
            border: 2px dashed #40E0D0;
            border-radius: 5px;
            margin-bottom: 10px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title with emoji
    st.markdown('<div class="title-box"><h1>🎯 EXECUTIVE DASHBOARD - MAJOR INCIDENT MANAGEMENT</h1></div>', unsafe_allow_html=True)

    # File uploader
    col1, col2, col3 = st.columns([2,1,1])
    with col1:
        uploaded_file = st.file_uploader("", type=['docx'])
    
    if uploaded_file:
        try:
            # Process with IncidentManager
            incident_manager = IncidentManager()
            document_text = incident_manager.read_docx(uploaded_file)
            st.session_state.transcript = document_text
            
            # Process with DetailExtractor
            if 'settings' in st.session_state:
                detailed_extractor = IncidentDetailExtractor(st.session_state.settings.OPENAI_API_KEY)
                incident_data = detailed_extractor.extract_detailed_issue_info(document_text)
                if incident_data:
                    st.session_state.detailed_issue_info = incident_data
                else:
                    st.error("Could not extract incident details from the document")
            
            incident_data = st.session_state.get('detailed_issue_info', {})
            
            # Header with incident info
            st.markdown(f"""
            <div class="status-header">
                <table width="100%">
                    <tr>
                        <td width="50%"><h2>🚨 {incident_data.get('incident_id', 'N/A')} - {incident_data.get('short_description', 'N/A')}</h2></td>
                        <td width="25%">🔄 Status: {incident_data.get('status', 'N/A')}</td>
                        <td width="25%">⏰ Time: {incident_data.get('outage_time', 'N/A')}</td>
                    </tr>
                </table>
            </div>
            """, unsafe_allow_html=True)

            # Top metrics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown('<div class="impact-box">', unsafe_allow_html=True)
                st.markdown("**🔄 Current Status**")
                description = incident_data.get('description', 'N/A')
                st.markdown(description[:150] + "..." if len(description) > 150 else description)
                st.markdown('</div>', unsafe_allow_html=True)
                
            with col2:
                st.markdown('<div class="impact-box">', unsafe_allow_html=True)
                st.markdown("**⚠️ Key Impacts**")
                impacted_services = incident_data.get('impacted_services', [])
                if isinstance(impacted_services, list) and impacted_services:
                    st.markdown("• " + "\n• ".join(impacted_services[:3]))
                    if len(impacted_services) > 3:
                        st.markdown("*(+ additional services)*")
                else:
                    st.markdown("No impacted services reported")
                st.markdown('</div>', unsafe_allow_html=True)
                
            with col3:
                st.markdown('<div class="impact-box">', unsafe_allow_html=True)
                st.markdown("**👥 Resolution Teams**")
                resolution_teams = incident_data.get('resolution_teams', [])
                if isinstance(resolution_teams, list) and resolution_teams:
                    st.markdown("• " + "\n• ".join(resolution_teams[:3]))
                    if len(resolution_teams) > 3:
                        st.markdown("*(+ additional teams)*")
                else:
                    st.markdown("No resolution teams specified")
                st.markdown('</div>', unsafe_allow_html=True)

            # Bottom section
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown('<div class="business-impact-box">', unsafe_allow_html=True)
                st.markdown("**💼 Business Impact Analysis**")
                impact = incident_data.get('business_impact', 'No business impact information available')
                impact_summary = impact[:200] + "..." if len(impact) > 200 else impact
                st.markdown(impact_summary)
                st.markdown('</div>', unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="communication-box">', unsafe_allow_html=True)
                st.markdown("**📢 Communication Status**")
                
                # Enhanced communication table
                comm_data = {
                    "Update": ["📝 Initial", "🔄 Update 1", "📌 Update 2"],
                    "Time": [
                        incident_data.get('mim_notified_time', 'N/A'),
                        "TBD",
                        incident_data.get('next_update', 'TBD')
                    ],
                    "Status": ["✅ Published", "⏳ Pending", "🕒 Scheduled"]
                }
                
                df = pd.DataFrame(comm_data)
                st.table(df)
                st.markdown('</div>', unsafe_allow_html=True)

            # Bridge details with proper error handling
            bridge_info = incident_data.get('bridge_details', {})
            if isinstance(bridge_info, dict) and bridge_info:
                st.markdown('<div class="bridge-box">', unsafe_allow_html=True)
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"**🌐 Bridge Platform**: {bridge_info.get('platform', 'N/A')}")
                with col2:
                    st.markdown(f"**🆔 Meeting ID**: {bridge_info.get('meeting_id', 'N/A')}")
                with col3:
                    st.markdown(f"**🔑 Passcode**: {bridge_info.get('passcode', 'N/A')}")
                st.markdown('</div>', unsafe_allow_html=True)

            # Process Links
            st.markdown('<div class="bridge-box">', unsafe_allow_html=True)
            st.markdown("**🔗 Key Process Links**")
            process_links = incident_data.get('process_links', {})
            if isinstance(process_links, dict) and process_links:
                for title, link in process_links.items():
                    st.markdown(f"- [{title}]({link})")
            else:
                st.markdown("No process links available")
            st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.info("📤 Upload incident document to view executive dashboard")

def main():
    st.set_page_config(
        page_title="Executive Dashboard",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="collapsed"
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
    initialize_session_state()
    if 'settings' not in st.session_state:
        st.session_state.settings = Settings()
    
    # Sidebar navigation
    st.sidebar.title("🎯 Navigation")
    page = st.sidebar.radio("Go to", [
        "Executive Dashboard",
        "Incident Details", 
        "Incident Summary", 
        "Similar Historical Incidents"
    ])
    
    # Page routing with document uploader on each page
    if page == "Executive Dashboard":
        show_executive_dashboard()
    elif page == "Incident Details":
        st.markdown('<div class="title-box"><h1>🔍 INCIDENT DETAILS</h1></div>', unsafe_allow_html=True)
        
        # File upload handling
        uploaded_file = st.file_uploader("Upload Document", type=['docx'], key="details_uploader")
        if uploaded_file:
            try:
                # Process with IncidentManager
                incident_manager = IncidentManager()
                document_text = incident_manager.read_docx(uploaded_file)
                st.session_state.transcript = document_text
                
                # Get base incident data
                base_incident_data = incident_manager.extract_incident_details(document_text)
                
                # Process with DetailExtractor if settings available
                if 'settings' in st.session_state:
                    detailed_extractor = IncidentDetailExtractor(st.session_state.settings.OPENAI_API_KEY)
                    detailed_info = detailed_extractor.extract_detailed_issue_info(document_text)
                    if detailed_info:
                        st.session_state.detailed_issue_info = detailed_info
                        st.success("✅ Document processed successfully!")
                    else:
                        st.warning("⚠️ Could not extract detailed information from the document")
                else:
                    st.error("⚠️ OpenAI API key not configured in settings")
            except Exception as e:
                st.error(f"Error: {str(e)}")
        
        # Show incident details view
        incident_details.show()
    elif page == "Incident Summary":
        st.markdown('<div class="title-box"><h1>📊 INCIDENT SUMMARY</h1></div>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload Document", type=['docx'], key="summary_uploader")
        if uploaded_file:
            try:
                incident_manager = IncidentManager()
                document_text = incident_manager.read_docx(uploaded_file)
                st.session_state.transcript = document_text
                if 'settings' in st.session_state:
                    detailed_extractor = IncidentDetailExtractor(st.session_state.settings.OPENAI_API_KEY)
                    incident_data = detailed_extractor.extract_detailed_issue_info(document_text)
                    if incident_data:
                        st.session_state.detailed_issue_info = incident_data
            except Exception as e:
                st.error(f"Error: {str(e)}")
        incident_summary.show()
    else:
        similar_historical_incidents.show()

if __name__ == "__main__":
    main()



















































































































