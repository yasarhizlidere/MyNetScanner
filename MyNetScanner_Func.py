import scapy.all as scapy
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress",dest="ip_address", help="enter IP address please")
    (user_input,arguments) = parse_object.parse_args()

    if not user_input.ip_address: #False
        print("enter IP address pls!")
    return user_input


def mynetscanner_func(ip):
    arp_request_packet = scapy.ARP(pdst="10.0.2.1/24") #arp request
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #broadcast
    combined_packet = broadcast_packet/arp_request_packet
    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
    answered_list.summary()

user_ip_address = get_user_input()
mynetscanner_func(user_ip_address.ip_address)
