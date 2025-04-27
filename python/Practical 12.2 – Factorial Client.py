import socket

def factorial_client():
    with socket.socket() as client_socket:
        client_socket.connect(('localhost', 9998))
        print("Connected to Factorial Server")
        
        while True:
            num = input("Enter number (or 'exit' to quit): ")
            client_socket.send(num.encode())
            
            if num.lower() == 'exit':
                break
                
            response = client_socket.recv(1024).decode()
            print(f"Factorial: {response}")

if __name__ == "__main__":
    factorial_client()
