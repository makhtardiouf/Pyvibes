# Functions with variable number of args
# https://docs.python.org/3.5/tutorial/controlflow.html

def buyCheese(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)

    for arg in arguments:
        print(arg)
    print("\n", "-" * 40)
    print("Featuring:")

    for k in keywords:
        print(f"{k}: {keywords[k]}")

    print(f"The shop keeper was {keywords['shop_keeper']}")


buyCheese("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shop_keeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
