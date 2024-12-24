import socket
import sys

if len(sys.argv) != 2:
    print("Usage: python client.py <name>")
    sys.exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 7777

try:
    s.connect((host, port))

    s.send(f"/name {sys.argv[1]}".encode())

    line = sys.stdin.readline().strip()

    while line:
        s.send(line.encode())
        data = s.recv(1024)
        print(data.decode(), end='')
        line = sys.stdin.readline().strip()

except Exception as e:
    print(f"Connection error: {e}")

finally:
    s.close()
