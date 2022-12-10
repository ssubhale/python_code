# Bellow have two list state and capital create dictionary which keys state list and values capital by dictionary comprehension

state = ["Maharastra", "Rajastan", "Gujrat","Karnataka"]
capital = ["Mumbai", "Jaipur", "Gandhinagar", "Benglore"]


def Program(seq1,seq2):
    d = {seq1[i]:seq2[i] for i in range(len(seq1))}
    return d

def main():
    print("Application for demonstration of dictionary comprehention")
    state = ["Maharastra", "Rajastan", "Gujrat","Karnataka"]
    capital = ["Mumbai", "Jaipur", "Gandhinagar", "Benglore"]
    ans = Program(state,capital)
    print("Output dictionary : ",ans)

if __name__ == "__main__":
    main()