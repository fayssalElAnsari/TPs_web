import sys
import socket

# Parse command-line arguments
if len(sys.argv) < 3:
    print("Usage: http_client.py <URI> <METHOD> [HEADER1 HEADER2 ...]")
    sys.exit(1)

uri = sys.argv[1]
method = sys.argv[2]
headers = {}
if len(sys.argv) > 3:
    for header in sys.argv[3:]:
        name, value = header.split(":", 1)
        headers[name.strip()] = value.strip()

# Check protocol
if not uri.startswith("http://"):
    print("Error: Only HTTP protocol is supported")
    sys.exit(1)

# Parse URI
_, _, host_port, path = uri.split("/", 3)
host, port = host_port.split(":", 1) if ":" in host_port else (host_port, 80)

# Create socket and connect to server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, int(port)))

    # Construct HTTP request message
    request = f"{method} {path} HTTP/1.1\r\n"
    request += f"Host: {host}\r\n"
    for name, value in headers.items():
        request += f"{name}: {value}\r\n"
    if method in ["POST", "PUT"]:
        if len(sys.argv) > 4:
            body = open(sys.argv[4], "rb").read()
        else:
            print("Please type the message body (end with ctrl-D):")
            body = sys.stdin.read()
        request += f"Content-Length: {len(body)}\r\n"
    request += "\r\n"
    if method in ["POST", "PUT"]:
        request += body

    # Send HTTP request to server
    s.sendall(request.encode())

    # Receive HTTP response from server
    response = b""
    while True:
        data = s.recv(1024)
        if not data:
            break
        response += data

    # Parse HTTP response
    status_line, headers, body = response.split(b"\r\n\r\n", 2)
    status_code, _, _ = status_line.split(b" ", 2)
    status_code = int(status_code)

    # Handle HTTP response
    if status_code < 200:
        print("Informational response:")
        print(response.decode())
    elif status_code < 300:
        print("Successful response:")
        print(response.decode())
    elif status_code < 400:
        print("Redirection response:")
        print(response.decode())
    elif status_code < 
