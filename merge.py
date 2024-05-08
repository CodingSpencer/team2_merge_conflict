def get_stuff():
    name = input("What's your name?")
    return name


def print_stuff():
    stuff = "Hi ", get_stuff()
    print(stuff)

def main():
    print_stuff()

if __name__ == "__main__":
    main()