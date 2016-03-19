import xmpp, Jingle, socket

username = 'node1'
password = '12'
to = 'node2@example.com/balcony'
frm = 'node1@example.com/orchard'
ip = 'localhost'
port = '13540'

myAddress = (ip, int(port))
Node2Address = None

file = open("Node1Output.txt", "w")

file.write('Starting Jingle Negotiation as Initiator\n\n\n')

def messageCB(conn,mess):
    if mess.getTagAttr('jingle', 'action') == 'session-accept' and mess.getTag('error') == None:
        file.write('\n\nReceived Session Accept:-\n')
        file.write(mess.__str__(1))

        Node2Address = Jingle.Jingle.GetCandidateAddress(mess)
        file.write('\n\nExtracted Other peers address: ')
        file.write(str(Node2Address))

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        file.write('\n\nStarting direct p2p link\n\n')
        sock.bind(myAddress)
        
        sock.sendto('Node1', Node2Address)
        file.write('Sent Node1 to other peer\n\n')

        data, address = sock.recvfrom(4096)
        file.write('Recieved ' + data + ' from other peer\n')

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
conn.auth(username, password, 'orchard')
conn.RegisterHandler('iq',messageCB)
conn.sendInitPresence()

message = Jingle.Jingle.jingleInit(frm, to, ip, port)
conn.send(message)
file.write('Sent Session Initiate:-\n')
file.write(message.__str__(1))

GoOn(conn)
