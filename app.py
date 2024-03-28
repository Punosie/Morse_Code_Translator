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
    code_in += ' '
    decrypted_msg = ''
    morse_char = ''
    inv_morse_dict = {v: k for k, v in mcd.items()}
    space_count = 0
    for char in code_in:
        if char != ' ':
            morse_char += char
            space_count = 0
        else:
            space_count += 1
            if space_count == 2:
                decrypted_msg += ' '
            else:
                decrypted_msg += inv_morse_dict.get(morse_char, '')
                morse_char = ''
    
    return decrypted_msg