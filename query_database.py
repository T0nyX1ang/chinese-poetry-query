"""Query a certain poem in a database."""

import sys
import os
import json
import re
from timeit import default_timer

tic = default_timer()

cwd = os.getcwd()
database_dir = os.path.join(cwd, "database")
query = sys.argv[1]
query = r".*[，。,.]" + query.replace("?", r"\w").replace(
    "*", r".*") + r"[，。,.].*"  # query pattern
pattern = re.compile(query)

for root, _, files in os.walk(database_dir):
    for file in files:
        with open(os.path.join(root, file), "r", encoding="utf-8") as f:
            data = json.loads(f.read())

        print('Searching in database: %s' % file[:-5])

        for item in data:
            target = re.match(pattern, item["content"])
            if target:
                print(item)

toc = default_timer()
print(toc - tic)
