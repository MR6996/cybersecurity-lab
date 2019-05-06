import binascii

def encrypt(plaintext, k):
	str_out = ''
	k_len = len(k)
	
	for i in range(len(plaintext)):
		str_out += chr(ord(plaintext[i])^ord(k[i%k_len]))
		
	return str_out
		
def decrypt(ciphertext, k):
	str_out = ''
	k_len = len(k)
	
	for i in range(len(ciphertext)):
		str_out += chr(ord(ciphertext[i])^ord(k[i%k_len]))
	
	return str_out

	
plaintext = input('Insert plaintext: ')
k = input('Insert the password: ')

cipher = encrypt(plaintext, k)
print('Ciphertext: ', binascii.hexlify(bytes(cipher, 'utf-8')))
print('PlainText: ', decrypt(cipher, k))