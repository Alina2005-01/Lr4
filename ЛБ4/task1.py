# TODO решите задачу
import json
import os

def task() -> float:
    file_path = os.path.join(os.path.dirname(__file__), 'input.json')

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    total = sum(item['score'] * item['weight'] for item in data)
    return round(total, 3)

print(task())
