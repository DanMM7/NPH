import socket
import struct

def unpack_packet(conn, header_format):
    try:
        header_size = struct.calcsize(header_format)
        header_data = conn.recv(header_size)

        if not header_data:
            return None

        version, header_length, service_type, payload_length = struct.unpack(header_format, header_data)
        payload_data = conn.recv(payload_length)

        # Decode payload based on service type
        if service_type == 1:  # Integer
            payload = struct.unpack("!i", payload_data)[0]
        elif service_type == 2:  # Float
            payload = struct.unpack("!f", payload_data)[0]
        elif service_type == 3:  # String
            payload = payload_data.decode()

        # Print received packet details
        packet_info = f"Version: {version}, Header Length: {header_length}, Service Type: {service_type}, Payload Length: {payload_length}, Payload: {payload}"
        print("Received Packet:", packet_info)

        # Convert everything back to bytes for sending back to the client
        response_packet = header_data + payload_data  # Ensuring both are bytes
        return response_packet

    except Exception as e:
        print("Error unpacking packet:", e)
        return None

if __name__ == "__main__":
    host, port = "localhost", 12345
    header_format = "!BBBH"  # Version (1 byte), Header Length (1 byte), Service Type (1 byte), Payload Length (2 bytes)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by: {addr}")
            while True:
                response = unpack_packet(conn, header_format)
                if response is None:
                    print("Closing connection...")
                    break
                conn.sendall(response)  # Echo back packet
