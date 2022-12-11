# Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string

def Function(seq1,seq2):
    s3 = seq1[0]+seq2[0]+seq1[len(seq1)//2]+seq2[len(seq2)//2]+seq1[-1]+seq2[-1]
    return s3


def main():
    print("Application for demonstration of string")
    s1 = input('Enter string:')
    s2 = input('Enter string:')
    ans = Function(s1,s2)
    print("Output string : ",ans)

if __name__ == "__main__":
    main()