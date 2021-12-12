# Jack en de schatkist


def welkRichting():
    print ("level 1")

    print ("Je staat voor een bos en op een bord staat: 'Alleen toegankelijk voor 30 jarige mensen'. Je bent 29, wat ga je doen?")

    vraagWelkPad = input("Naar huis gaan, een jaar wachten of verder het bos inlopen (huis, wachten, lopen)")
    if vraagWelkPad == "huis":
        print("Je gaat naar huis en je word onderweg opgegeten door Bigfoot")
        print('Game Over!')
        welkRichting()
    elif vraagWelkPad == "wachten":
        print("Je gaat een jaar wachten maar je sterft door honger")    
        print('Game Over!')
        welkRichting()
    else:
        None
welkRichting()
def apple():
    print("level 2")

    appel = input("Je loopt verder het bos in en je ziet een appel aan een boom hangen die 10 HP waard is, wil je hem pakken?(ja/nee)")
    if appel == "nee":
        print("je pakt niet de appel en je komt een tijger tegen.")
        HP = 50
        if HP < 60:
            print("Je gezondheid is niet hoger dan 50 HP en je word vermoord door de tijger")
            print('Game Over!')
            apple()
    elif appel != "nee":
        print("Je pakt de appel en je gezondheid is gestegen naar 60 HP")
apple()
def knife():
    print("level 3")

    mes = input("Je komt een tijger tegen en je hebt het dier verslagen. Terwijl je verder het bos inloopt kom je een mes tegen, wil je de mes pakken?(ja/nee) ")
    if mes == "nee":
        print("Je pakt niet de mes en komt een bandiet tegen")
        print("De bandiet vermoord je")
        print('Game Over!')
        knife()  
    else: 
        print("level 4")
knife()

print("Je pakt de mes en je komt een bandiet tegen. Je hebt de bandiet vermoord met je mes")           
appelOfPeer = input("Je loopt verder en je komt een appel en een peer tegen. De peer is 50 HP waard, welke wil je pakken?(appel,peer)")
if appelOfPeer == "peer":
    kerker = input("Je gezondheid is gestegen naar 110 HP. Je komt een kerker tegen wil je hem betreden?(ja/nee)")
    if kerker == "ja": 
        HPPearOrApple = 110 
        if HPPearOrApple <= 110 or HPPearOrApple <= 70: 
            boobytrapPeer = input("Je betreed de kerker en je ziet een boobytrap, wil je verder lopen?(ja/nee)")
            if boobytrapPeer == "ja":
                print("Je loopt verder en je word vermoord door de boobytrap")
                print('Game Over!')
            else:
                print("Je blijft stilstaan en word vermoord door pijlen")
                print('Game Over!')
    else: 
        print("Je gaat niet de kerker betreden en je valt in een gat")
        print('Game Over!')            
else:
    print("level 5") 

    kerkerAppel = input("Je gezondheid is gestegen naar 70 HP. Je komt een kerker tegen, wil je hem betreden?(ja/nee)")
    if kerkerAppel == "nee":
        print("Je gaat niet de kerker betreden en je valt in een gat")
        print('Game Over!')
    else:
        print("level 6") 

        boobytrapAppel = input("Je betreed de kerker en je ziet een boobytrap, wil je verder lopen?(ja/nee)")
        if boobytrapAppel == "nee":
            print("Je blijft stilstaan en word vermoord door pijlen")
            print('Game Over!')
        else:
            sleutel = input("Je loopt verder en je overleeft de boobytrap. De deur voor je gaat open en je komt een sleutel tegen, wil je hem oprapen?(ja/nee)")
            if not sleutel == "ja":
                print("Je raapt de sleutel niet op en de sleutel verdwijnt. Je loopt verder maar je komt een deur tegen die op slot zit.")
                print('Game Over!')
            else:
                print("level 7")

                hurken = input("Je raapt de sleutel op. Je loopt verder en je komt een deur tegen. Je probeert hem te openen met je sleutel maar het lukt niet. Op dat moment zie je een bord waarop staat dat je moet hurken om de deur te openen, wil je hurken?(ja/nee)")
                if hurken == "nee":
                    print("Je hurkt niet en je word verpletterd door een reusachtige bal.")
                    print('Game Over!')
                elif hurken == "ja" and sleutel == "ja":
                    print("level 8") 

                    tenenStaan = input("Je hurkt en de deur gaat open. Je loopt verder en je komt een andere deur tegen waarop staat dat je op je tenen moet staan, wil je dit doen?(ja/nee)")
                    if tenenStaan == "nee":
                        print("Je gaat dat niet doen en je word opgegeten door een haai")
                        print('Game Over!')
                    else:
                        print("level 9")

                        vierStrepen = int(input("Je staat op je tenen en de deur gaat open. Je loopt verder en je komt een deur tegen. Er staat dat je minimaal vier strepen moet krassen op de deur, hoeveel strepen wil je krassen?(10 of 3)"))
                        if vierStrepen < 4:
                            print("Je krast minder dan 4 strepen en je zit vast in de kerker")
                            print('Game Over!')
                        elif vierStrepen > 4:
                            print("level 10")

                            springen = int(input("Je krast meer dan 4 strepen en de deur word geopend. Je komt de laatste deur tegen en daarop staat dat je twee keer of minder moet springen, hoe vaak wil je springen?(3 of 1)"))
                            if springen <= 2:
                                print("Je springt minder dan twee keer en word vermoord door spijkers")
                                print('Game Over!')
                            elif springen >= 2:
                                print("De deur word geopend en je komt een schatkist tegen. Je opent de kist en er zit heel veel goud in. Gefeliciteerd je hebt 200 miljoen euro verdiend!!!!!!!")    