# https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

#     Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
import random, string

def password_gen():
    chars = string.printable[:string.printable.find(' ')]
    password = ''.join([ random.choice(chars) for i in range(0,8)])
    return password

if __name__=="__main__":
    print(password_gen())