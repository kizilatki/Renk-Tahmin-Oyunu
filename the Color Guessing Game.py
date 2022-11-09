print (" Renk Tahmin Oyununa Hoş Geldiniz:   ")

color = "mavi"

Player_Color = str(input(" Temel Renkler İçerisinden bir Renk Giriniz:  "))

chance = 3

while True:
    if chance != 0:
        if Player_Color != color:
            chance -= 1
            print(" {} hakkiniz kaldi." .format(chance))
            Player_Color = str(input(" Temel Renkler İçerisinden bir Renk Giriniz:  "))

        elif Player_Color != color:
            chance -= 1
            print(" {} hakkiniz kaldi." .format(chance))
            Player_Color = str(input(" Temel Renkler İçerisinden bir Renk Giriniz:  "))

        if Player_Color == color:
            chance -= 1
            print("Tebrikler, Bildiniz!")
            break
    
    else:
        chance == 0
        print ("Game Over!")
        break
