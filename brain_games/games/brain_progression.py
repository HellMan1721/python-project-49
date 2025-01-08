import random

DESC = 'What number is missing in the progression?'


def gen_gamedata():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    end = start + random.randint(5, 15) * step
    ran_prog = list(range(start, end, step))
    hid_index = random.randint(0, len(ran_prog) - 1)
    hid_value = f"{ran_prog[hid_index]}"
    ran_prog[hid_index] = '..'
    quest = ' '.join(str(i) for i in ran_prog)
    return quest, hid_value
