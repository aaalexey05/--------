import pyAesCrypt

password = input("Введите пароль для шифрования файла: ")

#encrypt
pyAesCrypt.encryptFile('password.json', 'password.json.aes', password)

#decrypt
pyAesCrypt.decryptFile('password.json.aes', 'password1.json', password)