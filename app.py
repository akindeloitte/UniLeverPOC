# #BEST
# import streamlit as st
# from views import incident_details, incident_summary, similar_historical_incidents
# from config.styles import CSS_STYLES
# from utils.session_state import initialize_session_state
# from config.settings import Settings
# from datetime import datetime
# from services.incident_manager import IncidentManager
# from services.detail_extractor import IncidentDetailExtractor
# from ui.counter import create_timer_app, create_status_cards
# import pandas as pd
# import streamlit.components.v1 as components
# from services.groq_extractor import GroqDetailExtractor
# import logging
# from ui.exec_timer import create_exec_timer, initialize_exec_timer, start_exec_timer

# from streamlit_navigation_bar import st_navbar

# #from st_pages import Page, show_pages, add_page_title
# from st_pages import add_page_title, get_nav_from_toml

# # Configure logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

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
#         .incident-header {
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#             margin-bottom: 10px;
#             padding: 10px;
#             background-color: white;
#             border-radius: 5px;
#             box-shadow: 0 2px 4px rgba(0,0,0,0.1);
#         }
#         .duration-box {
#             border: 2px solid #ff4444;
#             border-radius: 50%;
#             padding: 10px 15px;
#             color: #ff4444;
#             font-weight: bold;
#             font-size: 1.2em;
#         }
#         .blue-header {
#             background-color: #0066cc;
#             color: white;
#             padding: 10px;
#             border-radius: 5px 5px 0 0;
#             margin: 4px 0 0 0;
#         }
#         .white-content {
#             background-color: white;
#             border: 1px solid #ddd;
#             padding: 10px;
#             border-radius: 0 0 5px 5px;
#             margin: 0 0 10px 0;
#         }
#         .purple-box {
#             background-color: #8a2be2;
#             color: white;
#             padding: 8px;
#             margin: 4px 0;
#             border-radius: 5px;
#         }
#         /* Additional dashboard styling */
#         .dashboard-metrics {
#             padding: 15px;
#             border-radius: 5px;
#             margin-bottom: 15px;
#         }
#         .incident-status {
#             font-weight: bold;
#             padding: 5px 10px;
#             border-radius: 3px;
#             display: inline-block;
#         }
#         .status-active {
#             background-color: #dc3545;
#             color: white;
#         }
#         .metric-card {
#             background: white;
#             padding: 15px;
#             border-radius: 5px;
#             box-shadow: 0 2px 4px rgba(0,0,0,0.1);
#             margin-bottom: 15px;
#         }
#         .metric-title {
#             color: #666;
#             font-size: 0.9em;
#             margin-bottom: 5px;
#         }
#         .metric-value {
#             font-size: 1.2em;
#             font-weight: bold;
#             color: #333;
#         }
#         .upload-section {
#             padding: 20px;
#             border-radius: 5px;
#             background-color: #f8f9fa;
#             margin-bottom: 20px;
#         }
#         </style>
#     """, unsafe_allow_html=True)

    
#     with st.sidebar:
#         st.markdown("### 📂 Document Upload")
#         uploaded_file = st.file_uploader("Upload Incident Document", type=['docx'], key="main_uploader")
        
        
#         if uploaded_file:
#             try:
#                 # Start timer when file is uploaded
#                 start_exec_timer()

              
                    
#                     # st.session_state.current_phase = 1 #new
#                     # st.session_state.current_phase_start = datetime.now() #new


#                 incident_manager = IncidentManager()
#                 document_text = incident_manager.read_docx(uploaded_file)
#                 st.session_state.transcript = document_text
                
               
#                 if 'settings' in st.session_state:
#                     # Original OpenAI extraction
#                     detailed_extractor = IncidentDetailExtractor(st.session_state.settings.OPENAI_API_KEY)
#                     incident_data = detailed_extractor.extract_detailed_issue_info(document_text)
                    
#                     if incident_data:
#                         # Additional Groq extraction
#                         try:
#                             groq_extractor = GroqDetailExtractor(st.session_state.settings.GROQ_API_KEY)
#                             groq_details = groq_extractor.extract_description_and_actions(document_text)
                            
