from scapy.all import rdpcap, IP

def analyze_packets(pcap_file):
    packets = rdpcap(pcap_file)

    print(f"Total Packets: {len(packets)}\n")

    for i, packet in enumerate(packets, start=1):
        print(f"Packet #{i}")

        if IP in packet:
            print("Source IP:", packet[IP].src)
            print("Destination IP:", packet[IP].dst)
            print("Protocol:", packet[IP].proto)

        print("Packet Length:", len(packet))

        if packet.payload:
            print("Payload:", bytes(packet.payload)[:50])

        print("-" * 50)

pcap_file = input("Enter PCAP file path: ")
analyze_packets(pcap_file)