import datetime

tries = 0
guess = ''

list_char = 0

characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')

password = input('Put password here: ')
pass_list = list(password)

while True:
    