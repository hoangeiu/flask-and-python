def hello():
    print("Hello world!")


def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds id {age_seconds}")


friends = ["Rolf", "Bob"]


def add_friend():
    friend_name = input("Enter your friend name: ")
    friends.append(friend_name)
