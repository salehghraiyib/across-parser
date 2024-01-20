import json
import re
from unidecode import unidecode

def clean_german_text(text):

    # Remove extra whitespaces and line breaks
    cleaned_text = re.sub(r'\s+', ' ', text).strip()

    return cleaned_text


# Read the JSON file
# with open('modules.json', 'r') as file:
#    data = json.load(file)

#
# # Extract unique values of the 'name' field
# unique_codes = set(item['code'] for item in data.values())
# unique_names = set(item['name'] for item in data.values())
#
# # Print the unique names
# print("Unique Names:", unique_names)
# print(len(unique_names))
#
# # Specify the criterion key
# criterion_key = 'name'
#
# # Keep only the first occurrence of each unique criterion value
# filtered_data = {}
# unique_values_seen = set()
#
# for key, item in data.items():
#     criterion_value = item.get(criterion_key)
#     if criterion_value not in unique_values_seen:
#         unique_values_seen.add(criterion_value)
#         print(item.get("ECTS"))
#         # Use regular expression to extract numbers
#         numbers = re.findall(r'\d+', item.get("ECTS"))
#         if int(numbers[0]) <= 15:
#             item['aim'] = clean_german_text(item['aim'])
#             item['content'] = clean_german_text(item['content'])
#             item['program'] = clean_german_text(item['program']).strip()
#             if "mit" in item['program']:
#                 item['program'] = item['program'].split("mit")[0]
#             item['ECTS'] = numbers[0]
#             item['faculty'] = item['faculty'].strip()
#             item['name'] = item['name'].strip()
#             item['program'] = item['program'].strip()
#             filtered_data[key] = item
#
# # Convert the dictionary back to a list if necessary
# print(len(filtered_data))
#
# output_file_path = 'filtered_data.json'
#
# # Write the filtered data to a JSON file
# with open(output_file_path, 'w', encoding='utf-8') as output_file:
#     json.dump(filtered_data, output_file, ensure_ascii=False, indent=4)
