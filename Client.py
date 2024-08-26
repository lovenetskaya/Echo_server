import socket

def run_client():
    host = "localhost"
    port = 12345

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect((host, port))

    print(f"Подключено к серверу {host}:{port}")

    try:
        while True:
            msg = input("Введите сообщение для отправки на сервер: ")
            client_sock.send(msg.encode('utf-8'))

            # Получение данных от сервера
            server_response = client_sock.recv(1024)
            print(f"Ответ сервера: {server_response.decode('utf-8')}")

    except KeyboardInterrupt:
        print("\nСоединение с сервером прервано.")
        client_sock.close()

if __name__ == "__main__":
    run_client()
