# 3CX IP Blacklist

This script takes a .txt file and outputs a .json file that the 3CX Blacklist can use.

## .txt file format

The .txt file should be formatted in the following way

```
Site Name
Site Static IP Address
```
For example, let's say we want to add the static IP 123.456.789.1 and give it the description of Head Office, the .txt file should look like this
```
Head Office
123.456.789.1
```
## How to use

1. Download the IP Blacklist Import folder
2. Add your IP whitelist.txt file to the same directory as the 3CX IP Blacklist.py file.
3. Edit line 24 from `IPs_To_Whitelist = 'ips.txt' to the name of the txt file. Alternatively, rename the .txt file to ips.txt
4. Open the Python file in an IDE such as Visual Studio Code
5. Run the file. A JSON file will be created called Whitelist_Upload.json

## Uploading to 3CX

### For Version 18

1. Log into the 3CX Management console.
2. Expand Security
3. Open **IP Blacklist**

### For Version 20

1. Sign into the Web Client and click on Admin in the bottom right.
2. Click on **Advanced**
3. Open the **IP Blacklist**

### For both versions

4. Click on **Import**
5. Select the "Whitelist_Upload.json" file
6. Once uploaded, all static IP addresses should be added.

## Notes

- This code is designed to whitelist these IP addresses. If you are blacklisting IP addresses instead, please change line 17 from `"blockType": 1,` to `"blockType": 0,`
- Once uploaded the Expiration date shows as 01/01/3000 at 10:59:59 instead of the default time specified in the code. 
