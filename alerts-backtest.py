import csv
import os
from collections import defaultdict

# Function to parse the data from each line
def parse_line(line):
    ticker, timeframe, datetime, description, strategy, _, position_type, status = line.split(',')[:8] #only take the first 8 columns
    
    return {
        'ticker': ticker,
        'timeframe': timeframe,
        'datetime': datetime,
        'description': description,
        'strategy': strategy,
        'position_type': position_type,
        'status': status
    }

# Group by ticker and timeframe
grouped_data = defaultdict(lambda: defaultdict(list))

csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]

for file_name in csv_files:
    print(f"Processing file: {file_name}")
    with open(file_name, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for line in csv_reader:
            parsed_data = parse_line(','.join(line))  # Rejoin the line if it was split by csv.reader
            grouped_data[parsed_data['ticker']][parsed_data['timeframe']].append(parsed_data)

# Print or process grouped data
for ticker, timeframes in grouped_data.items():
    for timeframe, entries in timeframes.items():
        print(f"Ticker: {ticker}, Timeframe: {timeframe}")
        for entry in entries:
            print(f"  - Datetime: {entry['datetime']}, Position: {entry['position_type']}, Description: {entry['description']}, Strategy: {entry['strategy']}, Status: {entry['status']}")