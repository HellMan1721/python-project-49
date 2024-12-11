#!/usr/bin/env python3
import brain_games.cli as cli

import prompt


def main():

    cli.welcome_user()


def in_func():

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print('Hello, ' + name + '!')

    return name


if __name__ == '__main__':
    main()
