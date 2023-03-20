import string


def encrypt(message, shift):
    alphabet = list(string.ascii_lowercase)
    encrypted_message = []

    for letter in message.lower():
        try:
            if alphabet.index(letter) + shift < len(alphabet) - 1:
                encrypted_message.append(alphabet[alphabet.index(letter) + shift])
            else:
                encrypted_message.append(alphabet[alphabet.index(letter) + shift - 26])
        except ValueError:
            encrypted_message.append(letter)

    return ''.join(encrypted_message)
