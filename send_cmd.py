#! /usr/bin/env python

# The device that is running the subflow visualization must be on the same network as this sender,
# and must be reachable via UDP broadcast.

# Example usage:
# ./send_cmd.py "subflow24379;BPM:122:0;MOD:7:7;MOD:4:7;MOD:7:7;MOD:3:7;CST:0:7;LOP:2:2000;"

import sys
import socket


port  = 37020
magic = "subflow24379"
sendstr   = sys.argv[1]
print(sendstr)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.settimeout(1.0)
server.sendto(sendstr.encode('utf-8'), ('<broadcast>', port))

print("You should have seen the subflow screen flash briefly; if not, send again.")
print("To start this beat: Click UP on TV remote, or tap top of touchscreen.")
print("To pause: Click DOWN on TV remote or tap bottom of touchscreen.")
print("To unload sequence: Click DOWN or tap bottom while paused.")
