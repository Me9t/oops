import socket

def start_reverse_server():
    with socket.socket() as server_socket:
        server_socket.bind(('localhost', 9997))
        server_socket.listen(1)
        print("Reverse Number Server listening on port 9997...")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024).decode()
                if not data or data.lower() == 'exit':
                    break
                
                if data.isdigit():
                    reversed_num = data[::-1]
                    conn.send(reversed_num.encode())
                else:
                    conn.send(b"Invalid input. Send a number.")
            print("Connection closed")

if __name__ == "__main__":
    start_reverse_server()
