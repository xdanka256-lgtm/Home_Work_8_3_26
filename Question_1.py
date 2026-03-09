import random

def get_lucky_number(amount: int) -> tuple[int]:
    a = []
    for i in range(amount):
        a.append(random.randint(1, 100))
    return tuple(a)

print(get_lucky_number(10))
