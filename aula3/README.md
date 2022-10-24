# Encrypting

`python3 cypher.py input/file encrypted/file aes mode`

# Decrypting

`python3 decrypter.py encrypted/file output/file aes mode`

# Visualize Encrypted Image

`cp encrypted/file.bmp encrypted/new_file.bmp`
`dd if=input/original_file.bmp of=encrypted/new_file.bmp ibs=1 count=54 conv=notrunc`