#                             if groq_details:
#                                 # Update description and workaround
#                                 if 'issue_description' not in incident_data:
#                                     incident_data['issue_description'] = {}
                                
#                                 incident_data['issue_description']['description'] = groq_details.get('description', 
#                                     incident_data.get('issue_description', {}).get('description', ''))
#                                 incident_data['issue_description']['workaround'] = groq_details.get('workaround',
#                                     incident_data.get('issue_description', {}).get('workaround', ''))
                                
#                                 # Update next actions if available from Groq
#                                 if groq_details.get('next_actions'):
#                                     incident_data['next_actions'] = groq_details['next_actions']
                            
#                         except Exception as groq_error:
#                             logging.error(f"Groq extraction failed: {str(groq_error)}")
#                             # Continue with original OpenAI data if Groq fails
                            
#                         st.session_state.detailed_issue_info = incident_data
#                         st.sidebar.success("✅ Document processed successfully!")
#                     else:
#                         st.sidebar.error("Failed to extract incident details")
#             except Exception as e:
#                 st.sidebar.error(f"Error: {str(e)}")

#     # Title
#     st.markdown('<div class="title-box"><h1>🎯 EXECUTIVE DASHBOARD - MAJOR INCIDENT MANAGEMENT</h1></div>', unsafe_allow_html=True)
    

#     # Check for incident data in session state with proper null checks
#     if 'detailed_issue_info' in st.session_state and st.session_state.detailed_issue_info is not None:
#         incident_data = st.session_state.detailed_issue_info
        
#         # Clean location handling with proper null checks
#         all_locations = set()  # Using set to automatically handle duplicates
        
#         # Collect locations from all possible fields
#         issue_location = incident_data.get('issue_location', '')
#         affected_location = incident_data.get('affected_location', '')
        
#         if issue_location:
#             all_locations.update(loc.strip() for loc in issue_location.replace(' and ', ', ').split(','))
#         if affected_location:
#             all_locations.update(loc.strip() for loc in affected_location.replace(' and ', ', ').split(','))
            
#         # Clean and standardize locations with proper filtering
#         cleaned_locations = sorted(set(
#             loc.strip().replace('Bangalore', 'Bengaluru').title()
#             for loc in all_locations
#             if loc and loc.strip() and loc.strip() != 'N/A'
#         ))
        
#         # Format locations for display
#         location_str = ' and '.join(cleaned_locations) if cleaned_locations else ''

        
#       # Get incident details with proper null checks
#         incident_id = incident_data.get('incident_id', '')
#         issue_description = incident_data.get('short_description', '')
#         priority = incident_data.get('priority_level', '')
        
#         # Create header text with clean format
#         header_text = f"{incident_id} - {issue_description}"
#         if location_str:
#             header_text += f" at {location_str}"
        
        
      
#         incident_id = incident_data.get('incident_id', '')
#         issue_description = incident_data.get('short_description', '')
#         priority = incident_data.get('priority_level', '')
        
#         # Create header text with clean format
#         header_text = f"{incident_id} - {issue_description}"
#         if location_str:
#             header_text += f" at {location_str}"

        



#         header_text = f"{incident_id} - {issue_description}"
#         if location_str:
#             header_text += f" at {location_str}"
            
#         timer_html = create_exec_timer()
        
#         st.markdown(f"""
#         <div class="incident-header">
#             <div style="display: flex; align-items: center; gap: 10px;">
#                 <h2>{header_text}</h2>
#                 <div style="display: flex; align-items: center; gap: 10px;">
#                     {f'<span style="background-color: #ff4444; color: white; padding: 5px 12px; border-radius: 15px; font-weight: bold; font-size: 0.9em;">{priority}</span>' if priority else ''}
#                      <div class="duration-box" id="incident-duration">00:00:00</div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

        
#         # Main content in two columns
#         main_col1, main_col2 = st.columns([7, 3])
        
#         with main_col1:
#             # Current Status
#             st.markdown('<div class="blue-header">🔄 Current Status</div>', unsafe_allow_html=True)
#             st.markdown(f'<div class="white-content">{incident_data.get("description", "N/A")}</div>', unsafe_allow_html=True)
            
           

