import fitz
import re
import json
from data_transformation import clean_german_text as cgt
import os
from glob import glob

courses = []

# Path to your JSON file
json_file_path = 'Poland.json'
pdf_directory = 'Poland/'

pdf_files = glob(os.path.join('Poland/*.pdf'))
print(pdf_files)

# Check if the file exists
if os.path.exists(json_file_path):
    # Read the existing JSON content
    with open(json_file_path, 'r') as file:
        existing_data = json.load(file)
else:
    # If the file does not exist, start with an empty list
    existing_data = []

# University of bialystok
# for pdf_file in pdf_files:
#     doc = fitz.open(pdf_file)
#     text = ""
#
#     for page in doc:
#         text += page.get_text()
#
#     text = cgt(text)
#
#     print("print",text)
#     print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
#     module = text
#     course_code = module.split("Course code")[1].split("Course type")[0].strip()
#     print(course_code)
#     type = module.split("Course type")[1].split("Forms and")[0].strip()
#     uni = "Bialystok University Of Technology"
#     study_faculty = cgt(module.split("unit conducting the course ")[1].split("Date of issuing the")[0])
#     print(study_faculty)
#     level = cgt(module.split("and programme type")[1].split("Specialization")[0])
#     print(level)
#     course_name = cgt(module.split("Course name")[1].split("Course code")[0])
#     print(course_name)
#     ects = cgt(module.split("No. of ECTS credits")[1].split("Entry")[0])
#     print(ects)
#     course_aim = cgt(module.split("Course objectives")[1].split("Course content")[0].strip())
#     print(course_aim)
#     course_content = cgt(module.split("Course content")[1].split("Teaching methods")[0].strip())
#
#     module = {
#         "code": course_code,
#         "type": type,
#         "uni": uni,
#         "faculty": study_faculty,
#         "level": level,
#         "name": course_name,
#         "ECTS": ects,
#         "aim": course_aim,
#         "content": course_content
#     }
#     existing_data.append(module)
#
#     # Write the updated content back to the JSON file
#     with open(json_file_path, 'w') as file:
#         json.dump(existing_data, file, indent=4)
#
#

print(len(existing_data))