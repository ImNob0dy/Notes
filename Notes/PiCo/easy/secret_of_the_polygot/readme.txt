In this picoCTF challenge we have a file called "flag2of2-final.pdf"

Check the file metadata using 
exiftool (I got nothing)

I've tried couple of commands. I finally found using "file" command that this
.pdf have an image kind of data

Now convert the file into .png format

command: mv flag2of2-final.pdf flag2of2-final.png

Now you can see the half part of flag in img format and other half in pdf 
format.
