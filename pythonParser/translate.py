import json

# Specify the input and output file paths
input_file_path = 'Final/translated_data.json'
output_file_path = 'Final/translated_data.json'

# Read JSON data from the input file
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract the values (entries) and create a list of dictionaries
entries_without_id = list(data.values())

# Write the modified data to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(entries_without_id, output_file, indent=4, ensure_ascii=False)
