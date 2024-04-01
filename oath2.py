import streamlit as st
import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

# Your client credentials
client_id = 'client_id'
client_secret = 'client_secret'

# Create a session
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)

# Get token
token = oauth.fetch_token(token_url='https://your-jira-server.atlassian.net/oauth/token', client_id=client_id, client_secret=client_secret)

# Use the token
jira_server = 'jira_server'
response = oauth.get(f'https://{jira_server}/rest/api/2/search?jql=project=PROJECT_KEY')

# Get the JSON response body
issues = response.json()

# Print each issue key and summary
for issue in issues['issues']:
    print(f"{issue['key']}: {issue['fields']['summary']}")
