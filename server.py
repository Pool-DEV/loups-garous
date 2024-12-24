#!/usr/bin/env python3

import socket 
import sys
import threading

def GetClientName(client):
    data = client.recv(1024).decode()
    if data.startswith("/name "):
        return data[6:]
    return None

def HandleClient(client):
    try:
        while True:
            data = client.recv(1024).decode()
            if not data:
                break
            client.send(f"Reçu: {data}".encode())
    except Exception as e:
        print(f"[ERREUR] {e}")
    finally:
        client.close()

def start_server(host='127.0.0.1', port=7777):
    players_names = {}
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"[DÉMARRAGE] Serveur démarré sur {host}:{port}")
    try:
        while True:
            # Accepter une nouvelle connexion
            client_socket, client_address = server_socket.accept()
            # Récupérer le nom du client
            client_name = GetClientName(client_socket)
            if client_name is None:
                print("[ERREUR] Nom du client invalide")
                client_socket.close()
                continue
            players_names[client_socket] = client_name
            print(f"[CONNEXION] Nom du client: {client_name}")
            # Envoyer un message de bienvenue
            client_socket.send(f"Bienvenue {client_name}!".encode())
            # Créer un thread pour gérer le client
            client_thread = threading.Thread(target=HandleClient, args=(client_socket,))
            client_thread.start()
    except Exception as e:
        print(f"[ERREUR] {e}")
    finally:
        server_socket.close()


if __name__ == "__main__":
    start_server()