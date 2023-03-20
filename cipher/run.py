from encrypt.core import encrypt
from decrypt.core import decrypt
from helpers import START_UP_MESSAGE, exit_session, user_choices


def main():
    print(START_UP_MESSAGE)
    exit_cipher = False

    while not exit_cipher:
        message, shift, user_choice = user_choices()

        if user_choice == 'encrypt' or user_choice == 'encode':
            print("Encrypted message is: ", encrypt(message, shift))
        if user_choice == 'decrypt' or user_choice == 'decode':
            print("Encrypted message is: ", decrypt(message, shift))

        exit_cipher = exit_session(input("Type Y or Yes to EXIT. Any other key to continue.\n"))
        if exit_cipher:
            print("Goodbye")


main()
