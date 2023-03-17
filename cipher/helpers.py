START_UP_MESSAGE = '''


 ▄████▄  ▓█████ ▄▄▄        ██████  ▄▄▄       ██▀███      ▄████▄▓██   ██▓ ██▓███   ██░ ██ ▓█████  ██▀███  
▒██▀ ▀█  ▓█   ▀▒████▄    ▒██    ▒ ▒████▄    ▓██ ▒ ██▒   ▒██▀ ▀█ ▒██  ██▒▓██░  ██▒▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒
▒▓█    ▄ ▒███  ▒██  ▀█▄  ░ ▓██▄   ▒██  ▀█▄  ▓██ ░▄█ ▒   ▒▓█    ▄ ▒██ ██░▓██░ ██▓▒▒██▀▀██░▒███   ▓██ ░▄█ ▒
▒▓▓▄ ▄██▒▒▓█  ▄░██▄▄▄▄██   ▒   ██▒░██▄▄▄▄██ ▒██▀▀█▄     ▒▓▓▄ ▄██▒░ ▐██▓░▒██▄█▓▒ ▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  
▒ ▓███▀ ░░▒████▒▓█   ▓██▒▒██████▒▒ ▓█   ▓██▒░██▓ ▒██▒   ▒ ▓███▀ ░░ ██▒▓░▒██▒ ░  ░░▓█▒░██▓░▒████▒░██▓ ▒██▒
░ ░▒ ▒  ░░░ ▒░ ░▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░   ░ ░▒ ▒  ░ ██▒▒▒ ▒▓▒░ ░  ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░  ▒    ░ ░  ░ ▒   ▒▒ ░░ ░▒  ░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░     ░  ▒  ▓██ ░▒░ ░▒ ░      ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░
░           ░    ░   ▒   ░  ░  ░    ░   ▒     ░░   ░    ░       ▒ ▒ ░░  ░░        ░  ░░ ░   ░     ░░   ░ 
░ ░         ░  ░     ░  ░      ░        ░  ░   ░        ░ ░     ░ ░               ░  ░  ░   ░  ░   ░     
░                                                       ░       ░ ░                                      


'''


def get_user_choice(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() != "encode" and user_input.lower() != "decode" \
                and user_input.lower() != "encrypt" and user_input.lower() != "decrypt":
            print("Not a valid option. Type 'encode' or 'decode'")
            continue
        else:
            break
    return user_input


def get_shift(prompt):
    while True:
        shift = input(prompt)
        try:
            shift = normalize_shift(int(shift))
        except ValueError:
            print("Shift must be an integer.")
            continue

        if shift < 0:
            print("Shift must be larger than 0")
            continue
        else:
            break
    return shift


def normalize_shift(shift):
    if shift > 25:
        return int(shift - int(shift/26) * 26)
    else:
        return shift


def user_choices():
    user_choice = get_user_choice("Type 'encode' to encrypt a message or 'decode' to decrypt a message.\n")
    message = input(f"Write the message you want to {user_choice}:\n")
    shift = get_shift("By how much do you want to shift? \n")
    return message, shift, user_choice


def exit_session(exit_choice):
    return True if exit_choice.lower() == 'y' or exit_choice.lower() == 'yes' else False
