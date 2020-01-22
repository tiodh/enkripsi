chipper = input('Input Message: ')

plain = ''
for alphabet in chipper:
	temp = ord(alphabet)-1
	plain += chr(temp)

print(plain)
