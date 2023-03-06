import socket
import threading
def start(ip_port,new_clint):
    print("ip和port",ip_port)
    while True:
        recv_data=new_clint.recv(1024)
        if recv_data:
            print("接收的数据长度为:",len(recv_data))
            recv_conect=recv_data.decode(encoding="utf-8")
            print("接受的数据：",recv_conect,ip_port)
            send_conect="数据已经接受成功"
            send_data=send_conect.encode(encoding="utf-8")
            new_clint.send(send_data)
        else:
            print("客户取消连接",ip_port)
            break
    new_clint.close()

if  __name__=='__main__':
    sever=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sever.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    sever.bind(("",8080))
    sever.listen(128)
    while True:
        new_clint,ip_port=sever.accept()
        sub=threading.Thread(target=start,args=(ip_port,new_clint))
        sub.setDaemon(True)
        sub.start()
    

