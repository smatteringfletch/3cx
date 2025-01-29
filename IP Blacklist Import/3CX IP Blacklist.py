import json

def IP_Whitelist_3CX(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.read().splitlines()
    
    data = []
    for i in range(0, len(lines),2):
        # The .txt file should have every entry on a new line. Description of the entry with the IP address on a new line. For example:
        # Head Office - NSW
        # 192.168.100.250
        # The above IP address needs to be the PUBLIC IP address of the site. The above is an example only.
        office_name = lines[i]
        static_ip = lines[i+1]
        data.append({
            "ip": static_ip,
            "blockType": 1, # Block Type 1 is whitelist, Block Type 0 is blacklist
            "expirationDate": "2999-12-31T23:59:59+00:00", # This can be any value. I set this value high so it wouldn't expire and be removed anytime soon.
            "description": f'{office_name} Static IP'
        })
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

IPs_To_Whitelist = 'CurrentIPsJD.txt'
JSON_To_Upload = 'Whitelist_Upload.json'

IP_Whitelist_3CX(IPs_To_Whitelist, JSON_To_Upload)
