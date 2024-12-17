from datasets import load_dataset
import json
import os

# Load the House MD transcripts dataset
ds = load_dataset("VishaalY/house-md-transcripts")

# check existing quotes from file 
existing_quotes = set()
json_file_path = 'data/house_quotes.json'

if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as f:
        existing_data = json.load(f)
        existing_quotes = {entry['line'] for entry in existing_data}

unique_lines = set()

# Access the dataset
print(ds)

# Filter the dataset to get only House's lines
house_lines = []
for entry in ds['train']:
    if entry['name'] == 'House' and entry['line'] not in unique_lines and entry['line'] not in existing_quotes:
        house_lines.append(entry)
        unique_lines.add(entry['line'])

# Print the first few lines to verify
for line in house_lines[:5]:
    print(line['line'])

existing_data.extend(house_lines)

# Write just House's lines to a JSON file
with open('data/house_quotes.json', 'w') as f:
    json.dump(existing_data, f)

