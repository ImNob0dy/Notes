Hashcat is the world’s fastest CPU-based password recovery tool. While it's not as fast as its GPU counterpart oclHashcat, large lists can be easily split in half with a good dictionary and a bit of knowledge of the command switches. Hashcat is the self-proclaimed world’s fastest CPU-based password recovery tool, Examples of  hashcat  supported hashing algorithms are Microsoft LM Hashes, MD4, MD5, SHA-family, Unix Crypt formats, MySQL, Cisco PIX.

Hashcat works by:

1. **Loading the hash(es)** to be cracked.
2. **Selecting an attack mode** (e.g., brute force, dictionary, rule-based).
3. **Using a hash algorithm** (e.g., MD5, SHA-256, bcrypt).
4. **Iteratively testing password candidates** against the hash(es) until a match is found.

**Syntax**:
	 `hashcat [options] [hash_file] [wordlist/mask]`
	 
### **Common Options**

- `-a`: Specifies the **attack mode**:
    
    - `0`: Dictionary attack.
    - `1`: Combination attack.
    - `3`: Mask attack.
    - `6`: Hybrid attack (dictionary + mask).
    - `7`: Hybrid attack (mask + dictionary).
- `-m`: Specifies the hash type (e.g., `0` for MD5, `1000` for NTLM, `1800` for SHA-512).
    
- `-o`: Specifies the output file for cracked passwords.
    
- `--show`: Displays previously cracked passwords for a hash file.
    
- `--session`: Saves or resumes a cracking session.
    
- `--help`: Displays help information.

**Dictionary Attack**
	`hashcat -a 0 -m 0 hashes.txt wordlist.txt`
**Mask Attack (Brute Force)**
	`hashcat -a 3 -m 1000 hashes.txt ?u?l?l?l?l?d?d`
**Combination Attack**
	`hashcat -a 1 -m 0 hashes.txt wordlist1.txt wordlist2.txt`
**Show Cracked Passwords**
	`hashcat --show -m 0 hashes.txt`


