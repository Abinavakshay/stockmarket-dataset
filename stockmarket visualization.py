import autogen
import yfinance as yf
import matplotlib.pyplot as plt
import io
from PIL import Image


def fetch_stock_data(stock_symbol: str, period: str = "1mo"):
    try:
        stock = yf.Ticker(stock_symbol)
        data = stock.history(period=period)

        if data.empty:
            return f"No data found for {stock_symbol}. Check if it's a valid ticker or try a different" 
        plt.figure(figsize=(8, 4))
        plt.plot(data.index, data['Close'], label=f'{stock_symbol} Closing Prices', marker='o')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.title(f'{stock_symbol} Stock Price Over {period}')
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        plt.show()  
        
        return f"Stock data for {stock_symbol} visualized successfully."

    except Exception as e:
        return f"Error fetching data for {stock_symbol}: {str(e)}"

class StockAgent(autogen.AssistantAgent):
    def __init__(self, name="StockAgent"):
        super().__init__(name=name, llm_config=False)  

    def run(self, stock_symbol: str, period: str = "1mo"):
        return fetch_stock_data(stock_symbol, period) 
stock_agent = StockAgent()


if __name__ == "__main__":
    stock_symbol = input("Enter stock symbol (e.g., AAPL, TSLA, MSFT): ").upper()
    period = input("Enter time period (e.g., 1d, 1mo, 6mo, 1y, 5y): ").lower()
    
    response = stock_agent.run(stock_symbol, period)
    print(response)
