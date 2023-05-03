"""Generate database from chinese-poetry."""

import os
import json
import csv

def process_data(filename: str) -> dict:
    """Process data from csv file."""
    converted_data = []
    total = 0

    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = csv.reader(f)
            for item in data:
                if len(item) == 5 and str.isalnum(item[0]):
                    content = {}
                    content["title"] = item[1]
                    content["dynasty"] = item[2]
                    content["author"] = item[3]
                    content["content"] = item[4]
                    converted_data.append(content)
                    total += 1
    except Exception:
        print("Not a CSV file: ", filename)
        return []

    print("Processed %d items from %s" % (total, filename))
    return converted_data


def run():
    """Generate database from PoetryLibrary."""
    cwd = os.getcwd()
    working_dir = os.path.join(cwd, "PoetryLibrary")
    database_dir = os.path.join(cwd, "database")
    database = []

    if not os.path.exists(database_dir):
        os.mkdir(database_dir)

    for root, _, files in os.walk(working_dir):
        for file in files:
            filename = os.path.join(root, file)
            if "csv" not in filename:
                continue
            data = process_data(filename)
            database.extend(data)

    print('Total items:', len(database))

    with open(os.path.join(database_dir, "chinese_poetry_broad.json"),
              "w", encoding="utf-8") as f:
        f.write(json.dumps(database, ensure_ascii=False, indent=4))