#             st.markdown('<div class="blue-header">⏭️ Next Actions:</div>', unsafe_allow_html=True)
#             next_actions = incident_data.get('next_actions', [])
#             if next_actions:
#                 formatted_actions = "<div class='white-content'>"
#                 for action in next_actions:
#                     # Clean and properly capitalize the action
#                     clean_action = (action.replace('*', '')
#                                        .replace('•', '')
#                                        .strip()
#                                        .replace('dba', 'DBA')
#                                        .replace('dr', 'DR')
#                                        .replace('sap', 'SAP')
#                                        .replace('erp', 'ERP')
#                                        .replace('sre', 'SRE')
#                                        .replace('unix', 'UNIX'))
                    
#                     # Add bullet point and line break
#                     formatted_actions += f"• {clean_action}<br><br>"
                
#                 formatted_actions += "</div>"
#                 st.markdown(formatted_actions, unsafe_allow_html=True)
#             else:
#                 st.markdown("<div class='white-content'>No immediate actions required</div>", unsafe_allow_html=True)
            
           
#             st.markdown('<div class="blue-header">⚠️ Issue Description</div>', unsafe_allow_html=True)
            
#             # Get and format description with bullet points
#             system_info = "The ERP Central Application is inaccessible to multiple users in Bengaluru and Mumbai offices."
#             root_cause = "The database was in an incorrect state due to manual termination of an earlier backup."
#             timing = "The incident started at 9:53 PM UTC."
#             impact = "Multiple users are prevented from logging into the application, affecting operations across both locations."
            
#             formatted_description = f"""
#                 <div class="white-content">
#                     <strong>{header_text}</strong><br><br>
#                     • {system_info}<br><br>
#                     • {root_cause}<br><br>
#                     • {timing}<br><br>
#                     • {impact}<br><br>
#                     <strong>Work Around:</strong> {incident_data.get('issue_description', {}).get('workaround', '').capitalize()}
#                 </div>
#             """
            
#             st.markdown(formatted_description, unsafe_allow_html=True)
            
#             # Business Impact
#             st.markdown('<div class="blue-header">💼 Business Impact</div>', unsafe_allow_html=True)
            
#             # Applications
#             st.markdown('<div class="purple-box">Application (s)</div>', unsafe_allow_html=True)
#             services = incident_data.get('impacted_services', [])
#             st.markdown(f"""
#             <div class="white-content">
#                 <strong>Top Services Impacted: </strong>{', '.join(services) if services else 'N/A'}
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Geography
#             st.markdown('<div class="purple-box">Geography (S)</div>', unsafe_allow_html=True)
#             st.markdown(f"""
#             <div class="white-content">
#                 <strong>Sites Impacted: </strong>{location_str if location_str else 'N/A'}
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Process/Activities
#             st.markdown('<div class="purple-box">Process / Activities Impacted</div>', unsafe_allow_html=True)
#             st.markdown(f"""
#             <div class="white-content">
#                 <strong>Activities Impacted: </strong>{incident_data.get('activities_impacted', 'N/A')}
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Key Stakeholders
#             st.markdown('<div class="purple-box">Key Stakeholder Engaged</div>', unsafe_allow_html=True)
#             participants = incident_data.get('participants', [])
#             st.markdown(f"""
#             <div class="white-content">
#                 {', '.join(participants) if participants else 'N/A'}
#             </div>
#             """, unsafe_allow_html=True)
        
#         with main_col2:
            
#             st.markdown('<div class="blue-header">📢 MIM Communication Status</div>', unsafe_allow_html=True)
            
#             communications_df = pd.DataFrame([
#                 ['Open Comms (Hyper Link)', '1', '7:00 AM', 'Published'],
#                 ['Update 1 (Hyper Link)', '3', 'TBD', 'Not Published'],
#                 ['Update 2 (Hyper Link)', '2', '7:30 AM', 'Published'],
#                 ['Update 3 (Hyper Link)', '4', 'TBD', 'Not Published']
#             ], columns=['Communications', 'Order', 'Time', 'Status'])
            
#             st.table(communications_df.assign(hack='').set_index('hack'))
            
