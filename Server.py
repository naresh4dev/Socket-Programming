from socket import *
def starter():
    c1, addr1 = globals()['s'].accept()
    c1.send(bytes('Welcome to Messenger \nPlease Wait a moment ', 'utf-8'))
    name1 = c1.recv(1024).decode()
    print('Connected with', addr1, '\nName:', name1)
    c2, addr2 = globals()['s'].accept()
    c2.send(bytes('Welcome to Messenger', 'utf-8'))
    name2 = c2.recv(1024).decode()
    print('Connected with', addr2, '\nName:', name2)
    c1.send(bytes(name2, 'utf-8'))
    c2.send(bytes(name1, 'utf-8'))
    i1=c1.recv(1024).decode()
    i2=c2.recv(1024).decode()
    i1,i2=int(i1),int(i2)
    i=(i1+i2)//2
    s1=str(i)
    c1.send(bytes(s1,'utf-8'))
    c2.send(bytes(s1,'utf-8'))
    return c1,c2,i,name1,name2
def rec(c1,c2):
    op=''
    op1=c1.recv(1024).decode()
    op2=c2.recv(1024).decode()
    if op1=='1' and op2=='1':
        op='Same'
    elif op1=='2' and op2=='2':
        op='Same'
    elif op1=='1'and op2=='2':
        op='SR'
    elif op1=='2' and op2=='1':
        op='RS'
    return op
def Client(a,b):
    a.send(bytes('S','utf-8'))
    b.send(bytes('R','utf-8'))
def receiver(a,b,name):
    msg=b.recv(1024).decode()
    print(name,':',msg)
    a.send(bytes(name,'utf-8'))
    a.send(bytes(msg,'utf-8'))
def Sender(a,b,name):
    msg=a.recv(1024).decode()
    print(name,':',msg)
    b.send(bytes(name,'utf-8'))
    b.send(bytes(msg,'utf-8'))
def end(c1,c2):
    c1.send(bytes('Chat Ended By Server\nVisit again','utf-8'))
    c1.close()
    c2.send(bytes('Chat Ended By Server\nVisit again','utf-8'))
    c2.close()
s=socket()
s.bind(('localhost',9999))
s.listen(3)
print('Host Created\nwaiting for connections')
while True:
    c1,c2,iter,n1,n2=starter()
    op=rec(c1,c2)
    if op=='Same':
        c1.send(bytes(op,'utf-8'))
        c2.send(bytes(op,'utf-8'))
        end(c1,c2)
        break
    elif op=='SR':
        Client(c1,c2)
        print('Chating Info')
        for i in range(iter):
            Sender(c1,c2,n1)
            receiver(c1,c2,n2)
    elif op=='RS':
        Client(c2,c1)
        print('Chating Info')
        for i in range(iter):
            Sender(c2,c1,n2)
            receiver(c2,c1,n1)

    end(c1,c2)
    break
print('Over')