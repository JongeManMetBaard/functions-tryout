def nameAge():
    name = input("What's your name?")
    if name == "stop":
        return
    age = input("How old are you?")
    print("Hallo" ,name, "je leeftijd is", age)
    nameAge()
print("If you want to stop, type stop")

nameAge() 