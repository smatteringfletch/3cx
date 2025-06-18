import json

def IP_Policy_Builder(input, output, block_type):
    
    with open(input, 'r') as ip_file:
        lines = ip_file.read().splitlines()
    
    data = []

    for i in range(0, len(lines), 2):
        policy_name = lines[i]
        static_ip = lines[i+1]

        data.append({
            "ip": static_ip,
            "blockType": block_type,
            "expirationDate": "3000-12-31T23:59+00:00",
            "description": f'{policy_name} IP Address'
        })

    with open(output, 'w') as json_dump:
        json.dump(data, json_dump, indent=4)
    
    print(f'IP Policy JSON file created: {output}')

def get_filename(filetype, default):
    user_input = input(f'Please provide a filename for {filetype} or press enter to use the default name {default} ')
    return user_input.strip() if user_input.strip() else default

def get_blocktype(default = 1):
    user_input = input(f'Please select 1 to whitelist these IP Addresses, or press 0 to blacklist: [Default: {default}] ')
    if user_input == '':
        return default
    elif user_input in ('0', '1'):
        return int(user_input)
    else:
        print("Invalid input, default whitelist has been selected")
        return default

if __name__ == "__main__":
    IP_List = get_filename("IP List input file", "ips.txt")
    JSON_Output = get_filename("Output JSON File", 'IP_Formatted.json')
    
    blockType = get_blocktype(1)
    IP_Policy_Builder(IP_List, JSON_Output, blockType)