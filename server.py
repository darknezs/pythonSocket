import socket

serverIP = '192.x.x.x' #ip
port = 5000

while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    server.bind((serverIP, port))
    server.listen(1)

    print('[x] Waiting [x]')

    client, addr = server.accept()
    print('connect from:', str(addr))

    data = client.recv(1024).decode('utf-8')
    print('message from client:', data)

    rep_text = 'we get the message'

    client.send(rep_text.encode('utf-8'))
    client.close()
