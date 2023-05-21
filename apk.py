import socket

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
s.bind(("127.0.0.1", 5000))

# Listen for incoming connections
s.listen(5)

# Accept an incoming connection
conn, addr = s.accept()

# Get the username from the client
username = conn.recv(1024).decode("utf-8")

# Send a welcome message to the client
conn.send("Welcome to the chat room, {}!".format(username).encode("utf-8"))

# Start a loop to receive and send messages
while True:
    # Receive a message from the client
    message = conn.recv(1024).decode("utf-8")

    # Print the message to the console
    print(message)

    # Send a message back to the client
    conn.send("Your message was received!".encode("utf-8"))

# Close the connection
conn.close()