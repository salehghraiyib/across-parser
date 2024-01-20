# This is a sample Python script.
import fitz
import re
import os
from read_id import get_key
import json

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    courses = dict()

    json_file_path = "modules.json"

    identifier = "1"
    # Check if the file exists
    if os.path.exists(json_file_path):
        identifier = str(get_key())


    for x in range(1, 2):
        doc = fitz.open('TU-Chemnitz/AB_2021_5_2.pdf')
        text = ""

        for page in doc:
            text += page.get_text()

        #program = text.split("Studienordnung für den Studiengang ")[1].split(" mit")[0].strip()
        program = text.split("Studienordnung für den konsekutiven Studiengang")[1].split(" \nmit")[0].strip()
        #program = text.split("Studienordnung für den englischsprachigen konsekutiven Studiengang")[1].split(" \nmit")[0].strip()
        level = text.split("Abschluss")[1].split(" of")[0]
        data = text.split("Modulnummer")[1:]
        #data = data[1:]

        for module in data:
            course_code = re.sub(r"[\n]*", "", module.split(" ")[1])
            #type = re.sub(r"[\n]*", "", module.split("MO type\n")[1].split("\n")[0]).split("\n")[0]
            uni = "Technische Universitat Chemnitz"
            study_faculty = re.sub(r"[\n]*", "", module.split("Modulverantwortlich")[1].split("Inhalte")[0])
            study_program = program
            course_name = re.sub(r"[\n]*", "", module.split("Modulname")[1].split("Modulverantwortlich")[0])
            ects = module.split("In dem Modul werden")[1].split(" erworben.")[0]
            course_aim = module.split("Qualifikationsziele:")[1].split("Lehrformen")[0].strip()
            course_content = module.split("Inhalte:")[1].split("Qualifikationsziele:")[0].strip()

            if course_code == "":
                continue

            module = {
                "code": course_code,
                "uni": uni,
                "faculty": study_faculty,
                "program": study_program,
                "level": level,
                "name": course_name,
                "ECTS": ects,
                "aim": course_aim,
                "content": course_content
            }
            courses[identifier] = module
            identifier = str(int(identifier) + 1)

    print(courses)

    # Check if the file exists
    if os.path.exists(json_file_path):
        # If the file exists, read its content first
        with open(json_file_path, 'r') as file:
            existing_data = json.load(file)

        # Update the existing data with the new data
        existing_data.update(courses)

        # Write the updated data back to the file
        with open(json_file_path, 'w') as file:
            json.dump(existing_data, file, indent=4, ensure_ascii=False,sort_keys=True)
    else:
        # If the file doesn't exist, create a new one and write the data
        with open(json_file_path, 'w') as file:
            json.dump(courses, file, indent=4, ensure_ascii=False,sort_keys=True)

    print(f'Data has been written to {json_file_path}')


