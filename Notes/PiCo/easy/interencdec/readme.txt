In this picoCTF challenge we have a "enc_flage" file.

In this the flag is encrypted. By looking at the encrypted text we can see 
it is in base64 format. 
Because it is ending with "=="

Now decode it with base64. You still find that it is in base64.

Now decrypt the first result by base64 by removing the satrting b' and 
eding '.

You get something similar to the flag. Now try caesar cipher you wll get 
your flag.
