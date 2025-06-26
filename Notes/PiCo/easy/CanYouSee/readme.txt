In this challeng we need to find the hidden flag in the .jpeg file.

TO do that download the file "unknow.zip"

Extract the file using the following command

>> unzip unknown.zip

Afte extracting the file check for the metadata of the file.

Use the tool called stegoveritas.
 
Use the tool with the following options to get the information

>> stegoveritas -exif  or stegoveritas -xmp to get the metadata.

Now we can observe "| AttributionURL      | cGljb0NURntNRTc0RDQ3QV9ISUREM05fZDhjMzgxZmR9Cg== |"

Now look at the abotained attributeurl. It looks like base64.

Decode it using base64 decoder.

We get the flag.
