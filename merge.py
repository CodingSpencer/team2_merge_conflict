def get_stuff():
    name = input("What's your name?")
    return name


def print_stuff():
    stuff = "Hi ", get_stuff()
    print(stuff)

def german_hello_world():
    message = "Hallo Welt!"
    print(message)

def nathans_function():
    print("Nathan's function")
    
def countToOne():
    for i in range(1):
        print(i+1)


def duck_logic():
    quack = input('Whats the difference between a duck?')
    print(f'{quack} is indeed the difference between a duck.')

def main():
    print_stuff()
    nathans_function()
    german_hello_world()
    countToOne()
    duck_logic()

if __name__ == "__main__":
    main()