#### **Crack the Wireless Encryption**

1. **Navigate to the Capture File**:
    
    - Open a terminal and navigate to the `Documents` folder where the capture file is located:
        
        cd ~/Documents
        
2. **Identify the Target Network**:
    
    - Use `aircrack-ng` to analyze the capture file and identify the target network:
    
        `aircrack-ng W!F!_Pcap.cap`
        
    - Note the BSSID (MAC address) of the target network and the type of encryption (e.g., WEP, WPA/WPA2).
        
3. **Crack the Password**:
    
    - Use `aircrack-ng` with a wordlist to crack the password. Replace `<WORDLIST>` with the path to your wordlist (e.g., `rockyou.txt`):

        `aircrack-ng -w <WORDLIST> -b <BSSID> W!F!_Pcap.cap`
        
    - Example:
   
        `aircrack-ng -w /usr/share/wordlists/rockyou.txt -b 00:11:22:33:44:55 W!F!_Pcap.cap`
        
    - Once the password is cracked, note it down.
        
4. **Count the Password Characters**:
    
    - Count the number of characters in the cracked password:
 
        `echo -n "PASSWORD" | wc -c`
        
    - Replace `PASSWORD` with the actual password.

#### **2. Connect to the Rogue AP**

1. **Use `nmcli` or `wpa_supplicant`**:
    
    - Connect to the network using the cracked password. For example, using `nmcli`:

        `nmcli dev wifi connect <SSID> password <PASSWORD>`
        
    - Replace `<SSID>` with the network name and `<PASSWORD>` with the cracked password.