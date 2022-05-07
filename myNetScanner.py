import scapy.all as scapy
#1>>arp_request
#2>>broadcast
#3>>response

arp_request_packet = scapy.ARP(pdst="10.0.2.1/24") #arp request
#scapy.ls(scapy.ARP())
broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #broadcast
#scapy.ls(scapy.Ether())

#combined_packet = broadcast_packet/arp_request_packet #two packet in one(scapy language)
#result = scapy.srp(combined_packet,timeout=1)
#print(result)


combined_packet = broadcast_packet/arp_request_packet #two packet in one(scapy language)
(answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
answered_list.summary()



