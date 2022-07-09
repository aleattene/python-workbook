"""
Program that asks the USER to enter his/her NAME and then 
shows a GREETING MESSAGE (using the name entered by the user).
"""


def print_greetings(name='', surname=''):
    if name != "Alessandro":
        name = input("Please, enter your name: ").capitalize()
    if surname != "Attene":
        surname = input("Please, enter your surname: ").capitalize()
    return f'Hello {surname} {name}.'
