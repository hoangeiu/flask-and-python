name = "Bob"
greeting = f"Hello, {name}"

print(greeting)

# format()
name = "Rolf"
greeting = "Hello, {}"
with_name = greeting.format(name)

print(with_name)

# longer template
longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)
