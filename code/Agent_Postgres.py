#################################################################
# Connection Vault Part

import os
import yaml
from src.connection_utility import (make_string)
# from sqlalchemy import create_engine
# import pandas as pd

conn_home = os.environ.get('conn_home')
connection_file = os.path.join(conn_home, 'connections.yaml')

with open(connection_file, "r") as file:
    connections = yaml.safe_load(file)

connection_detail = connections['pg_dlt']
CONNECTION_STRING = make_string(connection_detail)

print(CONNECTION_STRING)

#################################################################
# Agent Part
# follow Basic Agent in below URL
# https://docs.agno.com/tools/toolkits/database/postgres

#### ERRORED OUT ####  EXPECTING OPEN AI API KEY, not sure how to change to OPEN AI Key
# uv run Agency_Postgres.py
# postgresql+psycopg2://dlt_user:dlt_pass@ankiz-Lat-E5570:5432/dlt_dblx
# INFO Setting default model to OpenAI Chat                                                                                                                                                                        
# ERROR    API status error from OpenAI API: Error code: 401 - {'error': {'message': 'Incorrect API key provided: sk-proj-********************************************P7gE. You can find your API key at           
#          https://platform.openai.com/account/api-keys.', 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_api_key'}}                                                                             
# WARNING  Attempt 1/1 failed: Incorrect API key provided: sk-proj-********************************************P7gE. You can find your API key at https://platform.openai.com/account/api-keys.                    
# ERROR    Failed after 1 attempts. Last error using OpenAIChat(gpt-4o)                                                                                                                                            
# ▰▰▰▱▱▱▱ Thinking...




from agno.agent import Agent
from agno.tools.postgres import PostgresTools

# Initialize PostgresTools with connection details
# postgres_tools = PostgresTools(
#     host="localhost",
#     port=5532,
#     db_name="ai",
#     user="ai",
#     password="ai"
# )

postgres_tools = PostgresTools(CONNECTION_STRING)

# Create an agent with the PostgresTools
agent = Agent(tools=[postgres_tools])

# Example: Ask the agent to run a SQL query

agent.print_response("""
Please run a SQL query to get salary from salesman table for name 'romel'
""")

# agent.print_response("""
# Please run a SQL query to get all users from the users table
# who signed up in the last 30 days
# """)