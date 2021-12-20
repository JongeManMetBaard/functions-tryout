print("“Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.”")
# stap 1
def askAmountOfIceCreamCoops():
    repeat = True 
    while repeat: 
        repeat = False
        scoopsOfIceCream = int(input("“Hoeveel bolletjes wilt u?” "))
        if scoopsOfIceCream <= 3 and scoopsOfIceCream >= 1:
            askInConeOrBowl(scoopsOfIceCream)
        elif scoopsOfIceCream <= 8 and scoopsOfIceCream >= 4:
            print("“Dan krijgt u van mij een bakje met " + str(scoopsOfIceCream) + " bolletjes”")
            askOrderMore("bakje", scoopsOfIceCream)
        elif scoopsOfIceCream >8:
            print("“Sorry, zulke grote bakken hebben we niet...”")
            repeat = True        
        else:
            print("“Sorry dat snap ik niet...”")
            repeat = True


# stap 2
def askInConeOrBowl(scoopsOfIceCream):
    repeat = True
    while repeat:
        repeat = False
        coneOrBowl = input("“Wilt u deze " + str(scoopsOfIceCream) + " bolletje(s) in een hoorntje of een bakje? (hoorntje/bakje)”")
        if coneOrBowl == "hoorntje" or coneOrBowl == "bakje":
            askOrderMore(coneOrBowl, scoopsOfIceCream)
        else:
            print("“Sorry, dat snap ik niet...”")
            repeat = True
    return coneOrBowl

# stap 3
def askOrderMore(coneOrBowl, scoopsOfIceCream):
    repeat = True
    while repeat:
        repeat = False
        orderMore = input("“Hier is uw " + coneOrBowl + " met " + str(scoopsOfIceCream) + " bolletje(s). Wilt u nog meer bestellen? (Y/N)”")
        if orderMore == "Y":
            askAmountOfIceCreamCoops()
        elif orderMore == "N":
            print("“Bedankt en tot ziens!”")                        
        else:
            print("“Sorry dat snap ik niet...”")
            repeat = True

askAmountOfIceCreamCoops()