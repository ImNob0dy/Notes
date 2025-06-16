### **List of tools for CEH**
### **Network Scanning and Enumeration**

1. [[netdiscover]]
2. [[Wireshark ]]or [[Tcpdump]]
3. [[nmap]]
4. [[Wpscan]]
5. [[ Nikto]]
6. [[Responder LLMNR]]

### **Password Cracking and Hash Analysis**

7. [[Hashcalc (Windows)]]   (Windows)
8. [[John]]
9. [[Hashcat]]
10. [[Hydra]]
11. [[Rainbow Crack]]
### **Exploitation Frameworks and Tools**

12. [[Metasploit]]
13. [[Sqlmap]]
14. [[Searchsploit]]

### **Web and Directory Analysis**

15. [[Dirb]]
16. [[ Cewl]]
17. [[Rockyou]] and [[SecList]]

### **Cryptography and Steganography**

18. [[VeraCrypt (windows)]]
19. [[BcTextEncoder (Windows)]]
20. [[cryptool (Windows)]]
21. [[snow (Windows)]]
22. [[Steghide]]
23. [[OpenStego (Windows)]]
24. [[ QuickStego]]
25. [[Covert TCP]]
26. [[Hashmyfiles (Windows)]]
27. [[CryptoForge (Windows)]]

### **Post-Exploitation and Privilege Escalation**

25. [[GTFOBINS]]
26. [[LinPeas]]
### **File and Data Forensics**

30. [[FTK Imager]]
31. [[ Malwoverview]]

### **System and File Utilities**

32. [[OleView]]
33. [[Dcomcnf]]
34. [[RpcDump]]
35. [[Gacutil]]

### **Other Specialized Tools**

36. [[Crunch (Password list generation)]]
37. [[Strings (Extracting readable text from binaries)]]
38. [[Aircrack-ng (Wireless security analysis)]]


--------------------------------------------------------------
**theHarvester** (This helps to find the personal details of a targeted website)
	Ex:  "theHarvester -d eccouncle.org -l 200 -b linkedin"


**sherlock**  - Find usernames across social networks
	sherlock relies on the site's designers providing a unique URL for a registered username. To determine if a username is available, Sherlock queries that URL, and uses to response to understand if there is a claimed username already there. Currently, the tool is capable of locating users on more than 300 social networks:	Apple Developer, Arduino, Docker Hub, GitHub, GitLab, Facebook, BitCoinForum, CNET, IFTTT, Instagram, PlayStore, PyPI, Scribd, Telegram,TikTok, Tinder etc.
	
		Command: python3 sherlock user123
				 python3 sherlock user1 user2 user3
Online Tools:
		followerwonk.com/

**Ping**:
	 This is a command which is used to check the connectivity with the target machine.
	 Basically sends ICMP packets and waits for the reply. 

	Command: ping <Taret Website>
	 ping <target website> -l <size>  "This is used to find the max size of a    
	                                packet "
	 ping <target website> -i <TTL> -n <number of echo requests> 
	 ping www.certifiedhacker.com -i 21 -n 1
**Photon**:
	 This is a python tool which is used to get all the info of the target site.
**Central Ops.net**:
	 This is an online tool which is similar to 'whois', Domain related, DNS information.


	
