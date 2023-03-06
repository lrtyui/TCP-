import socket
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
s.bind(('',8080))
s.listen(5)
print('Waiting for connection...')

while True:
    sock,addr = s.accept()
    print('Accept new connection from %s:%s...' % addr)
    count=0
    if count == 0:
        data1 = sock.recv(1024)
        print(str(data1))
        file_total_size = int(data1.decode())
        received_size = 0
        sock.send('received'.encode(encoding="utf-8"))
        data = sock.recv(1024)
        filepath = str(data.decode(encoding="utf-8"))
        f = open(filepath, 'wb')
    while received_size < file_total_size:
        data = sock.recv(1024)
        f.write(data)
        received_size += len(data)
        print('已接收 ',received_size,' Byte')
    data = sock.recv(1024)
    if data == b'end':
        break
        
f.close()
s.close()
