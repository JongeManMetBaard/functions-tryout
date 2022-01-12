print("“Welkom bij Papi Gelato”")
counterCones = 0
counterBowls = 0
totalScoopsOfIceCream = 0
coneOrBowl = "bakje" 

# smaken
def askFlavor(scoopsOfIceCream):
    num = 1                
    while num <= scoopsOfIceCream:
        flavor = input("“Welke smaak wilt u voor bolletje nummer " + str(num) + "? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?” ")

        if flavor != "A" and flavor != "C" and flavor != "M" and flavor != "V":
            print("“Sorry dat snap ik niet...”")
            
        if flavor == "A" or flavor == "C" or flavor == "M" or flavor == "V":
            num +=1 

# stap 1
def askAmountOfIceCreamScoops():
    repeat = True 
    while repeat: 
        repeat = False
        scoopsOfIceCream = int(input("“Hoeveel bolletjes wilt u?” "))

        if scoopsOfIceCream <= 3 and scoopsOfIceCream >= 1:
            askFlavor(scoopsOfIceCream)
            askInConeOrBowl(scoopsOfIceCream) 

        elif scoopsOfIceCream <= 8 and scoopsOfIceCream >= 4:
            print("“Dan krijgt u van mij een bakje met " + str(scoopsOfIceCream) + " bolletjes”")
            askFlavor(scoopsOfIceCream)
            global counterBowls
            counterBowls += 1
            askOrderMore("bakje", scoopsOfIceCream)

        elif scoopsOfIceCream > 8:
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
        global coneOrBowl
        coneOrBowl = input("“Wilt u deze " + str(scoopsOfIceCream) + " bolletje(s) in een hoorntje of een bakje? (hoorntje/bakje)”")

        if coneOrBowl == "hoorntje" or coneOrBowl == "bakje":
            if coneOrBowl == "hoorntje":
                global counterCones            
                counterCones += 1

            if coneOrBowl == "bakje": 
                global counterBowls
                counterBowls += 1

            askOrderMore(coneOrBowl, scoopsOfIceCream)

        else:
            print("“Sorry, dat snap ik niet...”")
            repeat = True

    return coneOrBowl

# stap 3
def askOrderMore(coneOrBowl, scoopsOfIceCream):
    global totalScoopsOfIceCream
    repeat = True
    while repeat:
        repeat = False
        orderMore = input("“Hier is uw " + coneOrBowl + " met " + str(scoopsOfIceCream) + " bolletje(s). Wilt u nog meer bestellen? (Y/N)”")

        if orderMore == "Y":        
            totalScoopsOfIceCream += scoopsOfIceCream
            askAmountOfIceCreamScoops()

        elif orderMore == "N": 
            totalScoopsOfIceCream += scoopsOfIceCream
            print("“Bedankt en tot ziens!”")    

        else:
            print("“Sorry dat snap ik niet...”")
            repeat = True

askAmountOfIceCreamScoops()

#(--------------------------------------functions above----------------------------------------------------)
# bonnetje
scoops = 1.10
cones = 1.25
bowls = 0.75


def calc():
    priceCones = counterCones * cones 
    priceBowls = counterBowls * bowls
    priceScoops = totalScoopsOfIceCream * scoops
    global totalPriceAll 
    totalPriceAll = priceScoops + priceBowls + priceCones
    
    print('---------["Papi Gelato"]---------')
    print("")
    print("Bolletjes    " ,totalScoopsOfIceCream, " x  €1.10 = €"+ f'{priceScoops:4.2f}')

    if counterCones > 0: 
        print("Hoorntje     ",counterCones," x  €1.25 = €"+ f'{priceCones:4.2f}')
    if counterBowls > 0:
        print("Bakje        ",counterBowls," x  €0.75 = €"+ f'{priceBowls:4.2f}')
    print("                         --------")
    print("Totaal                   = €"+ f'{totalPriceAll:4.2f}') 
    
calc()