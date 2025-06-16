John, better known as John the Ripper, is a tool  to find weak passwords of users in a server. John can use a dictionary or some search pattern as well as a password file to check for passwords. John supports different cracking modes  and  understands  many  ciphertext formats,  like  several  DES variants, MD5 and blowfish. It can also be used to extract AFS and Windows NT pass‐words.

 To use John, you just need to supply it a password file and the desired options. If no mode is  specified,  john will try "single" first, then "wordlist" and finally "incremental".

Once  John  finds  a password, it will be printed to the terminal and saved into a file called ~/.john/john.pot. John will read this file when it restarts so it doesn't try to crack already done passwords.
	To see the cracked passwords, use
       `john -show passwd`

**Important**: do this  under  the  same  directory  where  the  password  was  cracked  (when  using the  cronjob, /var/lib/john), otherwise it won't work.

To continue an interrupted session, run:
       `john -restore`

Syntax:
	 `john <options> <password_file>`
	 `john --wordlist=wordlist.txt hashes.txt` (With wordlist)
	 ex: `john --wordlist=/path/to/wordlist.txt /path/to/hashes.txt`
	 `john --wordlist=wordlist.txt --rules hashes.txt`
**Options**:
`--single`: Use single-crack mode, attempting simple variations of usernames and salts.
	`john --single hashes.txt`
	
`--incremental` or `-i`: Use incremental mode for brute-force attacks.
	`john --incremental hashes.txt`
	
`--show`: Display cracked passwords for the given hash file.
	`john --show hashes.txt`

`--format=<hash_type>`: Specify the hash type (e.g., `md5`, `sha256crypt`, `bcrypt`).
	`john --format=md5 hashes.txt`


**To decrypt ssh private keys:**
	`ssh2john <id_rsa_file/Private key file>`

	 `john <file> --wordlist=<path to the wordlins>`
		Ex: john rsa --wordlist=/home/kevin/rockyou.txt


