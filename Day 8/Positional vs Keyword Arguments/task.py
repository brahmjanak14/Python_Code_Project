# Functions with input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}?")


# Calling greet_with() with positional Arguments
greet_with("Jack Bauer", "Nowhere")
#vs.
greet_with("Nowhere", "Jack Bauer")


# Calling greet_with() with keyword arguments
greet_with(location="London",name="Angela")
