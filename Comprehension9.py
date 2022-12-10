# Given a dictionary, swap the keys-values

def Program(seq):
    d = {k:v for v,k in seq.items()}
    return d

def main():
    print("Application for demonstration of dictionary")
    data = {"A":1, "B":2, "C":3, "D":4, "E":5}
    ans = Program(data)
    print("Output dictionary : ",ans)

if __name__ == "__main__":
    main()
