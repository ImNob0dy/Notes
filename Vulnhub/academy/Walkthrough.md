
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







