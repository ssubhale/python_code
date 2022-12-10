#Find the planets whose length is less than 6.from given list by list comprehension

planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 


def Program(seq):
    l = [j for i in seq for j in i if len(j) < 6]
    return l


def main():
    print("Application for demonstration of list comprehension")
    planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 

    ans = Program(planets)
    print("Output list : ",ans)

if __name__ == "__main__":
    main()