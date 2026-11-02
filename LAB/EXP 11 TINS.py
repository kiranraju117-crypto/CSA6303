
from scapy.all import sniff

def display_packet(packet):
    print("\nCaptured Packet:")
    print(packet.summary())

print("Starting Packet Sniffing...")
print("Press Ctrl+C to stop capturing.\n")

try:
    sniff(
        count=10,
        prn=display_packet,
        store=False
    )
except KeyboardInterrupt:
    print("\nPacket sniffing stopped.")

