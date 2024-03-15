import json
import re

# filter non ascii characters 
def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i) < 128)

with open(r'C:\Users\saleh\Downloads\pythonParser\pythonParser\Final\translated_data.json', 'r', encoding="utf8") as file:
    data = json.load(file)

# Create a list to store modified entries
modified_data_list = []

for item in data:
    content_text = f"Content:{remove_non_ascii(item['content'])} \nAim:{item['aim']}"
    content_text = re.sub(r'\s+', ' ', content_text).strip()
    print(content_text)
    # if "in " in item["degree-program"]:
    #     degreepg = item["degree-program"].split("programme\n")[1].split("in ")[1].strip()
    # else:
    #     degreepg = re.sub(r'\s+', ' ', item["degree-program"].split("programme\n")[1])
    #     if "programme" in degreepg:
    #         degreepg = re.sub(r'\s+', ' ', degreepg.split("programme")[1])


    modified_data = {
        "name": remove_non_ascii(item["name"]),
        "degree-program": item["faculty"],
        "level": item["level"],
        "content": content_text,
        "uni-code": item["code"],
        "ECTS": int(item["ECTS"]),
        "program": item["program"],
        "university": "Technische Universitat Chemnitz"
    }

    print(modified_data)
    modified_data_list.append(modified_data)

with open("pythonParser/Final/translated_data_1.json.json", 'w') as file:
    json.dump(modified_data_list, file, indent=2)

print(len(modified_data_list))