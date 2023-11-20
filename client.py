import socket

#creating a socket, probably related to internet standard
#default socket types, does not required mostly
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#trying to connect to the server
HOST = 'paneah.ddns.net'
PORT = 1234
mysock.connect((HOST, PORT))
#changing Unicode(python) to UTF-8(compressed internet code)
cmd = 'GET /views/rest/1414 HTTP/1.1\r\n\r\n'.encode() #HTTP Get method
mysock.send(cmd) #sending the request

while True:
    data = mysock.recv(521) #recv >> take in the data until the number in the function is done
    if len(data) < 1: #breaks when there is no data 
        break
    print(data.decode(), end = '') #decoding the data as Unicode again and printing it 

mysock.close()