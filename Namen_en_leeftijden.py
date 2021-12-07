def nameAge():
    name = input("What's your name?") 
    age = input("How old are you?")
    print("Hallo" ,name, "je leeftijd is", age)
    if name == "stop" or age == "stop":
        return 
    nameAge()
print("If you want to stop, type stop")

nameAge() 