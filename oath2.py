import streamlit as st
import requests, webbrowser, os
from dotenv import load_dotenv
from streamlit_oauth import OAuth2Component

# For local testing
#load_dotenv()  # take environment variables from .env.

AUTHORIZATION_URL = "https://auth.atlassian.com/authorize"
TOKEN_URL = "https://auth.atlassian.com/oauth/token"
REVOKE_URL = ""
CLIENT_ID = st.secrets["CLIENT_ID"]
CLIENT_SECRET = st.secrets["SECRET"]
REDIRECT_URI = "https://jira-issue-tracker-ejvrmzicbw58u2aqsnckn8.streamlit.app/"
# For local testing
#CLIENT_ID = os.getenv("CLIENT_ID")
#CLIENT_SECRET = os.getenv("SECRET")
#REDIRECT_URI = "http://localhost:8502"
SCOPE = "read:jira-work"

oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZATION_URL, TOKEN_URL, TOKEN_URL, REVOKE_URL)

# Check if token exists in session state
if 'token' not in st.session_state:
  result = oauth2.authorize_button("Continue with Atlassian", REDIRECT_URI, SCOPE)
  if result:
    st.session_state.token = result.get('token')
    st.rerun()

# For local testing
#print(st.session_state)

# # Your client credentials
# client_id = 'client_id'
# client_secret = 'client_secret'

# # Create a session
# client = BackendApplicationClient(client_id=client_id)
# oauth = OAuth2Session(client=client)

# # Get token
# token = oauth.fetch_token(token_url='https://your-jira-server.atlassian.net/oauth/token', client_id=client_id, client_secret=client_secret)

# # Use the token
# jira_server = 'jira_server'
# response = oauth.get(f'https://{jira_server}/rest/api/2/search?jql=project=PROJECT_KEY')

# # Get the JSON response body
# issues = response.json()

# # Print each issue key and summary
# for issue in issues['issues']:
#     print(f"{issue['key']}: {issue['fields']['summary']}")
 
# """
# [Login](https://auth.atlassian.com/authorize?audience=api.atlassian.com&client_id=ncXG3wFdYgzhibpX64G7nM9xhh9DxSMS&scope=read%3Ajira-work&redirect_uri=http%3A%2F%2Flocalhost%3A8502%2F&state=${YOUR_USER_BOUND_VALUE}&response_type=code&prompt=consent)
# url = 'https://auth.atlassian.com/authorize?audience=api.atlassian.com&client_id=ncXG3wFdYgzhibpX64G7nM9xhh9DxSMS&scope=read%3Ajira-work&redirect_uri=https%3A%2F%2Fjira-issue-tracker-mcuw6k6su7gzqyn5hnyex3.streamlit.app%2F&state=${YOUR_USER_BOUND_VALUE}&response_type=code&prompt=consent'
# webbrowser.open_new(url)
# headers = {'Content-Type': 'application/json'}
# response = requests.get(url, headers=headers)
# print(response.json())
# """
# Define the URL and the headers
# url = 'https://auth.atlassian.com/oauth/token'
# headers = {'Content-Type': 'application/json'}

# # Define the data
# data = {
#     "grant_type": "authorization_code",
#     "client_id": "YOUR_CLIENT_ID",
#     "client_secret": "YOUR_CLIENT_SECRET",
#     "code": "YOUR_AUTHORIZATION_CODE",
#     "redirect_uri": "https://YOUR_APP_CALLBACK_URL"
# }

# # Make the POST request
# response = requests.post(url, headers=headers, data=json.dumps(data))

# # Print the response
# print(response.json())