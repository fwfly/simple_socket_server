import socket

def response(conn):
    #response_headers = {
    #    'Content-Type': 'text/html; encoding=utf8',
    #    'Content-Length': len(response_body_raw),
    #    'Connection': 'close',
    #}
    response_proto = 'HTTP/1.1'
    response_status = '200'
    response_status_text = 'OK'

    print "response OK"
    resmsg = "%s %s %s"% (response_proto, response_status, response_status_text)

    conn.send(resmsg)

def handleReq(conn):
    while True:
        print "----Recv data : "
        data = conn.recv(1024)
        print data
        if not data:
            break
    response(conn);
    conn.close()

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8008

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(10)

    while True:
        # bind socket
        conn, addr = server.accept()
        print 'COnnect with' + addr[0] + ","+ str(addr[1])

        # dump buffer
        handleReq(conn)

    server.close()
