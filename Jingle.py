import xmpp

class Jingle:
    @staticmethod
    def jingleInit(frm, to, ip, port):
        message = xmpp.Iq(None, None, {'type' : 'set'}, to, frm)
        jingle = message.addChild('jingle', namespace='urn:xmpp:jingle:1')
        jingle.setAttr('action', 'session-initiate')
        jingle.setAttr('initiator', frm)
        jingle.setAttr('sid', 'a73sjjvkla37jfea')
        content = jingle.addChild('content')
        content.setAttr('creator', 'initiator')
        content.setAttr('name', 'xmlstream')
        content.addChild('description', namespace='urn:xmpp:jingle:apps:xmlstream:0')
        transport = content.addChild('transport', namespace='urn:xmpp:jingle:transports:raw-udp:1')
        candidate = transport.addChild('candidate')
        candidate.setAttr('component', '1')
        candidate.setAttr('generation', '0')
        candidate.setAttr('id', 'a9j3mnbtu1')
        candidate.setAttr('ip', ip)
        candidate.setAttr('port', port)
        return message

    @staticmethod
    def jingleResp(frm, to, ip, port):
        message = xmpp.Iq(None, None, {'type' : 'set'}, to, frm)
        jingle = message.addChild('jingle', namespace='urn:xmpp:jingle:1')
        jingle.setAttr('action', 'session-accept')
        jingle.setAttr('initiator', to)
        jingle.setAttr('responder', frm)
        jingle.setAttr('sid', 'a73sjjvkla37jfea')
        content = jingle.addChild('content')
        content.setAttr('creator', 'initiator')
        content.setAttr('name', 'xmlstream')
        content.addChild('description', namespace='urn:xmpp:jingle:apps:xmlstream:0')
        transport = content.addChild('transport', namespace='urn:xmpp:jingle:transports:raw-udp:1')
        candidate = transport.addChild('candidate')
        candidate.setAttr('component', '1')
        candidate.setAttr('generation', '0')
        candidate.setAttr('id', 'a9j3mnbtu1')
        candidate.setAttr('ip', ip)
        candidate.setAttr('port', port)
        return message

    @staticmethod
    def GetCandidateAddress(mess):
        candidate = mess.getTag('jingle').getTag('content').getTag('transport').getTag('candidate')
        address = (candidate.getAttr('ip'), int(candidate.getAttr('port')))
        return address
