from ult.ServerAct import *
from socket import *
import re

if __name__ == "__main__":
	sock = socket(AF_INET, SOCK_DGRAM)
	sock.bind(('0.0.0.0', 10000))

	try:		
		while True:
			print('Wait next request...')

			info, addr = sock.recvfrom(MSGLEN)
			handle_request(sock, info, addr)

	except OSError as Err:
		print('OSError!', Err)

	sock.close()