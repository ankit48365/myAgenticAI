## This works via CLAUDE ANTHROPIC API


# follow Basic Agent in below URL
# https://docs.agno.com/introduction/agents

from agno.agent import Agent
from agno.models.anthropic import Claude

# API Details {https://console.anthropic.com/}

# Requires Anthropic API key 
# {echo 'export ANTHROPIC_API_KEY="sk-ant-xxxxxxxxxxxxx"' >> ~/.bashrc}
# source ~/.bashrc
# echo $ANTHROPIC_API_KEY


# User Input
Question = input("Enter your question: ")

# Main Model
agent = Agent(model=Claude(id="claude-3-7-sonnet-latest"), markdown=True)
agent.print_response(Question, stream=True)