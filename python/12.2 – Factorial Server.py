import socket
import math

def start_factorial_server():
    with socket.socket() as server_socket:
        server_socket.bind(('localhost', 9998))
        server_socket.listen(1)
        print("Factorial Server listening on port 9998...")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024).decode()
                if not data or data.lower() == 'exit':
                    break
                
                try:
                    num = int(data)
                    result = math.factorial(num)
                    conn.send(str(result).encode())
                except ValueError:
                    conn.send(b"Invalid input. Send a number.")
            print("Connection closed")

if __name__ == "__main__":
    start_factorial_server()
