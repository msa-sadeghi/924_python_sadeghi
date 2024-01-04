import string
import random

MAX_GUSSES = 10
def generate_secret_number(num_of_digits):
    digits = list(string.digits)
    random.shuffle(digits)
    res = ""
    for s in digits[:num_of_digits]:
        res += s
    return res

def verify_user_guess(guess, secret):
    if guess == secret:
        return "You won!"
    res = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            res.append("Fermi")
        elif guess[i] in secret:
            res.append("Pico")
    if not len(res):
        return "Bagels"
    return "".join(res)

while True:

    guess_counter = 0
    game_status = False
    secret_number = generate_secret_number(3)
    print("secret number generated.")
    while guess_counter < MAX_GUSSES:
        guess_counter += 1
        print(f"guess #{guess_counter}")
        user_guess = input("enter your guess(3 digits number) : ")
        res = verify_user_guess(user_guess, secret_number)
        print(res)
        if user_guess == secret_number:
            game_status = True
            break
    if game_status != True:
        print("you lose")
    if input("Do you want to quit? (y or n) : ") == "y":
        print("see you again")
        break

