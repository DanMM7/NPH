import argparse
import socket
import struct

def create_packet(version, header_length, service_type, payload):
    try:
        if service_type == 1:  # Integer
            payload_data = struct.pack("!i", int(payload))
        elif service_type == 2:  # Float
            payload_data = struct.pack("!f", float(payload))
        elif service_type == 3:  # String
            payload_data = payload.encode()
        else:
            raise ValueError("Invalid service type")

        payload_length = len(payload_data)
        header_format = "!BBBH"
        header = struct.pack(header_format, version, header_length, service_type, payload_length)

        return header + payload_data  # Full packet

    except Exception as e:
        print("Error creating packet:", e)
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Client for packet creation and sending.")
    parser.add_argument("--version", type=int, required=True, help="Packet version")
    parser.add_argument("--header_length", type=int, required=True, help="Length of the packet header")
    parser.add_argument("--service_type", type=int, required=True, help="Service type (1=int, 2=float, 3=string)")
    parser.add_argument("--payload", type=str, required=True, help="Payload to be packed into the packet")
    parser.add_argument("--host", type=str, default="localhost", help="Server host")
    parser.add_argument("--port", type=int, default=12345, help="Server port")

    args = parser.parse_args()

    packet = create_packet(args.version, args.header_length, args.service_type, args.payload)
    
    if packet:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((args.host, args.port))
            s.sendall(packet)

            response = s.recv(1024)
            print("Response from server:", response)
