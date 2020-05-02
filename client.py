import socket

serverIP = '192.x.x.x' #ip
port = 5000

while True:
    data = input('Send Message: ')
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    server.connect((serverIP, port))

    server.send(data.encode('utf-8'))

    data_server = server.recv(1024).decode('utf-8')
    print('Data from server: ', data_server)
    server.close()
