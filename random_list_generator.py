import random

def generate_list(a, b, length, rounding = 2): 

    if type(a) == int and type(b) == int:
        return [random.randint(a, b) for i in range(length)]
    elif type(a) == float or type(b) == float:
        return [round(random.uniform(a, b), rounding) for i in range(length)]
    
    return None


print(generate_list(0, 150, 5))
