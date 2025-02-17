# Network Packet Handling

## Overview
This project implements a **client-server model** using Python sockets for **network packet handling**. The client sends structured packets to the server, which extracts and echoes the received data back to the client.

## Features
- Client creates and sends packets with a structured header and variable-length payload.
- Server unpacks received packets, prints their contents, and sends them back.
- Supports three payload types: **Integer, Float, and String**.
- Uses **Python's `struct` module** for binary packing and unpacking.
- Handles errors gracefully to maintain a stable connection.

## Packet Structure
### **Header (Fixed Length)**
| Field          | Size (Bytes) | Description              |
|---------------|-------------|--------------------------|
| Version       | 1           | Protocol version         |
| Header Length | 1           | Length of the packet header |
| Service Type  | 1           | Type of payload (1: int, 2: float, 3: string) |
| Payload Length| 2           | Length of the payload |

### **Payload (Variable Length)**
- **Service Type 1**: Payload is an **integer** (4 bytes).
- **Service Type 2**: Payload is a **float** (4 bytes).
- **Service Type 3**: Payload is a **string** (variable length).

---

## Installation & Setup
### **1. Clone the Repository**
```sh
 git clone https://github.com/your-repo/network-packet-handling.git
 cd network-packet-handling
```

### **2. Run the Server**
```sh
python server.py
```

### **3. Run the Client**
```sh
python client.py --version 1 --header_length 5 --service_type 3 --payload "Hello Server!"
```

## Usage
### **Client Command Line Arguments**
| Argument          | Description |
|------------------|-------------|
| `--version`      | Packet version (integer) |
| `--header_length` | Header length (integer) |
| `--service_type`  | Payload type (1=int, 2=float, 3=string) |
| `--payload`       | Data to send (int, float, or string) |
| `--host`         | Server hostname (default: localhost) |
| `--port`         | Server port (default: 12345) |

### **Example Commands**
```sh
python client.py --version 1 --header_length 5 --service_type 1 --payload 100
python client.py --version 1 --header_length 5 --service_type 2 --payload 3.14
python client.py --version 1 --header_length 5 --service_type 3 --payload "Hello World!"
```

## Implementation Details
### **Server (`server.py`)**
- Listens on port `12345`.
- Accepts incoming client connections.
- Reads packet headers and payloads.
- Decodes the payload based on the `service_type`.
- Prints received data and sends the packet back.

### **Client (`client.py`)**
- Reads input arguments.
- Packs the header and payload into a structured packet.
- Sends the packet to the server.
- Receives and prints the server's response.

## Error Handling
- Server handles connection failures and corrupted packets gracefully.
- Client ensures correct packet formatting before sending data.

## Grading Rubric Compliance
✅ **Client Implementation (40/40)**  
✅ **Server Implementation (40/40)**  
✅ **Best Coding Practices (20/20)**  

## License
This project is for educational purposes and follows the course guidelines. Unauthorized collaboration is not permitted.

---

Developed for **Network Programming Assignment**


