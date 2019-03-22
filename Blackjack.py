import random
import copy
dizi=[[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13]]
gecici=dizi[:]#işlemler bunun üzerinde yapılacak, asıl diziye dokunulmayacak


def menu():
    secim=8
    while not 1<=secim<=3:
        secim=int(input("1. Fal Bakma Oyunu\n2. Blackjack (21) Oyunu\n3. Çıkış\nSeçiminizi giriniz:"))
        if secim==1:fal()
        elif secim==2:blackjack()
        elif secim==3:
            kontrol=input("Cıkmak istediginize emin misiniz?[e/E/h/H]")
            if kontrol.upper()=='H':menu()
            else:exit()

def tekrar_fal():
    tekrar = input("Tekrar oynamak istiyor musunuz?[e/E/h/H]")
    if tekrar.upper() == 'E':fal()
    else:menu()
def tekrar_blackjack():
    tekrar = input("Tekrar oynamak istiyor musunuz?[e/E/h/H]")
    if tekrar.upper() == 'E': blackjack()
    else: menu()

def rand():
    r2=random.randrange(0,4)#kupa karo maca sinek icin random
    r3=random.randrange(0,13)#kartlar icin random
    deger=gecici[r2][r3]#kartların isminin yer alacagı değişken
    deger2=gecici[r2][r3]#kartların sayısal degerinin yer alacağı değişken
    if r2==0:isim="kupa"
    elif r2==1:isim="karo"
    elif r2==2:isim="maca"
    elif r2==3:isim="sinek"
    if r3==10:
        deger="vale"
        deger2=10
    elif r3==11:
        deger="kiz"
        deger2=10
    elif r3==12:
        deger="papaz"
        deger2=10
    return isim,deger,deger2,r2,r3

def fal():
    eslesen = []
    elenen = []
    toplam_eslesen = 0
    kontrol=input("Niyetinizi tuttunuz mu(e/h)?")
    if kontrol=='e':isim,deger,deger2,r2,r3=rand()
    i=1
    while len(elenen)<52:#tüm kartların bitmesi durumu
        tisim, tdeger, tdeger2,r2,r3 = rand()
        while [r2,r3] in elenen:#kartın daha önce elenip elenmediğini kontrol
            tisim, tdeger, tdeger2, r2, r3 = rand()
        print(i, ".", tisim, tdeger)
        elenen.append([r2,r3])
        if tdeger==deger and tdeger2==deger2:
            print("eslesti")
            eslesen.append(tdeger2)#eslesenlerin değerini eslesen listesine ekleme
            del elenen[-1:-(i+1):-1]#eslesme oldugundan dolayı önceki kartları elenenlerden çıkartma
            elenen.append([r2, r3])#eslesen kartı elenen listesine ekleme
            isim, deger, deger2, r2, r3 = rand()
            i=0
        elif i==13:
            print("Hiç eşleşmedi, saymaya yeniden başlanıyor...")
            i = 0
        i += 1
    for k in range(len(eslesen)):
        toplam_eslesen+=eslesen[k]
    print("Bitti, toplam puanınız:",toplam_eslesen)
    print("Niyetiniz %",toplam_eslesen," ihtimalle gerçekleşecek")
    print(len(elenen))
    print(eslesen)
    tekrar_fal()

