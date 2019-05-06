
def encrypt(plaintext, k):
	str_out = ''

	for c in plaintext:
		str_out += chr((ord(c) - ord('A') + k)%26 + ord('A')) 
	
	return str_out
		
def decrypt(ciphertext, k):
	str_out = ''

	for c in ciphertext:
		str_out += chr((ord(c) - ord('A') - k)%26 + ord('A')) 
	
	return str_out

	
plaintext = input('Insert plaintext(Only capital): ')
k = int(input('Insert the shift value(Default 3): ') or '3')

cipher = encrypt(plaintext, k)
print('Ciphertext: ', cipher)
print('PlainText: ', decrypt(cipher, k))