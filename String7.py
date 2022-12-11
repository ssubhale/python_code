# Given a string input,count all lower case, upper case and digits without using built-in functions.


def Function(seq):
    upper = 0
    lower = 0
    digit = 0

    for i in seq:
        if i >= "A" and i <= "Z":
            upper += 1
        elif i >= "a" and i <= "z":
            lower += 1
        elif i >= "0" and i <= "9":
            digit += 1
        else:
            pass
    return upper, lower, digit

def main():
    print("Application for demonstration of string")
    s = input("enter string : ")
    a, b, c = Function(s)
    print(f"Uppercase letters : {a}\nLowercase letters : {b}\nDigits : {c}")


if __name__ == "__main__":
    main()