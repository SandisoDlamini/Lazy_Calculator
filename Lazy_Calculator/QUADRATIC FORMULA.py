print("Welcome to the quadratic format calculator.\n")
print("Quadratic equation structure: ax**2 + bx + c")

from fractions import Fraction

a_value = int(input("a: "))
b_value = int(input("b: "))
c_value = int(input("c: "))


def quad_formula(a=0, b=0, c=0):

    print(f"\na = {a}, b = {b}, c = {c}")

    square = (b**2) - (4 * a * c)

    print(f"\nsquare = {square}")

    square_root = square ** (1 / 2) if square >= 0 else None
    print(f"square_root = {square_root}")

    if square_root:
        addition_numerator = (-b) + square_root
        subtraction_numerator = (-b) - square_root
        denominator = (2 * a)

        addition_answer = addition_numerator / denominator
        add_float_test = int(addition_answer)
        if addition_answer != add_float_test:
            addition_answer = str(Fraction(int(addition_numerator), denominator))
        else:
            addition_answer = str(int(addition_answer))

        subtraction_answer = subtraction_numerator / denominator
        sub_float_test = int(subtraction_answer)
        if subtraction_answer != sub_float_test:
            subtraction_answer = str(Fraction(int(subtraction_answer), denominator))
        else:
            subtraction_answer = str(int(subtraction_answer))

        print(f"\nx = {addition_answer} or x = {subtraction_answer}")
    else:
        print("<Answer Undefined>")


quad_formula(a_value, b_value, c_value)
