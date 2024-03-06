def parrot(message="Squawk!"):
    print(message)
    return message
default_message = parrot()  # This will print "Squawk!" and assign "Squawk!" to default_message
custom_message = parrot("Hello!")  # This will print "Hello!" and assign the same string to custom_message
