import streamlit as st
import requests
from requests.auth import HTTPBasicAuth
from neo4j import GraphDatabase
from dataIngester import DataIngester

# initiate Neo4j data ingester
uri = "bolt://10.75.0.78:7687"
username = "neo4j"
password = ""
neo4j_dataIngester = DataIngester(uri, username, password)

# Jira access credential
API_TOKEN = ""
USER = "dinghe@biosustain.dtu.dk"

st.title("Jira Issue Viewer")

# Jira API URL
url = "https://biosustain-dev.atlassian.net/rest/api/3/search"
# auth
auth = HTTPBasicAuth(USER, API_TOKEN)

headers = {
  "Accept": "application/json"
}

query = {
  'jql': 'project = DCCP',
  # does not seeem to work
  'maxResults': 1000
}

try:
    response = requests.request("GET", url, headers=headers,params=query,auth=auth)
    if response.status_code == 200:
        data = response.json()
        for issue in data.get("issues", []):
            issue_key = issue['key']
            summary = issue['fields']['summary']
            try: 
                assignee = issue['fields']['assignee']['displayName']
            except:
                assignee = issue['fields']['assignee']
            status = issue['fields']['status']['name']
            st.write(f"Issue Key: {issue_key}, Summary: {summary}, Assignee: {assignee}, Status: {status}")
            neo4j_node_properties = {'issue_key':issue_key, 'summary':summary, 'assignee':assignee, 'status':status}
            neo4j_dataIngester.create_node("JiraTicket", neo4j_node_properties)
    else:
        st.write(f"Error fetching issues. Status code: {response.status_code}")
except requests.RequestException as e:
    st.write(f"Error: {e}")

