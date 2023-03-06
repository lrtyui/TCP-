import socket
tcp_clint=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_clint.connect(("47.113.217.150",8080))
send="hello world"
data=send.encode(encoding="utf-8")
tcp_clint.send(data)
rev_data=tcp_clint.recv(1024)
rev_connect=rev_data.decode(encoding="utf-8")
print("接受的数据为:",rev_connect)
tcp_clint.close()
# if __name__=="_main_":0
    