#!/usr/bin/env python3
import brain_games.cli as cli


def main():

    cli.welcome_user()


def in_func():

    name = cli.welcome_user()

    return name


if __name__ == '__main__':
    main()
