"""

Created on Sun 24 May 2020
@author: aman anand

"""


import scapy.all as scapy
from optparse import OptionParser
import socket

color = dict(
    FAIL="\033[91m",
    OKGREEN="\033[92m",
    OKBLUE="\033[94m",
    HEADER="\033[93m",
    END="\033[0m",
    BOLD="\033[1m",
)


def formatString(data):
    while len(data) < 15:
        data = data + " "
    return data


def getHostName(ip):
    try:
        host_name = socket.gethostbyaddr(ip)
        return str(host_name[0])
    except socket.herror:
        return " "


def getParameter():
    parser = OptionParser()
    parser.add_option("-i", "--ip", dest="ip", help="IP Address or Range")
    (option, args) = parser.parse_args()
    if not option.ip:
        parser.error(f"{color['FAIL']}[-] Please specify IP Range, For more details try --help {color['END']} ")

    return option


def scan(ip):
    packet_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    adp_request_broadcast = broadcast / packet_request
    answered, unanswered = scapy.srp(adp_request_broadcast, timeout=1, verbose=False)
    client_data_list = list()
    for element in answered:
        client_data_dict = {"ip": formatString(element[1].psrc), "mac": element[1].hwsrc,
                            "host": getHostName(element[1].psrc)}
        client_data_list.append(client_data_dict)
    if len(client_data_list) > 0:
        client_data_dict = {"ip": formatString(answered[0][1].pdst), "mac": answered[0][1].hwdst,
                            "host": getHostName(answered[0][1].pdst)}
        client_data_list.append(client_data_dict)
    return client_data_list


def print_client_details(data):
    print(f"{color['OKBLUE']}[-] Scanning Completed...")
    connected_devices = len(data)
    if connected_devices <= 0:
        print(f"{color['HEADER']}[-] No Device found.....{color['END']}")
    elif connected_devices == 1:
        print(f"{color['OKBLUE']}[-] One Device found.....{color['END']}")
    else:
        print(f"{color['OKGREEN']}[-] " + str(len(data)) + " Devices Found in this Network......" +
              f"{color['END']}")

    print("====================================================================================")
    print(f"{color['BOLD']}{color['HEADER']}IP Address\t\t   MAC Address\t\t\t   Host Name{color['END']}")
    print("====================================================================================")
    for element in data:
        print(f"{color['OKGREEN']}" + element["ip"] + "\t\t " + element["mac"] + "\t\t "
              + element["host"] + f"{color['END']}")


options = getParameter()
client_data = scan(options.ip)
print_client_details(client_data)


