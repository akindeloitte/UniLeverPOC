# import imaplib
# import email
# from email.header import decode_header
# from groq import Groq
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import logging

# class EmailProcessor:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.groq_client = Groq(api_key="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")  # Replace with actual key
        
#         # Team database mapping
#         self.team_database = {
#             "IT Team": ["arkapoor.ext@deloitte.com"],
#             "Firewall": ["arkapoor.ext@deloitte.com"],
#             "Logistics": ["arkapoor.ext@deloitte.com"],
#             "Miscellaneous": ["arkapoor.ext@deloitte.com"]
#         }

#     def authenticate_gmail(self):
#         """Authenticate with Gmail IMAP."""
#         try:
#             imap = imaplib.IMAP4_SSL("imap.gmail.com")
#             imap.login(self.username, self.password)
#             return imap
#         except Exception as e:
#             logging.error(f"Gmail authentication failed: {e}")
#             return None

#     def read_emails(self, imap, n=5):
#         """Read the latest n emails from the Gmail inbox."""
#         imap.select("inbox")
#         status, messages = imap.search(None, "UNSEEN")  # Only process unread emails
#         email_ids = messages[0].split()

#         latest_emails = []
#         for i in email_ids[-n:]:
#             res, msg = imap.fetch(i, "(RFC822)")
#             for response in msg:
#                 if isinstance(response, tuple):
#                     msg = email.message_from_bytes(response[1])
#                     subject = self._decode_header(msg["Subject"])
#                     body = self._get_email_body(msg)
                    
#                     latest_emails.append({
#                         'subject': subject,
#                         'body': body
#                     })

                    
#         return latest_emails

#     def _decode_header(self, header):
#         """Decode email headers."""
#         subject, encoding = decode_header(header)[0]
#         return subject.decode(encoding or "utf-8") if isinstance(subject, bytes) else subject

#     def _get_email_body(self, msg):
#         """Extract email body from multipart message."""
#         body = ""
#         if msg.is_multipart():
#             for part in msg.walk():
#                 if part.get_content_type() == "text/plain":
#                     body = part.get_payload(decode=True).decode()
#                     break
#         else:
#             body = msg.get_payload(decode=True).decode()
#         return body

#     def classify_incident(self, mail_content):
#         """Use Groq to classify incident and recommend teams."""
#         # prompt = f"""Analyze this incident email and recommend which team(s) should handle it:
#         # {mail_content}

#         # Recommend from: IT Team, Firewall, Logistics, Miscellaneous
#         # """

#         prompt = f"""Analyze the following incident mail and classify it into one or more of these categories:
#     1. IT Team: For technical issues related to software, hardware, networks, and general IT infrastructure.
#     2. Firewall: Specifically for issues related to firewall configuration, security, and network access control.
#     3. Logistics: For issues related to inventory management, supply chain, and physical asset tracking systems.
#     4. Miscellaneous: For general inquiries, HR-related tasks, and any issues not clearly falling into the above categories.

#     Provide **only** the team names that should handle the incident, choosing from the four options above.
#     Respond with one or more team names, separated by commas if necessary, and nothing else.

#     Incident Mail:
#     {mail_content}

#     Based on this information, which teams should be assigned to handle this incident? Respond with only the team names, without any explanation, and separate multiple team names by commas if needed.
#     """

#         response = self.groq_client.chat.completions.create(
#             messages=[{"role": "user", "content": prompt}],
#             model="llama3-70b-8192",
#             max_tokens=300,
#             temperature=0.2
#         )

#         return response.choices[0].message.content.strip()

#     def generate_incident_details(self, mail_content):
#         """Generate structured incident details from email."""
#         prompt = """Extract the following structured information from the incident email:
#         - Incident ID
#         - Short Description
#         - Priority Level
#         - Impacted Services
#         - Affected Location
#         - Participants
#         """

#         response = self.groq_client.chat.completions.create(
#             messages=[
#                 {"role": "system", "content": prompt},
#                 {"role": "user", "content": mail_content}
#             ],
#             model="llama3-70b-8192",
#             max_tokens=300
#         )

#         # Parse and return structured incident details
#         return self._parse_incident_details(response.choices[0].message.content)
    

