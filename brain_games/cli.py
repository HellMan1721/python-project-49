import prompt


def welcome_user():

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print('Hello, ' + name + '!')


def in_func():

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print('Hello, ' + name + '!')

    return name
