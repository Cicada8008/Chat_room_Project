import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Fixed the case to AF_INET
client.connect(('127.0.0.1', 55555))

nickname = input("Choose a nickname: ")  # Add a way to set a nickname

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message) 
        except:
            print("An error occurred!!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))  # Fixed typo 'sed' -> 'send'

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)  # Fixed to call 'write' instead of 'receive'
write_thread.start()