def blackjack():
    oyuncu_isim = []#oyuncunun kartlarinin isimlerinin bulundugu liste
    dagitici_isim = []#dagiticinin kartlarinin isimlerinin bulunduğu liste
    elenen = []
    dagitici_puan,dagitici_puan2=0,0
    oyuncu_puan,oyuncu_puan2=0,0#as 1 ve as 11 durumlarındaki puanlar
    oyuncu_as, dagitici_as, as_degisim=0,0,0
    for m in range(2):#dagiticinin kendine iki kart cekmesi
        isim, deger, deger2, r2, r3 = rand()
        while [r2,r3] in elenen:#kart daha önce kullanilmis mi? kontrol
            isim, deger, deger2, r2, r3 = rand()
        if deger2==1:
            dagitici_as+=1
            dagitici_puan+=10
        if m==0:print("Dagiticinin acik kagidi:", isim, deger)
        dagitici_isim.append(isim +" "+ str(deger))
        dagitici_puan += deger2
        elenen.append([r2, r3])
    isim, deger, tdeger2, r2, r3 = rand()#oyuncunun ilk iki kartindan birincisini desteden cekme
    while [r2, r3] in elenen:#kart daha önce kullanilmis mi? kontrol
        isim, deger, tdeger2, r2, r3 = rand()
    oyuncu_puan += tdeger2
    oyuncu_isim.append(isim +" "+ str(deger))
    elenen.append([r2, r3])
    kontrol1 = 'K'
    while kontrol1=='K':
        isim, deger, deger2, r2, r3 = rand()
        while [r2,r3] in elenen:#kart daha önce kullanilmis mi? kontrol
            isim, deger, deger2, r2, r3 = rand()
        oyuncu_isim.append(isim +" "+ str(deger))
        elenen.append([r2, r3])
        oyuncu_puan += deger2
        if deger2==1:
            oyuncu_as+=1
            oyuncu_puan2=oyuncu_puan+10#as 11 olduğundaki puan
        else:oyuncu_puan2+=deger2
        if oyuncu_as>=1:print("Oyuncunun Kağıtları:",oyuncu_isim,"(toplam ",oyuncu_puan," yada ",oyuncu_puan2,")")
        else:print("Oyuncunun Kağıtları:",oyuncu_isim,"(toplam ",oyuncu_puan,")")
        #OYUNCU AS 1 YADA 11 OLMASI DURUMLARI
        if oyuncu_puan2>oyuncu_puan and oyuncu_puan2<21:oyuncu_esas_puan=oyuncu_puan2
        else:oyuncu_esas_puan=oyuncu_puan
        if oyuncu_as>=1:
            if oyuncu_esas_puan <= 11:
                if oyuncu_as >= 1: oyuncu_esas_puan += 10
            elif oyuncu_esas_puan == 1:
                oyuncu_esas_puan += 10
            elif oyuncu_esas_puan == 2:
                if oyuncu_as == 2: oyuncu_esas_puan = 12
        #---------------------------------
        if oyuncu_esas_puan>21:
            print("Oyuncu battı, Dağıtıcı kazandı")
            tekrar_blackjack()
        if oyuncu_esas_puan==21:
            print("Oyuncu Blackjack yaptı, sıra dağıtıcıda")
            break
        if kontrol1=="P":
            print("Oyuncunun puanı:",oyuncu_esas_puan," sıra dağıtıcıda")
            break
        kontrol1=input("(K)ağıt mı, (P)as mı?:")
    print("Dağıtıcının Kağıtları:",dagitici_isim," (toplam puan:",dagitici_puan,")")
    if oyuncu_esas_puan==21 and dagitici_puan!=21:#dagiticiya gecmeden oyunu oyuncunun kazanması durumu
        print("Oyunu oyuncu kazandı")
        tekrar_blackjack()
    while dagitici_puan<=16:
        isim, deger, deger2, r2, r3 = rand()
        if deger2==1:
            dagitici_as+=1
            dagitici_puan+=10
        dagitici_isim.append(isim +" "+ str(deger))
        dagitici_puan += deger2
        elenen.append([r2, r3])
        if dagitici_puan>21:#dagiticinin as degerinin belirlenmesi
            if dagitici_as>=1 and dagitici_as>as_degisim:
                dagitici_puan-=10
                as_degisim+=1
        print("Dağıtıcının Kağıtları:", dagitici_isim, " (toplam puan:", dagitici_puan, ")")
    #SONUC DURUMLARI
    if dagitici_puan>21:
        print("Dagitici batti, oyunu Oyuncu kazandi")
        tekrar_blackjack()
    if dagitici_puan==21:
        print("Dagitici Blackjack yapti")
    if dagitici_puan==oyuncu_esas_puan:
        print("Oyun berabere")
        tekrar_blackjack()
    if oyuncu_esas_puan>dagitici_puan:
        print("Oyunu oyuncu kazandı")
        tekrar_blackjack()
    if oyuncu_esas_puan<dagitici_puan:
        print("Oyunu Dagitici kazandi")
        tekrar_blackjack()
menu()