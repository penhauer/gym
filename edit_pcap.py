from scapy.all import rdpcap, wrpcap, IP
import sys


if len(sys.argv) <= 4:
    print("Provide souce_ip and dest_ip")
    exit(1)



# Define your input and output PCAP file paths
input_pcap = sys.argv[1]
output_pcap = sys.argv[2]

# Define the source and destination IP addresses to replace with
new_source_ip = sys.argv[3]
new_dest_ip = sys.argv[4]

# Read the PCAP file
packets = rdpcap(input_pcap)

# Loop through the packets and modify IP addresses
for packet in packets:
    if packet.haslayer(IP):  # Check if it's an IP packet
        # Modify the source and destination IP addresses
        packet[IP].src = new_source_ip
        packet[IP].dst = new_dest_ip
        
        # Recalculate checksums for the modified packet
        del packet[IP].chksum
        del packet[IP].len

    print(packet)

# Write the modified packets to the output PCAP file
wrpcap(output_pcap, packets)

print(f"PCAP file modified and saved as {output_pcap}")
