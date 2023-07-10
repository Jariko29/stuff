import socket

def retrieve(host,name):
    mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysocket.connect((host,80))
    cmd = f'GET http://{host}/{name} HTTP/1.0\r\n\r\n'.encode()
    cmd = mysocket.send(cmd)
    
    info = b''
    while True:
        data = mysocket.recv(4096)
        if not data:
            break
        info += data
    return info.decode()
    
name = 'intro-short.txt'
host = 'data.pr4e.org'
Data = retrieve(host,name)
print(Data)

quit()
