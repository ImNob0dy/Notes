First to find the number hosts in the network we used the target Ip along with the wildcard.
	nmap 192.168.10.* <ip with the wildcard>
	Alternate 1      nmap 192.168.10.1/24 (Using CIDR notation)
	Alternate 2      nmap 192.168.10.1-256 (Using the range of hosts)
	Alternate 3      nmap -PR -sn 192.168.10.0/24 (Example Ip) ---> no need of root access.

- If we have many hosts available in the same subnet and we need to find the services and also the ports of all the hosts we can use  the command 
	  nmap -sC -sV -p- -T4 192.168.10.* -vv 
	  (or) 
	  nmap -sC -sV -p- 192.168.10.0/24 -T4 -vv
	  (or)
	  nmap -sC -sV -p- 192.168.10.1-256 -T4 -vv  (By default nmap uses stealth scan.) 


This phase starts with network scanning using [[nmap]]