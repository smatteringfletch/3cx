# IP Policy Builder (CLI Version)

A simple Python CLI tool to convert a plain text IP list into a JSON policy file for IP whitelisting or blacklisting. The format used is for the 3CX Blacklist, the json and data array can be modified to change the output into your desired format.

---

## Features

- Reads an input text file containing pairs of policy names and IP addresses.
- Outputs a formatted JSON file with IP policies.
- Supports selecting block type: whitelist (1) or blacklist (0).
- Customizable input and output filenames.

---

## Prerequisites

- Python 3.x installed on your system.

---

## Usage

1. Prepare your IP list file (`ips.txt` by default) with alternating lines:

    ```
    PolicyName1
    192.168.1.1
    PolicyName2
    10.0.0.5
    ...
    ```

2. Run the script:

    ```bash
    python ip_builder.py
    ```

3. The script will prompt you for:

    - Input file name (press Enter to use default `ips.txt`)
    - Output JSON file name (press Enter to use default `IP_Formatted.json`)
    - Block type: `1` for whitelist or `0` for blacklist (default is `1`)

4. The JSON policy file will be generated at the specified output location.

---

## Example

```bash
Please provide a filename for IP List input file or press enter to use the default name ips.txt: 
Please provide a filename for Output JSON File or press enter to use the default name IP_Formatted.json: 
Please select 1 to whitelist these IP Addresses, or press 0 to blacklist: [Default: 1]: 

IP Policy JSON file created: {output}
```

## Authors
This project was authored by **Matt Fletcher**.

[![Linkedin](https://i.sstatic.net/gVE0j.png) LinkedIn](https://www.linkedin.com/in/fletcher-matt/)
&nbsp;[![GitHub](https://i.sstatic.net/tskMh.png) GitHub](https://github.com/smatteringfletch)
