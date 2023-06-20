import base64
def encrypt_file(input_file, output_file):
    with open(input_file, 'rb') as file:
        plain_text = file.read()

    encrypted_text = base64.b64encode(plain_text)

    with open(output_file, 'wb') as file:
        file.write(encrypted_text)

input_file = 'input.txt'
output_file = 'encrypted.txt'
encrypt_file(input_file, output_file)
print('Файл успешно зашифрован.')