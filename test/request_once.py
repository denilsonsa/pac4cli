# ----------------------------------------
# A small utility script do one HTTP request.
# It's essentially a version of netcat client.
# See also serve_once.py.
# ----------------------------------------

import socket
import sys

if __name__ == "__main__":
    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket()
    s.connect((host, port))

    data = sys.stdin.buffer.read()
    data = data.replace(b"\n", b"\r\n")
    s.sendall(data)

    sys.stdout.buffer.write(s.recv(4096))
    s.close()
