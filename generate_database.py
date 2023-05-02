"""Generate database from json files."""

import os
import json
import opencc

converter = opencc.OpenCC("t2s.json")


def process_data(filename: str) -> dict:
    """Process data from json file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.loads(f.read())
    except Exception:
        print("Not a JSON file: ", filename)
        return []

    converted_data = []
    total = 0

    if isinstance(data, dict):
        data = [data]  # extra extraction for mismatched data
        # TODO: more extraction for mismatched data

    for item in data:
        try:
            content = {}
            paragraph = "".join(
                [converter.convert(p)
                 for p in item["paragraphs"]]) if "paragraphs" in item else ""
            para = "".join([converter.convert(p)
                            for p in item["para"]]) if "para" in item else ""
            contents = "".join([converter.convert(p) for p in item["content"]
                                ]) if "content" in item else ""

            content["content"] = paragraph + para + contents

            # extra extraction for poems with chapters, sections and titles
            chapter = converter.convert(
                item["chapter"]) if "chapter" in item else ""
            section = converter.convert(
                item["section"]) if "section" in item else ""
            title = converter.convert(item["title"]) if "title" in item else ""
            content["title"] = str.strip(chapter + " " + section + " " + title)

            content["author"] = converter.convert(
                item["author"]) if "author" in item else ""
            if 'caocao.json' in filename:
                content["author"] = '曹操'  # extra extraction

            if content["content"]:
                converted_data.append(content)
                total += 1
        except:
            continue


    print("Processed %d items from %s" % (total, filename))
    return converted_data


cwd = os.getcwd()
working_dir = os.path.join(cwd, "chinese-poetry")
database_dir = os.path.join(cwd, "database")
database = []

if not os.path.exists(database_dir):
    os.mkdir(database_dir)

for root, _, files in os.walk(working_dir):
    for file in files:
        filename = os.path.join(root, file)
        if "error" in filename:
            continue
        data = process_data(filename)
        database.extend(data)

print('Total items:', len(database))

with open(os.path.join(database_dir, "database.json"), "w",
          encoding="utf-8") as f:
    f.write(json.dumps(database, ensure_ascii=False, indent=4))
