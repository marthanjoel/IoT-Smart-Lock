import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.3.233', 10000)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Establish connection with client.
    c, (client_host, client_port) = sock.accept()
    print 'Got connection from', client_host, client_port
    #c.send('Server Online\n') # This is invalid HTTP header
    c.recv(1000) # should receive request from client. (GET ....)
    c.send('HTTP/1.0 200 OK\n')
    c.send('Content-Type: text/html\n')
    c.send('\n') # header and body should be separated by additional newline
    c.send("""
        <html>
        <body>
        <button>Hello</button> this is my server!
        </body>
        </html>
    """) # Use triple-quote string.
    c.close()