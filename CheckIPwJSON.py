import json
import ipaddress

deviceJSON = '{"Version": "15.6", "locationN": "500 Northridge", "role": "Access", "upTime": "12:10:53.49", "hostname": "ATL-3650-1", "macAddress": "39:58:1f:9e:38:c1", "series": "Cisco Catalyst 3650 Series Switches", "lastUpdated": "2017-09-21 13:12:46", "bootDateTime": "2016-10-27 05:24:53", "interfaceCount": "24", "lineCardCount": "1", "managementIpAddress": "192.168.10.10", "interfaces": {"interface": [{"GigabitEthernet0": {"ipv4": "100.100.100.1"}}, {"GigabitEthernet1": {"ipv4": "10.10.10.2"}}]}}'

data = json.loads(deviceJSON)

int_ip = data["interfaces"]["interface"]

for int in int_ip:
    for interface, address in int.items():
        add = address["ipv4"]
        if ipaddress.IPv4Address(add).is_private:
            print("{} has an ip address of {}".format(interface, add) + " is a private ip address")
        else:
            print("{} has an ip address of {}".format(interface, add) + " is not a private ip address")





