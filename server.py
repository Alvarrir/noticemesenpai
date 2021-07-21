import socket
import os
import time

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
    answer = string.encode() + b'f1n1sh'

listening_socket = socket.socket()

listening_socket.bind(('127.0.0.1', 6677))

listening_socket.listen()

game_socket, addr = listening_socket.accept()

max_score = len(answer)

score =0

while True:
    
    game_socket.sendall(answer)

    data = b''
    
    while b'f1n1sh' not in data:
        
        data += game_socket.recv(1024)

    data = data[:data.find(b'f1n1sh')].decode()

    for index in range(len(answer)):
        
        try:
            
            if data[index] == answer[index]:
                
                score += 1

        except:
            
            score += 0

    print("SCORE: ", score)
    
    print("MAX SCORE: ", max_score)
    
    result = score/max_score

    result = f'{result:.2f}'
    
    print("RESULT:", result)

    game_socket.sendall(result.encode() + b'f1n1sh')

    break

game_socket.close()

listening_socket.close()
