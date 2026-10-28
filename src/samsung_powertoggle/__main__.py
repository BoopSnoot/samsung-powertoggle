#!/usr/bin/python3

"""Toggle a Samsung Tizen TV on/off over the network.

On  -> Wake-on-LAN magic packet
Off -> KEY_POWER over the TV's websocket API

Setup:  pip install samsungtvws wakeonlan requests
Fill in TV_IP and TV_MAC below. First run: accept the "Allow" prompt on the TV.
"""
import os
import sys
import re
import requests
import wakeonlan
import socket
import ipaddress
from samsungtvws import SamsungTVWS
from platformdirs import PlatformDirs

dirs = PlatformDirs("samsung-powertoggle", ensure_exists=True)

TOKEN_FILE = os.path.join(dirs.user_cache_dir, "tv-token.txt")

def is_valid_ip(s: str) -> bool:
    try:
        ipaddress.ip_address(s)
        return True
    except ValueError:
        return False

def is_valid_mac(s: str) -> bool:
    """Accepts colon, dash, or dot-delimited MAC addresses."""
    s = s.replace(':', '').replace('-', '').replace('.', '')
    return bool(re.fullmatch(r'[0-9A-Fa-f]{12}', s))


def power_state(ip: str):
    """Return 'on', 'standby', or 'off' (unreachable)."""
    try:
        r = requests.get(f"http://{ip}:8001/api/v2/", timeout=2)
        state = r.json().get("device", {}).get("PowerState")
        # print(r.json())
        return state.lower()
    except Exception as e:
        return "off"


def main():
    if len(sys.argv) != 3:
        raise TypeError(f"Script requires 2 arguments but {len(sys.argv) - 1} were given")
    if not is_valid_ip(sys.argv[1]):   # Check for valid IP
        raise ValueError("Invalid IP format")

    if  not is_valid_mac(sys.argv[2]):   # Check for valid MAC
        raise ValueError("Invalid MAC format")

    tv_ip = sys.argv[1]
    tv_mac = sys.argv[2]
    tv = SamsungTVWS(host=tv_ip, port=8002, token_file=TOKEN_FILE, name=socket.gethostname())
    curr_power_state = power_state(tv_ip)
    # print(f'powerstate == {curr_power_state}')

    if curr_power_state == "on" or curr_power_state == 'standby':
        tv.send_key("KEY_POWER")
    else:
        # Send a few packets; Wi-Fi wake can miss the first one
        for _ in range(3):
            wakeonlan.wake(tv_mac)


if __name__ == "__main__":
    main()
