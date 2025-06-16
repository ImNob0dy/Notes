ADB: Used to connect to the android devices.
	`Command: adb connect <IP address of the device>`
	`To get the shell: adb shell`
	To download any required file: `adb pull <path of the file> <path of the location where you want to download>`

WPScan: This is a tool used to find the vulnerabilities and enumerate the website (mainly
	    wordpress). Look into the man page and --help/-h.
		`Syntax: wpscan --url <website url> <options>`

SQLMap: This is a tool to perform a SQL injection on a vulnerable website. Look for the point to 
        perform the injection attack.
		`Command: **sqlmap -u <website url> –dbs** `
				`**sqlmap -u <website url> --current-db**`
				`**sqlmap -u <website url> -D <database name> –tables`

Privilege Escalation: This is the method which is used to gain the root access.
	`Step-1: Connect via ssh to the machine.
	
	`Note: To find the sudo privileges for all the users on the machine we need to       used "sudo -l"`
	
	`If the user dosen't have the pssword to spinup the /bin/bash------we can use   
	the following command --- "sudo -u <user name> /bin/bash"`
	
	`Look for the loop hole. Try to access the root directory. 
	If we have a change we can use "SSH id_rsa"`
	
		`Create file and copy the id_rsa value`
		 `Commands: chmod 600 id_rsa, ssh -i id_rsa root@<ip address> -p <port 
					number>`


RAT: 
	Look for the following obstacles.
		1. Which machine to target?
		2. What if it says no active connections?
	Tools:
		1. njRAT
		2. MoSucker
		3. ProRat (We need password)
		4. Theef
		5. HTTP RAT


Nikto:
		`nikto -h <url>`
		This is used to find the further directories and documents on the web site `nikto -h <url> -id <username:password>`


Hashing:
	Tools:
		`hash-identifier`
		`hashid`  ----> `hashid -m -j '48bb6e862e54f2a795ffc4e541caed4d'`
		`HashTag` ----> `python HashTag.py -sh '48bb6e862e54f2a795ffc4e541caed4d'`
		 Link ---> [https://github.com/SmeegeSec/HashTag](https://github.com/SmeegeSec/HashTag)
		`unshadow`
		`haiti`  ----> https://noraj.github.io/haiti/#/pages/install
		`wordlistctl` ---> This tool is used to find the best wordlists. We can search locally and online.
			Example syntax:
					`wordlistctl search rockyou`
					`wordlistctl fetch -l rockyou`
					`wordlistctl search -l rockyou`
					`wordlistctl fetch -l rockyou -d`
					`wordlistctl search facebook`
					`wordlistctl list -g fuzzing`
	**CeWl**
		It could be useful to retrieve a lot of words related to the password's topic. This is used to download all the password related topics from a website.
		`cewl -d 2 -w $(pwd)/example.txt https://example.org`
	Online:
		https://www.onlinehashcrack.com/
		https://crackstation.net/
		https://simplycalc.com/crc32-file.php
		https://www.devglan.com/online-tools/encrypt-decrypt-image-free

openSSL:
	openssl enc -d -aes-256-cbc -in encrypted_file -out decrypted_file -k "your_password"


		 

