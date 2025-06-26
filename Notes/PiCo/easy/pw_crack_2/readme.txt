In this challenge we need to study the python code

Download the two files and save them in the same folder because the flag need to be decoded by the .py file.

Now look into the code. We can see that a password is required to decrypt the flag.

In the code we can see that the password is being compared with some hexadecimal forms. Look carefully we are using a method called type casting.

Try to convert the hexadecimal values into char values 

Note ---> chr(0x34) ... convert these values into chracters we will get the password.
Now run the code and give the obtained password. 

We get the flag.


