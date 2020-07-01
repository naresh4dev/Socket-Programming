from socket import *


def chat(c):
    ch = input('How many Converstation Do you want to Make')
    c.send(bytes(ch, 'utf-8'))
    m = c.recv(1024).decode()
    n = int(m)
    return n
def sender(c):
    msg = input('Enter a message')
    c.send(bytes(msg, 'utf-8'))
    print('Sended......')


def receiver(c):
    print('Waiting for reply......')
    print(c.recv(1024).decode(),':',c.recv(1024).decode())


def option(c):
    try:
        print('1.Send First\n 2.Receive First')
        op = int(input('Please enter you Choice'))
    except ValueError:
        print('Please enter your choice in INTEGER')
        la= int(input('Enter here'))
        op=la
    except Exception:
        print('Something Went Wrong......\nPlease Rerun your Program')
    finally:
        o=str(op)
        c.send(bytes(o, 'utf-8'))

def rec(c):
    ch = c.recv(1024).decode()
    return ch



c = socket()
c.connect(('localhost', 9999))#Please Enter IP address instead of 'localhost' to connect with Server
print('Connected With Server')
name = input('Enter your Name')
c.send(bytes(name, 'utf-8'))
print(c.recv(1024).decode())
name = c.recv(1024).decode()
print('Online:', name)
n = chat(c)
option(c)
ch = rec(c)
if ch == 'Same':
    print('You entered the Same input as your Partner')
    print('Please Rerun the Program and Enter the Alternative Input')
else:
    if ch == 'S' or ch == 's':
        for i in range(n):
            sender(c)
            receiver(c)
    elif ch == 'R' or ch == 'r':
        for i in range(n):
            receiver(c)
            sender(c)
print(c.recv(1024).decode())
