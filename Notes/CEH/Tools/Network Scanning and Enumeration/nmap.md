·       Scanning network **Live Hosts** (Ping Sweep)  --- ***nmap -sP IP/CIDR***

·       Scanning **Live Hosts** without port scan in Same subnet (ARP Scan)      --- 
    ***nmap -pr -sn  IP/CIDR***



·       **Scripts + Version** running on the target  machine     --- ***nmap -sC -sV IP/CIDR***


·       **OS** of the target                            --- *nmap -o IP*

·       All **open ports** of the target         --- *nmap -p- IP/CIDR*

·       **Specific port** scan of the target    --- ***nmap -p<port-number> IP/CIDR*

·       Aggressive Scan                            --- *nmap -A IP/CIDR*

·       Scanning using NSE scripts           ---  *nmap -scripts <script name> -p- IP/CIDR***

·       **Scripts + Version + Ports + OS* --- ***nmap -sC -sV -p- -A -T4 IP/CIDR***