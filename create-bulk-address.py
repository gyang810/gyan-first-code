import requests
import json
import csv

# Disable self-signed warning
requests.packages.urllib3.disable_warnings()

headers = {'X-PAN-KEY': 'LUFRPT1VMXovdm9ETmk4NkM4QUsvV1phS1MwOWlkZEU9UTJ4UWQzV0NWOXNrUi8wbjJWWVVyNUlybW9FWEg1cm9QWmhXNEQ5cDEyUnpjcEtxRWMzT2ZtczZSL3ZFd1pRNg=='}

api_url = "https://10.228.128.30/restapi/v10.2/Objects/Addresses"

with open ('object_source.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row['object_name']
        ip = row['ip']
        location = {'location': 'shared', 'name': name}

        body = json.dumps(
            {
                "entry":
                {
                    "@name": name,
                    "ip-netmask": ip
                }
            }
        )

        r = requests.post(api_url, params=location, verify=False, headers=headers, data=body)
        print(r.text)