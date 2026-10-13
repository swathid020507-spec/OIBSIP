import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

clients = {}
clients_lock = threading.Lock()


def broadcast(message, sender=None):
    """Send a message to every connected client."""
    with clients_lock:
        recipients = list(clients.keys())

    for client in recipients:
        if client == sender:
            continue

        try:
            client.sendall(message.encode("utf-8"))
        except OSError:
            remove_client(client)


def remove_client(client):
    """Remove a disconnected client safely."""
    with clients_lock:
        username = clients.pop(client, None)

    if username:
        print(f"{username} disconnected.")
        broadcast(f"[System] {username} left the chat.")

    try:
        client.close()
    except OSError:
        pass


def handle_client(client):
    """Receive messages from one client."""
    try:
        client.sendall(b"Enter your username: ")
        username = client.recv(1024).decode("utf-8").strip()

        if not username:
            username = "Guest"

        with clients_lock:
            clients[client] = username

        print(f"{username} connected.")
        client.sendall(
            f"[System] Welcome, {username}! You are connected.\n".encode("utf-8")
        )
        broadcast(f"[System] {username} joined the chat.", sender=client)

        while True:
            data = client.recv(4096)

            if not data:
                break

            message = data.decode("utf-8").strip()

            if message.lower() == "/quit":
                break

            if message:
                print(f"{username}: {message}")
                broadcast(f"{username}: {message}", sender=client)

    except (ConnectionError, OSError):
        pass
    finally:
        remove_client(client)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind((HOST, PORT))
        server.listen()

        print("=" * 40)
        print("       PYTHON CHAT SERVER")
        print("=" * 40)
        print(f"Server running at {HOST}:{PORT}")
        print("Waiting for clients...")

        while True:
            client, address = server.accept()
            print(f"Connection received from {address}")

            thread = threading.Thread(
                target=handle_client,
                args=(client,),
                daemon=True
            )
            thread.start()

    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server.close()

        with clients_lock:
            connected_clients = list(clients.keys())

        for client in connected_clients:
            remove_client(client)


if __name__ == "__main__":
    start_server()