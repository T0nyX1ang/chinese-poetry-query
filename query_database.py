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
query = r".*[，。,.]" + query.replace(r"x", r"\w") + r"[，。,.].*"

with open(os.path.join(database_dir, "database.json"), "r",
          encoding="utf-8") as f:
    data = json.loads(f.read())

pattern = re.compile(query)

for item in data:
    if re.match(pattern, item["content"]):
        print(item["content"])

toc = default_timer()
print(toc - tic)
