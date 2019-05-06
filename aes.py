from Crypto.Cipher import AES

key = b'aaaabbbbccccdddd'
iv = b'0000111122223333'

def pkcs7(plaintext):
	padbytes = 16 - len(plaintext)%16
	return (plaintext + chr(padbytes)*padbytes).encode()

def enc(plaintext):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	return cipher.encrypt(pkcs7(plaintext))

def ispkcs7(plaintext):
	l = len(plaintext)
	c = ord(plaintext[l-1])                       
	if (c > 16) or (c < 1):
		return "PADDING ERROR"
	if plaintext[l-c:] != chr(c)*c:
		return "PADDING ERROR"
	return plaintext[:-c]
	
def decr(ciphertext):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	return ispkcs7(cipher.decrypt(ciphertext).decode())

	
c = enc('asdasd asdasd qweqweqweqweqweqweqweqweqweqwe')
print(c)
d = decr(c)
print(d)