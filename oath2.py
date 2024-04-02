import streamlit as st
import requests, webbrowser
from streamlit_oauth import OAuth2Component

""" # Your client credentials
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
 """

url = 'https://auth.atlassian.com/authorize?audience=api.atlassian.com&client_id=ncXG3wFdYgzhibpX64G7nM9xhh9DxSMS&scope=read%3Ajira-work&redirect_uri=https%3A%2F%2Fjira-issue-tracker-mcuw6k6su7gzqyn5hnyex3.streamlit.app%2F&state=${YOUR_USER_BOUND_VALUE}&response_type=code&prompt=consent'
webbrowser.open_new(url)
headers = {'Content-Type': 'application/json'}
response = requests.get(url, headers=headers)
print(response.json())

""" # Define the URL and the headers
url = 'https://auth.atlassian.com/oauth/token'
headers = {'Content-Type': 'application/json'}

# Define the data
data = {
    "grant_type": "authorization_code",
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET",
    "code": "YOUR_AUTHORIZATION_CODE",
    "redirect_uri": "https://YOUR_APP_CALLBACK_URL"
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Print the response
print(response.json()) """