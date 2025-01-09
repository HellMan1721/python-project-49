import random

DESCRIPTION = 'What number is missing in the progression?'


def gen_gamedata():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    end = start + random.randint(5, 15) * step
    random_progression = list(range(start, end, step))
    hidden_index = random.randint(0, len(random_progression) - 1)
    hidden_value = f"{random_progression[hidden_index]}"
    random_progression[hidden_index] = '..'
    question = ' '.join(str(i) for i in random_progression)
    return quest, hidden_value
