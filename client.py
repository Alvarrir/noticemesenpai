import socket
import time
import os

print("AVAILABLE GAME MODES:")
print("1. EASY")
print("2. MEDIUM [NOT IMPLEMENTED]")
print("3. DIFFICULT [NOT IMPLEMENTED]")
print("4. SKIRMISH [NOT IMPLEMETED]")

modes = ["1", "2", "3", "4"]

ingame = False

mode = str(input("ENTER GAME MODE (1,2,3,4): "))

if mode in modes:
    ingame = True

address = str(input("ENTER IPV4 ADDRESS: "))
port = int(input("ENTER PORT NUMBER: "))

game_socket = socket.socket()

game_socket.connect((address, port))

while ingame:
    
    data = b''
    while b'/end' not in data:
        data += game_socket.recv(1024)
    data = data[:data.find(b'/end')].decode()
    string = ''
    for i in data:
        string += i

    print(string)
    
    start = time.time()

    temp_file = open('temp.txt','w')
    os.startfile('temp.txt')
    temp_file.close()
    while True:
        filesize = os.path.getsize("temp.txt")
        if filesize > 0:
            print("The file is not empty: " + str(filesize))
            break
    temp_file = open('temp.txt','r')
    data = ''
    array = []
    for line in temp_file:
        array.append(line)
    string = ''
    for i in array:
        string += i
    data = string.encode() + b'/end'
    print(data)
    end = time.time()
    game_socket.sendall(data)

    data = b''

    while b'/end' not in data:

        data += game_socket.recv(1024)

    data = data[:data.find(b'/end')]
    print(data.decode())

print("TIME TAKEN:", start-end)

