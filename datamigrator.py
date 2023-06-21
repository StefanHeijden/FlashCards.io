import json
import os
import csv


def find_csv_files(directory):
    csv_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                csv_files.append(os.path.join(root, file))
    return csv_files


def process_csv_files(csv_files):
    data_dict = []
    for file in csv_files:
        file_path = os.path.abspath(file)
        subject = os.path.basename(os.path.dirname(file_path))
        source = os.path.basename(os.path.dirname(os.path.dirname(file_path)))

        with open(file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                themes = []
                for i in range(2, len(row)):
                    themes.append(row[i])
                data_dict.append(
                    {
                        "question": row[0],
                        "answer": row[1],
                        "source": source,
                        "subject": subject,
                        "themes": themes,
                        "seen": 0
                    }
                )
    return data_dict


directory_path = "."
csv_files = find_csv_files(directory_path)
data_dict = process_csv_files(csv_files)

# Save data_dict as JSON
with open("Questions_And_Answers.json", "w") as json_file:
    json.dump(data_dict, json_file, indent=4)
