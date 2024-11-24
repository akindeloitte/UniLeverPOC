# import streamlit as st
# from services.incident_manager import IncidentManager
# from services.detail_extractor import IncidentDetailExtractor

# def show_document_upload():
#     """Shared document upload component that maintains state across pages"""
#     uploaded_file = st.file_uploader("📤 Upload Incident Document", type=['docx'], key="doc_uploader")
    
#     if uploaded_file and 'previous_file' not in st.session_state:
#         st.session_state.previous_file = uploaded_file.name
#         process_uploaded_document(uploaded_file)
#     elif uploaded_file and st.session_state.get('previous_file') != uploaded_file.name:
#         st.session_state.previous_file = uploaded_file.name
#         process_uploaded_document(uploaded_file)
        
#     return uploaded_file is not None

import streamlit as st
from services.incident_manager import IncidentManager
from services.detail_extractor import IncidentDetailExtractor
import logging

def process_uploaded_document(uploaded_file):
    """Process the uploaded document and store results in session state"""
    try:
        # Process with IncidentManager
        incident_manager = IncidentManager()
        document_text = incident_manager.read_docx(uploaded_file)
        
        # Store transcript for other views
        st.session_state.transcript = document_text
        
        # Process with DetailExtractor
        if 'settings' in st.session_state:
            detailed_extractor = IncidentDetailExtractor(st.session_state.settings.OPENAI_API_KEY)
            detailed_info = detailed_extractor.extract_detailed_issue_info(document_text)
            
            if detailed_info:
                st.session_state.detailed_issue_info = detailed_info
            else:
                st.error("Could not extract incident details from the document")
                return False
                
        return True
    except Exception as e:
        st.error(f"Error processing document: {str(e)}")
        logging.error(f"Document processing error: {str(e)}")
        return False

def show_document_upload():
    """Shared document upload component that maintains state across pages"""
    uploaded_file = st.file_uploader("📤 Upload Incident Document", type=['docx'], key="doc_uploader")
    
    if uploaded_file and 'previous_file' not in st.session_state:
        st.session_state.previous_file = uploaded_file.name
        process_uploaded_document(uploaded_file)
    elif uploaded_file and st.session_state.get('previous_file') != uploaded_file.name:
        st.session_state.previous_file = uploaded_file.name
        process_uploaded_document(uploaded_file)
        
    return uploaded_file is not None