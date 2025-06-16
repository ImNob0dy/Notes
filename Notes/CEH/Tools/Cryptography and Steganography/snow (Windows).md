Snow is a tool used for **steganography**, the practice of hiding information within other data. It specifically hides messages within whitespace (spaces and tabs) in text files. The hidden information is encoded in the form of a message and is appended to the visible text file, making it hard to detect by casual inspection.

**Syntax**
		`snow -C -p <password> -f <file> -m <message> -o <output_file>`

**Hide a Message**:
		`snow -C -p secret123 -m "Hidden message" -f input.txt -o output.txt`

- `-C`: Compress the message before hiding.
- `-p`: Use "secret123" as the password.
- `-m`: The message to hide.
- `-f`: Input file to hide the message in.
- `-o`: Output file containing the steganographic data.

**Extract a Message:**
		`snow -C -p secret123 -f output.txt`

**Hiding the data:**
		`SNOW.EXE -C -m <secret message> -p <password> <original file > <output file>`

**Extracting the data:**
		`SNOW.EXE -C -p <password of the file> <file need to be exreacted>`



