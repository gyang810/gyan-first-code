import requests
import json

# Disable self-signed warning
requests.packages.urllib3.disable_warnings()

# Rest API URI
location = {'location': 'device-group', 'device-group': 'Global'}

api_url = "https://10.228.128.30/restapi/v10.2/Policies/SecurityPreRules"

headers = {'X-PAN-KEY': 'LUFRPT1VMXovdm9ETmk4NkM4QUsvV1phS1MwOWlkZEU9UTJ4UWQzV0NWOXNrUi8wbjJWWVVyNUlybW9FWEg1cm9QWmhXNEQ5cDEyUnpjcEtxRWMzT2ZtczZSL3ZFd1pRNg=='}

r = requests.get(api_url, params=location, verify=False, headers=headers)

json_object = json.loads(r.text)
json_formatted_str = json.dumps(json_object, indent=2)

print(json_formatted_str)


