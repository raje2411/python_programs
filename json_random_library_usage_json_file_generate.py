#!/usr/bin/env python3.7
import json
import os
import random

def generate_json_files() :
    count = int(os.getenv("FILE_COUNT") or 100)
    words = [word.strip() for word in open("/Users/rraman/python_programs/books/words").readlines()]
    for file_identifier_number in range(count) :
        amount = random.uniform(1.0, 1000)
        content = {
            'topic' : random.choice(words),
            'value' : '%.2f' % amount,
            'sub_values' : {
                'sub_topic' : random.choice(words), 'sub_value' : '%.2f' % random.uniform(1.0, 1000)
            }
        }
        # Dump the content into .json file
        with open(f"/Users/rraman/python_programs/books/new/receipt-{file_identifier_number}.json", 'w') as f :
          json.dump(content, f)


if __name__ == '__main__' :
    generate_json_files()
