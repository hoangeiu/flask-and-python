# =====> Must be dictionary <======


def named1(**kwargs):
    print(kwargs)


named1(name="Bob", age=25)

# ///////////


def named2(name, age):
    print(name, age)


details = {"name": "Bob", "age": 25}

named2(**details)
named1(**details)

# //////////


def print_nicely(**kwargs):
    named1(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)

# /////////


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)
