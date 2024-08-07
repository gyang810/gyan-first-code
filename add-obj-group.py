import csv
import requests
import json
# Disable self-signed warning
requests.packages.urllib3.disable_warnings()

base_url  = "https://10.228.128.30"
csv_file_path = 'addresses.csv'
address_group_name = "myaddressgroup"  
headers = {'X-PAN-KEY': 'LUFRPT1VMXovdm9ETmk4NkM4QUsvV1phS1MwOWlkZEU9UTJ4UWQzV0NWOXNrUi8wbjJWWVVyNUlybW9FWEg1cm9QWmhXNEQ5cDEyUnpjcEtxRWMzT2ZtczZSL3ZFd1pRNg=='}
fun_url = f"{base_url}/restapi/v10.2/Objects/Addresses"
address_name = ['test1', 'test2']
address_group_name = "test-addressgroup"


location = {'location': 'shared', 'name': address_group_name}
url = f"{base_url}/restapi/v10.2/Objects/AddressGroups"
    
body = json.dumps ( 
    {
        "entry": 
            {    
        '@name':address_group_name,
        '@location':"shared",
        
        "static":{
            
            "member":address_name
        
        }
       }
        
                
            }
    
 ) 
response = requests.post(url, verify=False, headers=headers, data=body, params=location)
print(response.json())
print(address_name)
    