#             # Bridge Details
#             bridge_info = incident_data.get('bridge_details')
#             if bridge_info:
#                 st.markdown('<div class="blue-header">🌐 Bridge Details</div>', unsafe_allow_html=True)
#                 st.markdown(f"""
#                 <div class="white-content">
#                     <strong>Business Bridge:</strong><br>
#                     Platform: {bridge_info.get('platform', 'N/A')}<br>
#                     Meeting ID: {bridge_info.get('meeting_id', 'N/A')}<br>
#                     Passcode: {bridge_info.get('passcode', 'N/A')}
#                 </div>
#                 """, unsafe_allow_html=True)

#             st.markdown('<div class="blue-header">🔗 Key Process Links</div>', unsafe_allow_html=True)
            
#             process_links = [
#                 "Announcement Portal Link",
#                 "GCC Calendar Link",
#                 "Executive Communication Process",
#                 "MIM Process Document",
#                 "Easy Learn Session Training",
#                 "Change Management Process",
#                 "Problem Management Process",
#                 "P1s Do/Don't's"
#             ]
            
#             links_html = "<div class='white-content'>"
#             for link in process_links:
#                 links_html += f"""
#                 <div style="padding: 8px 0;">
#                     <a href="#" style="color: #0066cc; text-decoration: none; display: block;">
#                         {link}
#                     </a>
#                 </div>"""
#             links_html += "</div>"
            
#             st.markdown(links_html, unsafe_allow_html=True)
           

#     else:
#         st.info("Please upload an incident document using the panel on the left")


# # def main():
# #     st.set_page_config(page_title="Executive Dashboard", page_icon="🎯", layout="wide", initial_sidebar_state="expanded")
    
# #     # Initialize session state
# #     initialize_session_state()
# #     initialize_exec_timer()
# #     if 'settings' not in st.session_state:
# #         st.session_state.settings = Settings()
    
# #     # Sidebar styling
# #     st.markdown("""
# #         <style>
# #         .css-1d391kg {
# #             background-color: #40E0D0;
# #         }
# #         .sidebar .sidebar-content {
# #             background-color: #40E0D0;
# #         }
# #         </style>
# #     """, unsafe_allow_html=True)
    
# #     st.markdown(CSS_STYLES, unsafe_allow_html=True)
    
# #     # Sidebar navigation
# #     st.sidebar.markdown("---")
# #     st.sidebar.title("🎯 Navigation")

# # #     show_pages(
# # #     [
# # #         Page("app.py", "Executive Dashboard", "🏠"),
# # #         Page("views/incident_details.py", "Incident Details", "📝"),
# # #         Page("views/incident_summary.py", "Incident Summary", "📊"),
# # #         Page("views/similar_historical_incidents.py", "Similar Incidents", "🔍"),
# # #     ]
# # # )

# #     # page = st.sidebar.radio("Go to", [
# #     #     "Executive Dashboard",
# #     #     "Incident Details", 
# #     #     "Incident Summary", 
# #     #     "Similar Historical Incidents"
# #     # ])


# #     # pages = {
# #     #     "Executive Dashboard": show_executive_dashboard,
# #     #     "Incident Details": incident_details.show,
# #     #     "Incident Summary": incident_summary.show,
# #     #     "Similar Historical Incidents": similar_historical_incidents.show
# #     # }
    
# #     # st.navigation(pages)
    
# #     # if pages == "Executive Dashboard":
# #     #     show_executive_dashboard()
# #     # elif pages == "Incident Details":
# #     #     st.markdown('<div class="title-box"><h1>🔍 INCIDENT DETAILS</h1></div>', unsafe_allow_html=True)
# #     #     if 'detailed_issue_info' in st.session_state:
# #     #         incident_details.show()
# #     #     else:
# #     #         st.info("Please upload a document in the Executive Dashboard first")
# #     # elif pages == "Incident Summary":
# #     #     st.markdown('<div class="title-box"><h1>📊 INCIDENT SUMMARY</h1></div>', unsafe_allow_html=True)
# #     #     if 'detailed_issue_info' in st.session_state:
# #     #         incident_summary.show()
# #     #     else:
# #     #         st.info("Please upload a document in the Executive Dashboard first")
# #     # else:
# #     #     similar_historical_incidents.show()


