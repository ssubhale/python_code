## Nested set


def Project():
    world = set()
    n = int(input('Enter no of country:'))
    for i in range(n):
        country = set()
        ns = int(input('Enter no states:'))
        for j in range(ns):
            states = set()
            nc = int(input('Enter no of cities:'))
            for k in range(nc):
                states.add(input('Enter a name of cities:'))
            country.add(frozenset(states))
        world.add(frozenset(country))
    return world

def main():
    print("Application for demonstration of nested set")
    ans = Project()
    print(ans)

if __name__ == "__main__":
    main()