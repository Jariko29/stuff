import socket 

def search_engine(page_title,host):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((host,80))
    cmd = f"GET http://{host}{page_title} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    mysocket.send(cmd.encode())
    
    info = b''
    while(True):
        data = mysocket.recv(512)
        if not data:
            break
        info += data
    return info.decode()

page_title = 'intro-short.txt'
host_name = 'data.pr4e.org'
info = search_engine(page_title,host_name)
print(info)

quit()