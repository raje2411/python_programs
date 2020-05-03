#!/usr/bin/env python3.7
import json2hive
import json
from json2hive.utils import infer_schema
from json2hive.generators import generate_json_table_statement

# infer schema from objects, these objects could be the result of json.loads(...)
# object1 = {'name': 'John', 'age': 25}
# object2 = {'name': 'Mary', 'age': 23}
# schema = infer_schema([object1, object2])

with open("/Users/rraman/temp.json","r") as read_file:
    data = json.load(read_file)

# data = {"name": "Ford Prefect","species": "Betelgeusian"}

data ={
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}

data.strip()

schema = infer_schema([data])
# Generate CREATE TABLE statement
statement = generate_json_table_statement('example', schema, managed=True)
print(statement)
