import csv
import requests

# Disable self-signed warning
requests.packages.urllib3.disable_warnings()

#function to create if an address object exist or not
def address_exists(base_url, api_key, address_name):
    url = f"{base_url}/restapi/v10.2/objects/addresses"
    params = {
        'apikey':api_key,
        'filter':f"name eq ' {address_name}"
            }
    response = requests.get(url, params=params, verify=False)
    print(response.json())
    return response.status_code == 200 and response.json()['result']['count']>0

def create_address(base_url, api_key, address_name, address_value):
    url = f"{base_url}/restapi/v10.2/objects/Addresses"
    data = {
        'apikey':api_key,
        '@name':address_name,
        'ip-netmask':address_value
            }
    response = requests.post(url, json=data, verify=False)
    return response.status_code == 201 

def add_to_address_group(base_url, api_key, group_name, address_name):
    url = f"{base_url}/restapi/v10.2/objects/addressesgroups/{group_name}/members"
    data = {
        'apikey':api_key,
        'addressobjectname':address_name,
            }
    response = requests.post(url, json=data)
    return response.status_code == 201 

def process_csv(file_path, base_url, api_key, address_group_name):
    existing_address = []
    new_address = []

    with open(file_path, 'r') as cssvfile:
        csvreader = csv.DictReader(cssvfile)
        for row in csvreader:
            address_name = row['name']
            address_value = row['value']

            if address_exists(base_url, api_key, address_name):
                existing_address.append(address_name)
            else:
                if create_address(base_url, api_key, address_name, address_value):
                    new_address.append(address_name)
    
    for address_name in existing_address + new_address:
        add_to_address_group(base_url, api_key, address_group_name, address_name)

base_url  = "https://10.228.128.30"
api_key = 'LUFRPT1VMXovdm9ETmk4NkM4QUsvV1phS1MwOWlkZEU9UTJ4UWQzV0NWOXNrUi8wbjJWWVVyNUlybW9FWEg1cm9QWmhXNEQ5cDEyUnpjcEtxRWMzT2ZtczZSL3ZFd1pRNg=='
csv_file_path = 'addresses.csv'
address_group_name = "myaddressgroup"  

process_csv(csv_file_path, base_url, api_key, address_group_name)