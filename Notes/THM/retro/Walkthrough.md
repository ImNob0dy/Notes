
In this I'm not able to perform ping  to the target machine.

So, used "nmap -Pn -p- -T4 -vv 10.10.X.X"
For more information look into nmap_scan.txt

This is a windows machine.

There are two open ports 80(http), 3389(RDP).

I performed a directory search using gobuster 

	```Command: gobuster dir -w /usr/share/wordlist/dirbuster/directory-2.3-medium.txt -u http://10.10.33.21/

Found the hidden directory /retro

After searching found an user name wade with a password 