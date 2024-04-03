import streamlit as st
import requests, os
# For local testing
#from dotenv import load_dotenv
from atlassian import Jira

# For local testing
#load_dotenv()  # take environment variables from .env.
jira = Jira(
    url='https://biosustain-dev.atlassian.net',
    # For local testing
    #username=os.getenv("USER_NAME"),
    #password=os.getenv("API_TOKEN"),
    username=st.secrets("USER_NAME"),
    password=st.secrets("API_TOKEN"),
    cloud=True)

issue_count = 0
while True:
    DCCP_issues = jira.get_all_project_issues('DCCP', start=issue_count)
    if len(DCCP_issues) % 50 > 0:
        for issue in DCCP_issues:
            issue_key = issue['key']
            summary = issue['fields']['summary']
            status = issue['fields']['status']['name']
            try:
                assignee = issue['fields']['assignee']['displayName']
            except:
                assignee = issue['fields']['assignee']
            
            st.write(f"Issue Key: {issue_key}, Summary: {summary}, Assignee: {assignee}, Status: {status}")
        break
    else:
        for issue in DCCP_issues:
            issue_key = issue['key']
            summary = issue['fields']['summary']
            status = issue['fields']['status']['name']
            try:
                assignee = issue['fields']['assignee']['displayName']
            except:
                assignee = issue['fields']['assignee']
            
            st.write(f"Issue Key: {issue_key}, Summary: {summary}, Assignee: {assignee}, Status: {status}")

    issue_count += 50

# CLIENT_ID = os.getenv("CLIENT_ID")
# CLIENT_SECRET = os.getenv("SECRET")
# REDIRECT_URI = "http://localhost:8502"
# AUTHORIZATION_URL = "https://auth.atlassian.com/authorize"
# TOKEN_URL = "https://auth.atlassian.com/oauth/token"
# REVOKE_URL = ""
# SCOPE = "read:jira-work"

# oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZATION_URL, TOKEN_URL, TOKEN_URL, REVOKE_URL)

# # Check if token exists in session state
# if 'token' not in st.session_state:
#   result = oauth2.authorize_button("Continue with Atlassian", REDIRECT_URI, SCOPE)
#   if result:
#     st.session_state.token = result.get('token')
#     st.rerun()
# else:
#     # If token exists in session state, show the token
#     access_token = st.session_state['token']['access_token']

# # Use the token to get cloudid
# headers = {'Authorization': f'Bearer {access_token}', 'Accept': 'application/json'}
# jira_api_server = 'https://api.atlassian.com/oauth/token/accessible-resources'
# response = requests.get(jira_api_server, headers=headers)
# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()
#     cloudid = data[0]['id']
#     st.write(data)
# else:
#     st.write(f"Error: {response.status_code} - {response.text}")



# # Make api request
# jira_app_api = f'https://api.atlassian.com/ex/jira/{cloudid}/rest/api/3/search'
# query = {
#   'jql': 'project = DCCP',
#   # does not seeem to work
#   'maxResults': -1
# }

# try:
#     response = requests.get(jira_app_api, headers=headers, params=query)
#     if response.status_code == 200:
#         data = response.json()
#         for issue in data.get("issues", []):
#             issue_key = issue['key']
#             summary = issue['fields']['summary']
#             try: 
#                 assignee = issue['fields']['assignee']['displayName']
#             except:
#                 assignee = issue['fields']['assignee']
#             status = issue['fields']['status']['name']
#             st.write(f"Issue Key: {issue_key}, Summary: {summary}, Assignee: {assignee}, Status: {status}")
#             #neo4j_node_properties = {'issue_key':issue_key, 'summary':summary, 'assignee':assignee, 'status':status}
#             #neo4j_dataIngester.create_node("JiraTicket", neo4j_node_properties)
#     else:
#         st.write(f"Error fetching issues. Status code: {response.status_code}")

# except requests.RequestException as e:
#     st.write(f"Error: {e}")


# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()
#     # Get the DCCP project and return issues
#     for proj_dict in data:
#        #st.write(proj_dict)
#        if proj_dict['key'] == "DCCP":
#           DCCP_api_url = proj_dict['self']

#     response_DCCP = requests.get(DCCP_api_url)
#     data_DCCP = response_DCCP.json()
#     st.write(data_DCCP)
    
# else:
#     st.write(f"Error: {response.status_code} - {response.text}")

