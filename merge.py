def get_stuff():
    name = input("What's your name?")
    return name


def print_stuff():
    stuff = "Hi ", get_stuff()
    print(stuff)

def german_hello_world():
    message = "Hallo Welt!"
    print(message)

def main():
    print_stuff()

if __name__ == "__main__":
    main()