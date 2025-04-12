from scapy.all import sniff

# Function to process each captured packet
def packet_callback(packet):
    if packet.haslayer("IP"):  # Check if the packet contains an IP layer
        print(f"Source: {packet['IP'].src} --> Destination: {packet['IP'].dst} | Protocol: {packet['IP'].proto}")

# Start sniffing on your network interface (Wi-Fi or eth0 depending on your system)
# 'count=10' captures 10 packets; remove it for continuous sniffing
print("Starting packet sniffing...")
sniff(prn=packet_callback, iface="wlan0", count=10)
print("Sniffing finished.")
