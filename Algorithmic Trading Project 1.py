import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
import os

os.chdir(r'C:\Users\jc\PycharmProjects\untitled\algorithmic trading project 1 starter file')
stocks = pd.read_csv('sp_500_stocks.csv')
# have secrets.py with the API token in the same folder. secrets.py will contain the API Token. For testing, use IEX_CLOUD_API_TOKEN = 'Tpk_059b97af715d417d9f49f50b51b1c448'
from secrets import IEX_CLOUD_API_TOKEN

symbol = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()
price = data['latestPrice']
market_cap = data['marketCap']
print('Price for {} is ${}, with a market cap of {} \n'.format(symbol, price, market_cap))

# adding stock data to pandas dataframe
my_columns = ['Ticker', 'Price','Market Capitalization', 'Number Of Shares to Buy']
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

symbol_groups = list(chunks(stocks['Ticker'], 100))
symbol_strings = []
for i in range(0, len(symbol_groups)):
    symbol_strings.append(','.join(symbol_groups[i]))
#     print(symbol_strings[i])
final_dataframe = pd.DataFrame(columns = my_columns)
for symbol_string in symbol_strings:
    batch_api_call_url = f'https://sandbox.iexapis.com/stable/stock/market/batch/?types=quote&symbols={symbol_string}&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(batch_api_call_url).json()
    for symbol in symbol_string.split(','):
        final_dataframe = final_dataframe.append(pd.Series([
            symbol,
            data[symbol]['quote']['latestPrice'],
            data[symbol]['quote']['marketCap'],
            'NA'
        ], index=my_columns),ignore_index=True)

print(final_dataframe)

portfolio_size = input('Enter value of your portfolio:')

try:
    val = float(portfolio_size)
    print('Your porfolio value is {}'.format(val))
except ValueError:
    print('Please enter a number value.')
    portfolio_size = input('Enter the value fo your portfolio using numbers:')

position_size = float(portfolio_size) / len(final_dataframe.index)
for i in range(0, len(final_dataframe['Ticker'])-1):
    final_dataframe.loc[i, 'Number Of Shares to Buy'] = math.floor(position_size / final_dataframe['Price'][i])
final_dataframe

writer = pd.ExcelWriter('recommended trades.xlsx', engine='xlsxwriter')
final_dataframe.to_excel(writer, 'Recommended Trades', index=False)

background_color = '#0a0a23'
font_color = '#ffffff'

string_format = writer.book.add_format(
    {
        'font_color': font_color,
        'bg_color': background_color,
        'border': 1
    }
)

dollar_format = writer.book.add_format(
    {
        'num_format': '$0.00',
        'font_color': font_color,
        'bg_color': background_color,
        'border': 1
    }
)

int_format = writer.book.add_format(
    {
        'num_format': '0',
        'font_color': font_color,
        'bg_color': background_color,
        'border': 1
    }
)

column_formats = {
                    'A': ['Ticker', string_format],
                    'B': ['Price', dollar_format],
                    'C': ['Market Capitalization', dollar_format],
                    'D': ['Number of Shares to Buy', int_format]
                    }

for column in column_formats.keys():
    writer.sheets['Recommended Trades'].set_column(f'{column}:{column}', 20, column_formats[column][1])
    writer.sheets['Recommended Trades'].write(f'{column}1', column_formats[column][0], string_format)

# Save xlsx to cwd
writer.save()
