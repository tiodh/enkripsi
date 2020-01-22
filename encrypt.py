message = input('Input Message: ')

chipper = ''
for alphabet in message:
	temp = ord(alphabet)+1
	chipper += chr(temp)

print(chipper)
