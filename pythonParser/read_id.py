import json


# Read json file - compassing of modules
def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}


# returns the next id to be added to the list that is being collected
def generate_next_id(existing_ids):
    if existing_ids:
        return str(int(max(existing_ids)) + 1)
    else:
        return '1'


# reads the file that is created -> returns the next id to give the next module that will be imported and it will be added
def get_key():
    json_file_path = 'modules.json'

    # Step 1: Load existing JSON data
    existing_data = read_json(json_file_path)

    # Step 2: Extract existing IDs (assuming they are string representations of numbers)
    existing_ids = [int(key) for key in existing_data.keys() if key.isdigit()]
    print(existing_ids)

    # Step 3: Find the maximum ID in file
    max_id = max(existing_ids, default='0')

    # Step 4: Generate a new ID in file
    new_id = generate_next_id(existing_ids)
    print(new_id)

    # Step 5: Add the new entry with the generated ID
    return new_id