# #      # Sidebar navigation
# #     page = st_navbar(
# #         ["Executive Dashboard", 
# #          "Incident Details", 
# #          "Incident Summary", 
# #          "Similar Historical Incidents"]
# #     )

# #     # Routing logic
# #     if page == "Executive Dashboard":
# #         show_executive_dashboard()
# #     elif page == "Incident Details":
# #         st.markdown('<div class="title-box"><h1>🔍 INCIDENT DETAILS</h1></div>', unsafe_allow_html=True)
# #         if 'detailed_issue_info' in st.session_state:
# #             incident_details.show()
# #         else:
# #             st.info("Please upload a document in the Executive Dashboard first")
# #     elif page == "Incident Summary":
# #         st.markdown('<div class="title-box"><h1>📊 INCIDENT SUMMARY</h1></div>', unsafe_allow_html=True)
# #         if 'detailed_issue_info' in st.session_state:
# #             incident_summary.show()
# #         else:
# #             st.info("Please upload a document in the Executive Dashboard first")
# #     elif page == "Similar Historical Incidents":
# #         similar_historical_incidents.show()





#     # show_pages([
#     #     Page("app.py", "Executive Dashboard", "🏠"),
#     #     Page("views/incident_details.py", "Incident Details", "📝"),
#     #     Page("views/incident_summary.py", "Incident Summary", "📊"),
#     #     Page("views/similar_historical_incidents.py", "Similar Incidents", "🔍"),
#     # ])

#     # # Routing based on the current page
#     # current_page = st.experimental_get_query_params().get("page", ["app"])[0]

#     # if current_page == "app":
#     #     show_executive_dashboard()
#     # elif current_page == "incident_details":
#     #     st.markdown('<div class="title-box"><h1>🔍 INCIDENT DETAILS</h1></div>', unsafe_allow_html=True)
#     #     if 'detailed_issue_info' in st.session_state:
#     #         incident_details.show()
#     #     else:
#     #         st.info("Please upload a document in the Executive Dashboard first")
#     # elif current_page == "incident_summary":
#     #     st.markdown('<div class="title-box"><h1>📊 INCIDENT SUMMARY</h1></div>', unsafe_allow_html=True)
#     #     if 'detailed_issue_info' in st.session_state:
#     #         incident_summary.show()
#     #     else:
#     #         st.info("Please upload a document in the Executive Dashboard first")
#     # elif current_page == "similar_historical_incidents":
#     #     similar_historical_incidents.show() 

# #     # Sidebar Navigation
# # sections = st.sidebar.toggle("Sections", value=True, key="use_sections")
# # nav = get_nav_from_toml(
# #     ".streamlit/pages_sections.toml" if sections else ".streamlit/pages.toml"
# # )

# # #st.logo("logo.png")  # Replace with the actual path to your logo file

# # pg = st.navigation(nav)

# # # Add title and run selected page
# # add_page_title(pg)
# # pg.run()
# def main():
#     st.set_page_config(page_title="Executive Dashboard", page_icon="🎯", layout="wide", initial_sidebar_state="expanded")
    
#     # Initialize session state
#     initialize_session_state()
#     initialize_exec_timer()
#     if 'settings' not in st.session_state:
#         st.session_state.settings = Settings()
    
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

#     # Create navigation tabs
#     tab_names = ["Executive Dashboard", "Incident Details", "Incident Summary", "Similar Historical Incidents"]
#     tabs = st.tabs(tab_names)

#     # Routing logic
#     with tabs[0]:
#         show_executive_dashboard()
#     with tabs[1]:
#         if 'detailed_issue_info' in st.session_state:
#             st.markdown('<div class="title-box"><h1>🔍 INCIDENT DETAILS</h1></div>', unsafe_allow_html=True)
#             incident_details.show()
#         else:
#             st.info("Please upload a document in the Executive Dashboard first")
#     with tabs[2]:
#         if 'detailed_issue_info' in st.session_state:
#             st.markdown('<div class="title-box"><h1>📊 INCIDENT SUMMARY</h1></div>', unsafe_allow_html=True)
#             incident_summary.show()
#         else:
#             st.info("Please upload a document in the Executive Dashboard first")
#     with tabs[3]:
#         similar_historical_incidents.show()

