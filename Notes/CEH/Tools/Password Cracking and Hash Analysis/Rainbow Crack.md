**RainbowCrack** is a tool used to crack hashed passwords by utilizing **rainbow tables**. Instead of brute-forcing or dictionary attacks, RainbowCrack precomputes hash values for a large set of possible passwords and stores them in rainbow tables. This method makes password cracking much faster, as it eliminates the need to compute hashes on the fly.

### **Using RainbowCrack**

#### **1. Precompute Rainbow Tables**

Use the RainbowCrack utility or third-party tools to generate tables:
	`rtgen <hash_type> <charset> <min_length> <max_length> <table_index> <chain_length>`
Example:
	`rtgen md5 lowercase 1 7 0 2000`

This generates a rainbow table for MD5 hashes using lowercase letters, with passwords between 1 and 7 characters long.
#### **2. Sort the Rainbow Tables**

After generating tables, sort them for optimal use:
	`rtsort <table_file>`
#### **3. Crack the Hash**

Once you have the rainbow table, use RainbowCrack to crack the hash:
	`rcrack <table_file> -h <hash>`

Example:
	`rcrack ./tables/ -h 5d41402abc4b2a76b9719d911017c592`

This cracks the MD5 hash for "hello".

---
### **Popular Rainbow Table Hash Types**

- MD5
- SHA-1
- NTLM