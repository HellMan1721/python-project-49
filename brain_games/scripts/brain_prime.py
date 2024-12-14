import brain_games.engine as games
import brain_games.games.brain_prime as plant


def main():

    games.engine(plant.desc, plant.is_prime)


if __name__ == '__main__':

    main()
