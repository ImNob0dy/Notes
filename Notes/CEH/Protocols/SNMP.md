 Here we’re going to take a look specifically at the enumeration of Simple Network Management Protocol (SNMP). This protocol is leveraged for monitoring all sorts of IP-capable components on a network, and is used across a wide variety of devices and operating systems.

# Tools used to Enumerate:
1. Nmap
2. snmp-check
3. Metasploit
# What to Enumerate:
1. Default UDP port used by SNMP.
2. Identify the processes running on the target machine using [[nmap]] scripts.
3. List valid community strings of the server using [[nmap]] scripts.
4. List valid community strings of the server using snmp_login [[Metasploit]] module.
5. List all the interfaces of the machine. Using appropriate [[nmap]] scripts.
	To use the nmap scripts for SNMP protocol:
		`Command`: `sudo nmap -p- <snmp port> --script=snmp* <target ip> `
		The above command uses * (WildCard).
	