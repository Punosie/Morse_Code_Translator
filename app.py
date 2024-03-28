from const import MORSE_CODE_DICT as mcd

def encrypt(code_in):
    encrypted_msg = ''
    for char in code_in:
        if char.upper() in mcd:
            encrypted_msg += mcd[char.upper()] + ' '
        elif char == ' ':
            encrypted_msg += ' '

    print(encrypted_msg.strip())
    return encrypted_msg.strip()


def decrypt(code_in):
    pass

def converter():
    pass

encrypt('Hello')