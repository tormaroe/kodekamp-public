from os import listdir
from subprocess import call

for x in listdir("answers"):
	
	print "-------------------------"
	print "*** Testing", x, "***"

	## Decryption
	call(["python", "answers/"+x, "d", "secret1.txt", "key1.1tp"])

	## Encryption
	call(["python", "answers/"+x, "e", "message1.txt", "key1.1tp"])

	print "-------------------------"
	print