# Find the given output list from following input list

Input = [[10,20],[30,40],[50,60],[70,80]]
Output = [[10, 30, 50, 70],[20, 40, 60, 80]]

def Program(matrix):
    d = [[j[i] for j in matrix] for i in range(len(matrix[0]))]
    return d


def main():
    print("Application for demonstration of list comprehension")
    data = [[10, 20], [30,40], [50,60], [70,80]]
    ans = Program(data)
    print("Output list : ",ans)
if __name__ == "__main__":
    main()
