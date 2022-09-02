from encrypt import encrypt

to_encrypt = input("Enter the string that you want to encrypt: ")
keymap_path = input("Enter the absolute path of the keymap: ")
encrypted = encrypt(to_encrypt, keymap_path)

print(f"Here is the encrypted string: {encrypted}")