#     def _parse_incident_details(self, details_text):
#         """Parse incident details text into a dictionary."""
#         details = {}
#         # Implement parsing logic for the text
#         return details

#     def process_emails(self):
#         """Main method to process emails and return incident details."""
#         imap = self.authenticate_gmail()
#         if not imap:
#             return []

#         emails = self.read_emails(imap)
#         processed_incidents = []

#         for email_data in emails:
#             # Classify incident and generate details
#             assigned_teams = self.classify_incident(email_data['body'])
#             incident_details = self.generate_incident_details(email_data['body'])

#             # Send notifications
#             self._send_team_notifications(assigned_teams, email_data)

#             processed_incidents.append(incident_details)

#         imap.logout()
#         return processed_incidents

#     def _send_team_notifications(self, teams, email_data):
#         """Send email notifications to relevant teams."""
#         # Implementation of email notification logic
#         pass

# # Additional helper methods can be added as needed





# # import streamlit as st
# # import imaplib
# # import email
# # from email.header import decode_header
# # from groq import Groq
# # import logging
# # from typing import List, Dict

# # class EmailProcessor:
# #     def __init__(self, username, password, groq_api_key=None):
# #         self.username = username
# #         self.password = password
        
# #         # Use environment variable or passed key, with fallback to session state
# #         self.groq_api_key = (
# #             groq_api_key or 
# #             st.secrets.get('GROQ_API_KEY') or 
# #             getattr(st.session_state, 'GROQ_API_KEY', None)
# #         )
        
# #         # Validate API key
# #         if not self.groq_api_key:
# #             st.error("No Groq API Key found. Please set it in Streamlit secrets or session state.")
# #             self.groq_client = None
# #         else:
# #             try:
# #                 self.groq_client = Groq(api_key=self.groq_api_key)
# #             except Exception as e:
# #                 st.error(f"Failed to initialize Groq client: {e}")
# #                 self.groq_client = None

# #     def classify_incident(self, mail_content):
# #         """Safely classify incident with error handling"""
# #         if not self.groq_client:
# #             st.warning("Groq client not initialized. Skipping classification.")
# #             return "Miscellaneous"

# #         try:
# #             prompt = f"""Analyze this incident email and recommend which team(s) should handle it:
# #             {mail_content}

# #             Recommend from: IT Team, Firewall, Logistics, Miscellaneous
# #             """

# #             response = self.groq_client.chat.completions.create(
# #                 messages=[{"role": "user", "content": prompt}],
# #                 model="llama3-70b-8192",
# #                 max_tokens=50
# #             )

# #             return response.choices[0].message.content.strip()
        
# #         except Exception as e:
# #             st.error(f"Error in incident classification: {e}")
# #             return "Miscellaneous"

# #     def process_emails(self) -> List[Dict]:
# #         """
# #         Process emails with comprehensive error handling
# #         Returns list of processed incident details
# #         """
# #         try:
# #             imap = self.authenticate_gmail()
# #             if not imap:
# #                 st.error("Could not authenticate with Gmail")
# #                 return []

# #             emails = self.read_emails(imap)
# #             processed_incidents = []

# #             for email_data in emails:
# #                 try:
# #                     # Classify incident
# #                     assigned_teams = self.classify_incident(email_data['body'])
                    
# #                     # Generate incident details (with error handling)
# #                     incident_details = self.generate_incident_details(email_data['body'])
                    
# #                     # Add classification to incident details
# #                     incident_details['assigned_teams'] = assigned_teams
                    
# #                     processed_incidents.append(incident_details)
                
# #                 except Exception as email_process_error:
# #                     st.error(f"Error processing individual email: {email_process_error}")

# #             imap.logout()
# #             return processed_incidents

# #         except Exception as overall_error:
# #             st.error(f"Unexpected error in email processing: {overall_error}")
# #             return []

# #     def generate_incident_details(self, mail_content):
# #         """Generate structured incident details from email"""
# #         if not self.groq_client:
# #             return {
# #                 'incident_id': 'AUTO_' + str(hash(mail_content))[:8],
# #                 'short_description': 'Email Incident (Details Unavailable)',
# #                 'priority_level': 'Unknown'
# #             }

