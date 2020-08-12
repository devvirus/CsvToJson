from csvtojson import make_json_tree
import json

lis_arr = make_json_tree('data.csv')
with open('data.json', 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(lis_arr, indent=4))
