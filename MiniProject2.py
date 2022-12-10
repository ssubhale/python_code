## Create the world, countries, states, cities ==>> Nested list

def Project():
    world = list()
    n = int(input("Enter no of countries you want to add in world list : "))
    for i in range(n):
        count = list()
        ns = int(input("Enter no of states : "))
        for j in range(ns):
            state = list()
            nc = int(input("Enter no of cities : "))
            for k in range(nc):
                state.append(input("Enter city name : "))
            count.append(state)
        world.append(count)
    return world

def main():
    print("Application for demonstration of nested list")
    ans = Project()
    print(ans)

if __name__ == "__main__":
    main()