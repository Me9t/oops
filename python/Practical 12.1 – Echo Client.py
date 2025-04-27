import socket

def start_client():
    with socket.socket() as client_socket:
        client_socket.connect(('localhost', 9999))
        print("Connected to Echo Server")
        
        while True:
            message = input("Enter message (or 'exit' to quit): ")
            client_socket.send(message.encode())
            
            if message.lower() == 'exit':
                break
                
            response = client_socket.recv(1024).decode()
            print(f"Server echoed: {response}")

if __name__ == "__main__":
    start_client()
