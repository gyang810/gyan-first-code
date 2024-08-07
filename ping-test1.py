import os
import time
import csv
from ping3 import ping
from datetime import datetime


def ping_devices():
  csv_file = 'C:/Users/948308/Desktop/Django-start/playground/devices.csv'
  output_file  = 'ping_results.txt'
  results = []
  
 # try:
  with open(csv_file, 'r' ) as file:
    reader = csv.reader(file)
    devices=[(row[0], row[1]) for row in reader ]

  for devices_name, ip_address in devices:  
    response = ping(ip_address, timeout=2)
    status="UP" if response is not None else "DOWN"
    results.append((devices_name, ip_address, status))
    
    print (f"pinging {ip_address}...{status}")
    timestamp = datetime.now().strftime('%y-%m-%d %H:%M:%S ')
    
    
    with open(output_file, 'w') as file:
     for devices_name, ip_address, status in results:       
      file.write(f"{devices_name} ({ip_address}) : {status}\n")
      
  
if __name__ =="__main__":
 ping_devices()