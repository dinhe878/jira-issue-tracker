import streamlit as st
import requests

# Jira server URL, API token and USER
JIRA_BASE_URL = "https://biosustain-dev.atlassian.net/jira"
API_TOKEN = "ATATT3xFfGF03YAmMcNMmpBQpW_ngTT_fkltfVQtRCiXGOFJYQCerT72u8DMRBk7izmnMBJ3vTADxH-bZDP1kMR_fOH1M0pfxuh3HeT71ZNyBhAn7HXfINwhx2i7iaB-5kvLvpgcHauJec_WsyERUYmfv8IN7BuwvCkIIh2cK7d57sNlhjGhwyk=94B2E4D3"
USER = 'dinghe@biosustain.dtu.dk'

st.title("Jira Issue Viewer")

# Example JQL query (replace with your own)
jql_query = "assignee = currentUser() AND resolution = Unresolved order by updated DESC"

# Construct the API URL
api_url = f"{JIRA_BASE_URL}/rest/api/2/search?jql={jql_query}"

try:
    response = requests.get(api_url, auth=(USER, API_TOKEN))
    if response.status_code == 200:
        data = response.json()
        for issue in data.get("issues", []):
            st.write(f"Issue Key: {issue['key']}, Summary: {issue['fields']['summary']}")
    else:
        st.write(f"Error fetching issues. Status code: {response.status_code}")
except requests.RequestException as e:
    st.write(f"Error: {e}")

