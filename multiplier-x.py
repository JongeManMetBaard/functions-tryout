def tafelVan(tafel:int):
    for i in range(1,11):
        print(i*tafel)
    
welkGetal = int(input("Van welk getal wilt u de tafel zien?"))
tafelVan(welkGetal)
