"""
Imports:
json for handling JSON data.
sys for handling command-line arguments.
ipaddress for IP address validation.
"""

import json
import sys
import ipaddress


def ip_print(path_to_json):
    """
    Extracts IP addresses from a JSON file.

    This function reads a JSON file and extracts the IP addresses from the "value"
    object inside the "vm_private_ips" key. If a "network" object is present, it also
    extracts corresponding IP addresses for the same names and prints them on the same line.

    Args:
        path_to_json (str): The name of the JSON file to be read.

    Returns:
        list: A list of formatted IP addresses.

    Raises:
        FileNotFoundError: If the specified file is not found.
        json.JSONDecodeError: If there is an error decoding the JSON data.
        KeyError: If required keys are missing in the JSON data.
        TypeError: If the data types in the JSON file are not as expected.
        ValueError: If an invalid IP address is detected.
        Exception: For any other unexpected errors.
    Note: Any other uncaught exceptions are handled by try catch block
    """
    try:
        with open(path_to_json, 'r') as file:
            data = json.load(file)

        # Extract private IPs from the 'value' object
        vm_private_ips = data.get('vm_private_ips', {}).get('value', {})

        # Extract network IPs from the 'network' object
        network_vms = data.get('network', {}).get('vms', [])
        network_ips = {vm['attributes']['name']: vm['attributes']['access_ip_v4'] for vm in network_vms}

        results = []
        for name, private_ip in vm_private_ips.items():
            network_ip = network_ips.get(name, "")
            if network_ip:
                if is_valid_ip(private_ip) and is_valid_ip(network_ip):
                    results.append(f"{private_ip} {network_ip}")
                else:
                    raise ValueError(f"Invalid IP address detected: {private_ip}, {network_ip}")
            else:
                if is_valid_ip(private_ip):
                    results.append(private_ip)
                else:
                    raise ValueError(f"Invalid IP address detected: {private_ip}")

        return results

    except FileNotFoundError:
        print(f"File '{path_to_json}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file, check if json format is good'{path_to_json}'.")
        sys.exit(1)
    except KeyError as e:
        print(f"Key error, Check if keys are correct: {e}")
        sys.exit(1)
    except TypeError as e:
        print(f"Type error: {e}")

    except ValueError as e:
        print(f"Value error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def is_valid_ip(ip_addr):
    """
    Validates an IP address.

    The function checks if the given string is a valid IP address.

    Args:
        ip_addr (str): The IP address to be validated.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    try:
        ipaddress.ip_address(ip_addr)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("User input error: Check if you are providing in following way: python extract_ips.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    ip_addresses = ip_print(filename)

    print("Please find below extracted IP addresses from the file:")
    for ip in ip_addresses:
        print(ip)
