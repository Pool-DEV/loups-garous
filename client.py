import socket
import sys

if len(sys.argv) < 2:
    print("Usage: python client.py <name>")
    sys.exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 7777

try:
    s.connect((host, port))

    # Envoyer le nom du client
    name = ""
    for arg in sys.argv[1:]:
        name += arg + " "
    s.send(f"/name {name}".encode())
    data = s.recv(1024)
    print(data.decode())

    # Envoyer des données
    while True:
        message = input()
        s.send(message.encode())
        data = s.recv(1024)
        print(data.decode())

except Exception as e:
    print(f"Connection error: {e}")

finally:
    s.close()
