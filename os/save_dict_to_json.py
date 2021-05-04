import json

total_result = [
    {"name": {"first": "Regina", "last": "Grabmaier"}},
    {"name": {"first": "Silke", "last": "Warnke-Rehm"}}
]

with open('result.json', 'w') as fp:
    json.dump(total_result, fp)
