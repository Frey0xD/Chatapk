import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.bind(("127.0.0.1", 5000))

sten for incoming connectionss.listen(5)


conn, addr = s.accept()


username = conn.recv(1024).decode("utf-8")


conn.send("Welcome to the chat room, {}!".format(username).encode("utf-8"))


while True:

    message = conn.recv(1024).decode("utf-8")

    
    print(message)

    conn.send("Your message was received!".encode("utf-8"))


conn.close()
