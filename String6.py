def Function():
    s = "pythonprogram"
    d = 3
    left = s[d: ]+s[ :d]
    print(left)

    right = s[-d: ]+s[ :-d]
    print(right)



def main():
    print("Application for demonstration of string")
    Function()    

if __name__ == "__main__":
    main()