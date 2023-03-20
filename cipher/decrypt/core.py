import string


def decrypt(message, shift):
    alphabet = list(string.ascii_lowercase)
    decrypted_message = []

    for letter in message.lower():
        try:
            if alphabet.index(letter) - shift < 0:
                decrypted_message.append(alphabet[len(alphabet) - (shift - alphabet.index(letter))])
            else:
                decrypted_message.append(alphabet[alphabet.index(letter) - shift])
        except ValueError:
            decrypted_message.append(letter)

    return ''.join(decrypted_message)