# if __name__ == "__main__":
#     main()







#EMAIL INTEGRATION







import streamlit as st
from views import incident_details, incident_summary, similar_historical_incidents
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

from services.email_processor import EmailProcessor

#from st_pages import Page, show_pages, add_page_title
from st_pages import add_page_title, get_nav_from_toml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

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

    
    with st.sidebar:
        st.markdown("### 📂 Document Upload")
        uploaded_file = st.file_uploader("Upload Incident Document", type=['docx'], key="main_uploader")
        
        
        if uploaded_file:
            try:
                # Start timer when file is uploaded
                start_exec_timer()

              
                    
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
    st.markdown('<div class="title-box"><h1>🎯 EXECUTIVE DASHBOARD - MAJOR INCIDENT MANAGEMENT</h1></div>', unsafe_allow_html=True)
    

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
        
        st.markdown(f"""
        <div class="incident-header">
            <div style="display: flex; align-items: center; gap: 10px;">
                <h2>{header_text}</h2>
                <div style="display: flex; align-items: center; gap: 10px;">
                    {f'<span style="background-color: #ff4444; color: white; padding: 5px 12px; border-radius: 15px; font-weight: bold; font-size: 0.9em;">{priority}</span>' if priority else ''}
                     <div class="duration-box" id="incident-duration">00:00:00</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        
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
            
            # Get and format description with bullet points
            system_info = "The ERP Central Application is inaccessible to multiple users in Bengaluru and Mumbai offices."
            root_cause = "The database was in an incorrect state due to manual termination of an earlier backup."
            timing = "The incident started at 9:53 PM UTC."
            impact = "Multiple users are prevented from logging into the application, affecting operations across both locations."
            
            formatted_description = f"""
                <div class="white-content">
                    <strong>{header_text}</strong><br><br>
                    • {system_info}<br><br>
                    • {root_cause}<br><br>
                    • {timing}<br><br>
                    • {impact}<br><br>
                    <strong>Work Around:</strong> {incident_data.get('issue_description', {}).get('workaround', '').capitalize()}
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

def main():
    st.set_page_config(page_title="Executive Dashboard", page_icon="🎯", layout="wide", initial_sidebar_state="expanded")

      
    # Initialize session state
    initialize_session_state()
    initialize_exec_timer()
    
    if 'settings' not in st.session_state:
        st.session_state.settings = Settings()
    
    # New: Initialize Email Processor
    if 'email_processor' not in st.session_state:
        st.session_state.email_processor = EmailProcessor(
            username=st.session_state.settings.EMAIL_USERNAME,
            password=st.session_state.settings.EMAIL_PASSWORD
        )
    
    # Check for emails and process them periodically
    if st.button("Check for Incident Emails"):
        new_incidents = st.session_state.email_processor.process_emails()
        if new_incidents:
            for incident in new_incidents:
                st.success(f"New Incident Detected: {incident.get('incident_id', 'Unknown')}")
                st.session_state.detailed_issue_info = incident
    
    # Initialize session state
    initialize_session_state()
    initialize_exec_timer()
    if 'settings' not in st.session_state:
        st.session_state.settings = Settings()
    
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
    tab_names = ["Executive Dashboard", "Incident Details", "Incident Summary", "Similar Historical Incidents"]
    tabs = st.tabs(tab_names)

    # Routing logic
    with tabs[0]:
        show_executive_dashboard()
    with tabs[1]:
        if 'detailed_issue_info' in st.session_state:
            st.markdown('<div class="title-box"><h1>🔍 INCIDENT DETAILS</h1></div>', unsafe_allow_html=True)
            incident_details.show()
        else:
            st.info("Please upload a document in the Executive Dashboard first")
    with tabs[2]:
        if 'detailed_issue_info' in st.session_state:
            st.markdown('<div class="title-box"><h1>📊 INCIDENT SUMMARY</h1></div>', unsafe_allow_html=True)
            incident_summary.show()
        else:
            st.info("Please upload a document in the Executive Dashboard first")
    with tabs[3]:
        similar_historical_incidents.show()

if __name__ == "__main__":
    main()



























































































