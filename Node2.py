import xmpp, Jingle, socket

username = 'node2'
password = '12'
to = 'node1@example.com/orchard'
frm = 'node2@example.com/balcony'
ip = 'localhost'
port = '13550'

myAddress = (ip, int(port))
Node1Address = None

file = open("Node2Output.txt", "w")

file.write('Starting Jingle Negotiation as Responder\n\n\n')

def messageCB(conn,mess):
    if mess.getTagAttr('jingle', 'action') == 'session-initiate' and mess.getTag('error') == None:
        file.write('Received Session Initiate:-\n')
        file.write(mess.__str__(1))

        Node1Address = Jingle.Jingle.GetCandidateAddress(mess)
        file.write('\n\nExtracted Other peers address: ')
        file.write(str(Node1Address))

        
        message = Jingle.Jingle.jingleResp(frm, to, ip, port)
        conn.send(message)
        file.write('\n\n\nSent Session Accept:-\n')
        file.write(message.__str__(1))

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        file.write('\n\nStarting direct p2p link\n\n')
        sock.bind(myAddress)

        data, address = sock.recvfrom(4096)
        file.write('Recieved ' + data + ' from other peer\n\n')

        sock.sendto('Node2', Node1Address)
        file.write('Sent Node2 to other peer\n')

        file.close()

        exit()

        

def StepOn(conn):
    try:
        conn.Process(1)
    except KeyboardInterrupt: return 0
    return 1

def GoOn(conn):
    while StepOn(conn): pass

conn = xmpp.Client('example.com')
conn.connect(server=('localhost',5222))
conn.auth(username, password, 'balcony')
conn.RegisterHandler('iq',messageCB)
conn.sendInitPresence()

GoOn(conn)


