from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.yfinance import YFinanceTools

# requires {uv add yfinance}

agent = Agent(
    model=Claude(id="claude-3-7-sonnet-latest"),
    tools=[YFinanceTools(stock_price=True)],
    instructions=[
        "Use tables to display data.",
        "Only include the table in your response. No other text.",
    ],
    markdown=True,
)
agent.print_response("What is the stock price of Apple and Samsung?", stream=True)

# agent.print_response("What was the stock price of Apple yesterday?", stream=True)