# #         try:
# #             prompt = """Extract the following structured information from the incident email:
# #             - Incident ID (generate if not present)
# #             - Short Description
# #             - Priority Level (High/Medium/Low)
# #             - Impacted Services
# #             - Affected Location
# #             - Key Details
# #             """

# #             response = self.groq_client.chat.completions.create(
# #                 messages=[
# #                     {"role": "system", "content": prompt},
# #                     {"role": "user", "content": mail_content}
# #                 ],
# #                 model="llama3-70b-8192",
# #                 max_tokens=300
# #             )

# #             # Parse response
# #             details_text = response.choices[0].message.content
            
# #             # Basic parsing (you might want to improve this)
# #             return {
# #                 'incident_id': self._extract_detail(details_text, 'Incident ID') or 'AUTO_' + str(hash(mail_content))[:8],
# #                 'short_description': self._extract_detail(details_text, 'Short Description') or 'Unspecified Incident',
# #                 'priority_level': self._extract_detail(details_text, 'Priority Level') or 'Medium',
# #                 'impacted_services': self._extract_detail(details_text, 'Impacted Services', is_list=True) or [],
# #                 'affected_location': self._extract_detail(details_text, 'Affected Location') or 'Unknown',
# #             }

# #         except Exception as e:
# #             st.error(f"Error generating incident details: {e}")
# #             return {
# #                 'incident_id': 'AUTO_' + str(hash(mail_content))[:8],
# #                 'short_description': 'Email Incident (Details Extraction Failed)',
# #                 'priority_level': 'Unknown'
# #             }

# #     def _extract_detail(self, text, key, is_list=False):
# #         """
# #         Simple utility to extract details from text
# #         Can be expanded for more robust parsing
# #         """
# #         import re
        
# #         pattern = rf"{key}:\s*(.+?)(?=\n[A-Za-z]+:|$)"
# #         matches = re.findall(pattern, text, re.DOTALL | re.IGNORECASE)
        
# #         if matches:
# #             if is_list:
# #                 # Split by comma or newline for lists
# #                 return [item.strip() for item in re.split(r'[,\n]', matches[0]) if item.strip()]
# #             return matches[0].strip()
        
# #         return None

# #     # Rest of the methods remain the same as in previous implementation











import imaplib
import email
from email.header import decode_header
from groq import Groq
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

