MODE_ENCRYPT = 1
MODE_DECRYPT = 0

def cipher(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data
	
input(" escolha um intervalo: ")
input("escreva uma frase: ")

ciphered = cipher(input, key, MODE_ENCRYPT)
print('Encriptada:', ciphered)
plain = cipher(ciphered, key, MODE_DECRYPT)
print('Decriptada:', plain)


