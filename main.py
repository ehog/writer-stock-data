import os
from dotenv import load_dotenv
import pandas as pd
from writerai import Writer

load_dotenv()

client = Writer(
    api_key=os.getenv('WRITER_API_KEY')
)

def load_stock_data_from_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        return data
    except Exception as e:
        print("Error loading data:", e)
        return None

def main():
    print("Hello Writer!")
    # Load the stock data
    file_path = 'daily_IBM.csv'
    stock_data = load_stock_data_from_csv(file_path)
    print(stock_data)



if __name__ == "__main__":
    main()