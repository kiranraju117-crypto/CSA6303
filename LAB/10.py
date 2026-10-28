connections = []

def outbound():
    connections.append("WebServer")
    print("Outbound connection allowed")

def inbound(source):
    if source in connections:
        print("Return traffic allowed")
    else:
        print("Inbound traffic blocked")

outbound()
inbound("WebServer")
inbound("UnknownHost")