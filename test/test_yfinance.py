import pytest
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.yfinance import YFinanceTools


def test_stock_price_retrieval(capfd):
    agent = Agent(
        model=Claude(id="claude-3-7-sonnet-latest"),
        tools=[YFinanceTools(stock_price=True)],
        markdown=True,
    )

    # Capture printed output
    agent.print_response("What is the stock price of Apple?", stream=True)
    captured = capfd.readouterr()
    response = captured.out  # Get printed output
    assert response is not None
    assert "Apple" in response  # Ensure Apple's stock price is included


if __name__ == "__main__":
    pytest.main()