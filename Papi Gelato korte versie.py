print("“Welkom bij Papi Gelato”")
counterCones = 0
counterBowls = 0
totalScoopsOfIceCream = 0
coneOrBowl = "bakje"

counterWhippedCream = 0
counterTopping = 0
totalScoopsOfIceCreamSprinkels = 0
counterCaramelSauceCone = 0
counterCaramelSauceBowl = 0

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

            askTopping(coneOrBowl, scoopsOfIceCream)

        else:
            print("“Sorry, dat snap ik niet...”")
            repeat = True

    return coneOrBowl

# toppings
def askTopping(coneOrBowl, scoopsOfIceCream):

    repeat = True 
    while repeat:
        repeat = False
        global topping
        topping = input("“Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?”")

        if topping == "A" or topping == "B" or topping == "B" or topping == "C" or topping == "D":
            if topping == "A" or topping == "B" or topping == "C" or topping == "D":
                global counterTopping
                counterTopping += 1
                if topping == "B":
                    global counterWhippedCream
                    counterWhippedCream += 1
                if topping == "D":
                    if coneOrBowl == "hoorntje":
                        global counterCaramelSauceCone
                        counterCaramelSauceCone += 1
                    if coneOrBowl == "bakje":
                        global counterCaramelSauceBowl
                        counterCaramelSauceBowl += 1
                if topping == "A":
                    counterTopping = 0

            
            askOrderMore(coneOrBowl, scoopsOfIceCream)
        
        else: 
            print("“Sorry, dat snap ik niet...”")
            repeat = True

# stap 3
def askOrderMore(coneOrBowl, scoopsOfIceCream):
    global totalScoopsOfIceCream
    repeat = True
    while repeat:
        repeat = False
        orderMore = input("“Hier is uw " + coneOrBowl + " met " + str(scoopsOfIceCream) + " bolletje(s). Wilt u nog meer bestellen? (Y/N)”")

        if orderMore == "Y":        
            totalScoopsOfIceCream += scoopsOfIceCream
            if topping == "C":
                global totalScoopsOfIceCreamSprinkels
                totalScoopsOfIceCreamSprinkels += scoopsOfIceCream

            askAmountOfIceCreamScoops()

        elif orderMore == "N": 
            totalScoopsOfIceCream += scoopsOfIceCream
            if topping == "C":
                totalScoopsOfIceCreamSprinkels += scoopsOfIceCream
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

whippedCream = 0.50
sprinkels = 0.30
caramelSauceCone = 0.60
caramelSauceBowl = 0.90 

def calc():
    priceCones = counterCones * cones 
    priceBowls = counterBowls * bowls
    priceScoops = totalScoopsOfIceCream * scoops
    priceSprinkels = sprinkels * totalScoopsOfIceCreamSprinkels
    priceCaramelSauceCone = caramelSauceCone * counterCaramelSauceCone
    priceCaramelSauceBowl = caramelSauceBowl * counterCaramelSauceBowl
    priceWhippedCream = counterWhippedCream * whippedCream 
    priceTopping = priceWhippedCream + priceCaramelSauceCone + priceCaramelSauceBowl + priceSprinkels
    totalPriceAll = priceScoops + priceBowls + priceCones + priceTopping
    
    print('---------["Papi Gelato"]---------')
    print("")
    print("Bolletjes    " ,totalScoopsOfIceCream, " x  €1.10 = €"+ f'{priceScoops:4.2f}')

    if counterCones > 0: 
        print("Hoorntje     ",counterCones," x  €1.25 = €"+ f'{priceCones:4.2f}')
    if counterBowls > 0:
        print("Bakje        ",counterBowls," x  €0.75 = €"+ f'{priceBowls:4.2f}')
    if counterTopping > 1:
        print("Topping       1  x  €"f"{priceTopping:4.2f} = €"+ f'{priceTopping:4.2f}')
    print("                         --------")
    print("Totaal                    = €"+ f'{totalPriceAll:4.2f}') 
    
calc()