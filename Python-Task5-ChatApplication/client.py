import socket
import threading

HOST = "127.0.0.1"
PORT = 12345


def receive_messages(client):
    """Receive and display messages from the server."""
    while True:
        try:
            message = client.recv(4096)

            if not message:
                print("\nDisconnected from the server.")
                break

            text = message.decode("utf-8")
            print(text, end="", flush=True)

            if "Enter your username:" in text:
                continue

            if not text.endswith("\n"):
                print()

        except (ConnectionError, OSError):
            print("\nConnection closed.")
            break


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        print("Connected to the Python Chat Application!")
        print("Type /quit to leave the chat.\n")

        receiver = threading.Thread(
            target=receive_messages,
            args=(client,),
            daemon=True
        )
        receiver.start()

        while True:
            message = input()

            if message.strip().lower() == "/quit":
                client.sendall(b"/quit")
                break

            client.sendall(message.encode("utf-8"))

    except ConnectionRefusedError:
        print("Cannot connect. Please start server.py first.")
    except (ConnectionError, OSError):
        print("Connection lost. Please try again.")
    except KeyboardInterrupt:
        print("\nLeaving the chat...")
    finally:
        client.close()


if __name__ == "__main__":
    start_client()