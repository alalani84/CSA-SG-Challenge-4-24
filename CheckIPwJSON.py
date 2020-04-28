import json
import ipaddress

deviceJSON = '{"Version": "15.6", "locationN": "500 Northridge", "role": "Access", "upTime": "12:10:53.49", "hostname": "ATL-3650-1", "macAddress": "39:58:1f:9e:38:c1", "series": "Cisco Catalyst 3650 Series Switches", "lastUpdated": "2017-09-21 13:12:46", "bootDateTime": "2016-10-27 05:24:53", "interfaceCount": "24", "lineCardCount": "1", "managementIpAddress": "192.168.10.10", "interfaces": {"interface": [{"GigabitEthernet0": {"ipv4": "100.100.100.1"}}, {"GigabitEthernet1": {"ipv4": "10.10.10.2"}}]}}'

data = json.loads(deviceJSON)

gig0 = data["interfaces"]["interface"][0]["GigabitEthernet0"]["ipv4"]
gig1 = data["interfaces"]["interface"][1]["GigabitEthernet1"]["ipv4"]
ip = {"GigabitEthernet0":gig0, "GigabitEthernet1":gig1}

for interface, address in ip.items():
    if ipaddress.IPv4Address(address).is_private:
        print("{} has an ip address of {}".format(interface, address) + " is a private ip address")
    else:
        print("{} has an ip address of {}".format(interface, address) + " is not a private ip address")





