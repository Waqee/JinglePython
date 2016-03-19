# JinglePython

A simple implementation of P2P Messaging between 2 peers negotiated by a Jingle session over Raw UDP Transport (To be changed to ICE-UDP in Light Melody)

See The Node1Output.txt and Node2Output.txt for a sample running overview

#Overview

1. Node1: Acts as Initiator with jid: Node1@example.com/orchard
2. Node2: Acts as Responder with jid: Node2@example.com/balcony
3. Jingle: Class for creating xmpp messages and extracting addresses
4. Node1Output.txt and Node2Output.txt Overview of the connection phases

#Running

1. Install xmpppy using sudo apt-get install python-xmpp
2. Change ip, port and jids to your own configuration (I'm using prosody with accounts named as described in overview)
3. Run Node2.py, then Node1.py

#Contributors

MySelf

#License

Open Source. MIT License

