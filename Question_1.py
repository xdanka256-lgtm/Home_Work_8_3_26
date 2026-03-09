import random

def get_lucky_number(amount: int) -> tuple[int]:
    numbers = []
    for i in range(amount):
        numbers.append(random.randint(1, 100))
    return tuple(numbers)


