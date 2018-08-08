#! /usr/bin/python3.6
# password_locker.py - an insecure password locker program
# this program contains a random password generator.
import sys
import pyperclip
import random
import string


def random_password_generator(length=20):
    ''' generates a random number of the desired length '''
    rand_strings = string.ascii_letters + '1234567890'  # creates a string containing all possible chars
    temp_pass = ''  # the string to eventually return
    for i in range(length):
        temp_pass += random.choice(rand_strings)
    return temp_pass


PASSWORDS = {'master': 'masterpass',
             'bgu': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'email': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

master_pass = sys.argv[1]  # first command line arg is the master password
if master_pass == PASSWORDS['master']:
    print('access granted.')
else:
    print('access denied, exiting program.')
    sys.exit()

print('please enter account name:')
account = input()

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
elif not (account.isalpha):
    print('account name is only allowed to contains letters')
else:
    print('There is no account named ' + account)
    print('would you like to create a password for this account?')
    print('y/n')
    answer = input()
    if str(answer).lower() == 'y':
        print('creating a password:')
        new_pass = random_password_generator(30)
        PASSWORDS.get(account, new_pass)
        print('succesfuly created a new acc-pass pair. account name: ' + str(account))
        pyperclip.copy(new_pass)
        print('coppied new password to clipboard')
    else:
        print('account name contains more then letters, invalid.')
