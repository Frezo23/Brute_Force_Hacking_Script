import datetime

tries = 0
number = 0
len_of_pass = 0
guess = []
num_of_char_list = []

running = 0
char_pick = 0

characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')

password = input('Put password here: ')
pass_list = list(password)

for x in range(len(password)):
    guess.append('')
    num_of_char_list.append(0)

len_of_pass = len(pass_list) - 1

while True:
    guess[running] = characters[char_pick]
    char_pick += 1
    if char_pick == 62:
        char_pick = 0
        if running <= len(pass_list) - 2:
            running += 1
        else:
            running = 0
    if guess == pass_list:
        print(guess)
        print(pass_list)
            