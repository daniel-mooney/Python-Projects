import random
import numpy

# Useful for creating large data files consisiting of numbers for other programs

def generate_list(a, b, length, rounding = 2): 

    if type(a) == int and type(b) == int:
        return [random.randint(a, b) for i in range(length)]
    elif type(a) == float or type(b) == float:
        return [round(random.uniform(a, b), rounding) for i in range(length)]
    
    return None


def main():
    print(generate_list(0.0, 0.9, 5))


if __name__ == "__main__":
    main()
