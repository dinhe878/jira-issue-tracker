import streamlit as st
import requests
from requests.auth import HTTPBasicAuth
from neo4j import GraphDatabase
from dataIngester import DataIngester

# initiate Neo4j data ingester
uri = "bolt://10.75.0.78:7687"
username = "neo4j"
password = "rEV6UgEk9PiVGE"
neo4j_dataIngester = DataIngester(uri, username, password)

# Jira access credential
API_TOKEN = "ATATT3xFfGF0AZYY7Lr8oRZj53hkX6zM8Xr_87V4vG3SKRAWrMAxePlNB23AvpbGGoLiF7zE6frC7dfPtAXuNvAYI1rcNvBC-CE9E94k67i9nzgCDzvjbHwcog880GL11FDi5-Zm3g4RSWb69IEqKuzhfmLbMYSZpBtIxy7N_jelMOCbzWqtXcc=D69A42DD"
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