class EmailProcessor:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.groq_client = Groq(api_key="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")  # Replace with actual key
        
        # Enhanced team database mapping with multiple team members
        self.team_database = {
            "IT Team": ["shnalawade@deloitte.com", "arkapoor.ext@deloitte.com"],
            "Firewall": ["shnalawade@deloitte.com", "arkapoor.ext@deloitte.com"],
            "Logistics": ["shnalawade@deloitte.com", "arkapoor.ext@deloitte.com"],
            "Miscellaneous": ["arkapoor.ext@deloitte.com", "shnalawade@deloitte.com"]
        }

    def authenticate_gmail(self):
        """Authenticate with Gmail IMAP."""
        try:
            imap = imaplib.IMAP4_SSL("imap.gmail.com")
            imap.login(self.username, self.password)
            return imap
        except Exception as e:
            logging.error(f"Gmail authentication failed: {e}")
            return None

    def read_emails(self, imap, n=5):
        """Read the latest n emails from the Gmail inbox."""
        imap.select("inbox")
        status, messages = imap.search(None, "UNSEEN")  # Only process unread emails
        email_ids = messages[0].split()

        latest_emails = []
        for i in email_ids[-n:]:
            res, msg = imap.fetch(i, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    subject = self._decode_header(msg["Subject"])
                    body = self._get_email_body(msg)
                    from_ = msg.get("From")
                    
                    latest_emails.append({
                        'subject': subject,
                        'body': body,
                        'from': from_
                    })
                    
        return latest_emails

    def _decode_header(self, header):
        """Decode email headers."""
        subject, encoding = decode_header(header)[0]
        return subject.decode(encoding or "utf-8") if isinstance(subject, bytes) else subject

    def _get_email_body(self, msg):
        """Extract email body from multipart message."""
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    break
        else:
            body = msg.get_payload(decode=True).decode()
        return body

    def classify_incident(self, mail_content):
        """Use Groq to classify incident and recommend teams."""
        prompt = f"""Analyze the following incident mail and classify it into one or more of these categories:
    1. IT Team: For technical issues related to software, hardware, networks, and general IT infrastructure.
    2. Firewall: Specifically for issues related to firewall configuration, security, and network access control.
    3. Logistics: For issues related to inventory management, supply chain, and physical asset tracking systems.
    4. Miscellaneous: For general inquiries, HR-related tasks, and any issues not clearly falling into the above categories.

    Provide **only** the team names that should handle the incident, choosing from the four options above.
    Respond with one or more team names, separated by commas if necessary, and nothing else.

    Incident Mail:
    {mail_content}

    Based on this information, which teams should be assigned to handle this incident? Respond with only the team names, without any explanation, and separate multiple team names by commas if needed.
    """

        response = self.groq_client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-70b-8192",
            max_tokens=300,
            temperature=0.2
        )

        # Validate the response, splitting if multiple teams are provided
        valid_teams = ["IT Team", "Firewall", "Logistics", "Miscellaneous"]
        assigned_teams = [team.strip() for team in response.choices[0].message.content.strip().split(",") if team.strip() in valid_teams]

        if not assigned_teams:
            assigned_teams = ["Miscellaneous"]

        return assigned_teams

    def generate_incident_details(self, mail_content):
        """Generate structured incident details from email."""
        prompt = """Extract the following structured information from the incident email:
        - Incident ID
        - Short Description
        - Priority Level
        - Impacted Services
        - Affected Location
        - Participants
        """

        response = self.groq_client.chat.completions.create(
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": mail_content}
            ],
            model="llama3-70b-8192",
            max_tokens=300
        )

        # Parse and return structured incident details
        return self._parse_incident_details(response.choices[0].message.content)
    
    def _parse_incident_details(self, details_text):
        """Parse incident details text into a dictionary."""
        details = {}
        # Implement basic parsing logic for the text
        # This is a placeholder and can be enhanced
        details['incident_id'] = 'AUTO_' + str(hash(details_text))[:8]
        details['short_description'] = 'Incident details extracted'
        return details

    def _send_team_notifications(self, teams, email_data):
        """Send email notifications to relevant teams."""
        sender_email = "arkapoordeloitte@gmail.com"
        sender_password = "goxl vfwn ilrm aypw" 
        
        # Collect all receiver emails from multiple teams
        receiver_emails = []
        for team in teams:
            receiver_emails.extend(self.team_database[team])
        
        # Create email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = ", ".join(receiver_emails)
        message["Subject"] = f"New Incident Assigned to {', '.join(teams)}"

        body = f"""A new incident has been assigned to the following teams: {', '.join(teams)}

Subject: {email_data.get('subject', 'No Subject')}
From: {email_data.get('from', 'Unknown Sender')}

Incident Content:
{email_data.get('body', 'No content available')}

Please handle this incident as soon as possible.

Meeting ID: 316 793 798 594 
Passcode: h4o7kG
"""
        message.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(message)
            logging.info("Email notification sent successfully!")
        except Exception as e:
            logging.error(f"Failed to send email notification: {str(e)}")

    def process_emails(self):
        """Main method to process emails and return incident details."""
        imap = self.authenticate_gmail()
        if not imap:
            return []

        emails = self.read_emails(imap)
        processed_incidents = []

        for email_data in emails:
            # Classify incident and generate details
            assigned_teams = self.classify_incident(email_data['body'])
            incident_details = self.generate_incident_details(email_data['body'])

            # Send notifications
            self._send_team_notifications(assigned_teams, email_data)

            # Add team assignment to incident details
            incident_details['assigned_teams'] = assigned_teams
            processed_incidents.append(incident_details)

        imap.logout()
        return processed_incidents

# Example usage
if __name__ == '__main__':
    # Replace with actual credentials
    processor = EmailProcessor('arkapoordeloitte@gmail.com', 'goxl vfwn ilrm aypw')
    incidents = processor.process_emails()
    print(incidents)