import yaml
import json

with open('order.yaml') as yaml_file:
    templates = yaml.safe_load(yaml_file)
    print(templates['invoice'])
    print(templates['bill-to']['address'])
    products = templates['product']
    for i in products:
        print(i['price'], i['description'], i['quantity'])


with open('order.yaml') as yaml_file, \
        open('yaml_to_json.json', 'w') as json_file:
    yaml_file = yaml.safe_load(yaml_file)
    j_d = json.dumps(yaml_file, sort_keys=True, default=str)
    json.dump(j_d, json_file)
