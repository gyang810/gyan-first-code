#Works
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
address_name = 'MCS_129.47.0.0-16'
address_group_name = "test-addressgroup"

def address_exists(url, address):
  params = {       
        'name': {address},
        'location': 'shared'
            }
  response = requests.get(url, verify=False, params=params, headers=headers)
  #print(response.json())
  #print(f"No need to create {address} ")
  return response.status_code == 200 and response.json()
  


def create_address(url, address_name, address_value):
 location = {'location': 'shared', 'name': address_name}
 body = json.dumps ( 
    {
        "entry": 
            {    
        '@name':address_name,
        'ip-netmask':address_value,
                
            }
    }
 )
 response = requests.post(url, verify=False, headers=headers, data=body, params=location)
 #print(response.json())
 print(f"created new address object {address_name}")
 
def add_to_address_group(url, address_group_name, address_name):
 location = {'location': 'shared', 'name': address_group_name}
 url = f"{base_url}/restapi/v10.2/objects/addressgroups"
    
 body = json.dumps ( 
    {
        "entry": 
            {    
        '@name':address_group_name,
        "static": {
            "member":address_name
       }
        
                
            }
    }
 ) 
 response = requests.post(url, verify=False, headers=headers, data=body, params=location)
 print(response.json())
 #print(address_name)
    

def process_csv(url, file_path):
    existing_address = []
    new_address = [] 
    #final_list = []
    with open(file_path, 'r') as cssvfile:
       csvreader = csv.DictReader(cssvfile)
       for row in csvreader:
           address_name = row['name']
           address_value = row['value']

           if address_exists(url, address_name):
              existing_address.append(address_name)
              
              
           else:
               if create_address(url, address_name, address_value):
                   new_address.append(address_name)
                   
    #print(f"New addresses are {new_address}")
    # print(f"Existing addresses are {existing_address}")
    
    
    final_list = existing_address + new_address
    print (f"Final list is {final_list}")
    add_to_address_group(url, address_group_name, final_list)
               
               
# print(new_address)
#print(address_name)
process_csv(fun_url, csv_file_path)
   
#    for address_name in existing_address + new_address:
#        add_to_address_group(base_url, api_key, address_group_name, address_name)



