#for loop

#start => (0)
#stop =>
#step => (1)

for i in range(10):
    print(i)

for i in range(0,10,1):
    print(i)

# girdiğin 3 sayıdan hangisi n büyük?

""" biggestValue = 0
for i in range(3):
    sayi = int(input(f"{i+1}. sayıyı giriniz: "))
    if sayi > biggestValue:
        biggestValue = sayi

print("Girdiğiniz sayılar arasında en büyük olanı: " + str(biggestValue)) """


# forRangeMin = int(input("Döngünün alt limitini belirleyiniz: "))
# forRangeMax = int(input("Döngünün üst limitini belirleyiniz: "))

# for i in range(forRangeMin, forRangeMax):
#     if i % 2 == 0:
#         print(i)


""" sayilar = []

for i in range(3):
    sayilar.append(int(input(f"{i+1}. Sayıyı Gİriniz: ")))

sayilar.sort(reverse=True)
print(sayilar)
 """


ogrenciler = ["Güneş", "Recep", "Betül", "Yunus", "İrem"]
print(len(ogrenciler))   #length => uzunluğu, eleman sayısı

#eleman indexleri
for i in range(len(ogrenciler)):
    print(ogrenciler)

#her bir elemanı tek tek gösterir. index ile çalışır
for i in range(len(ogrenciler)):
    print(f"{i+1}. Öğrenci: {ogrenciler[i]}")

#her bir elemanı tek tek gösterir. elemanlar ile çalışır. 
for i in ogrenciler:
    print(f"Öğrenci: {i}")


#break => index değeri 3'den büyük olunca döngüden çık.
for i in range(len(ogrenciler)):
    if i>3:
        break
    print(f"{i+1}. Öğrenci: {ogrenciler[i]}")


#continue => döngü Recep'e gelince; Recep'i atla ve öngüye devam et.
#iterasyondaki current değeri tla, bir sonraki değer ile devam et
for ogrenci in ogrenciler:
    if ogrenci == "Recep":
        continue
    print(f"Öğrenci: {ogrenci}")


#While
i = 0
while i < 10:
    print("Merhaba")
    i = i + 1
    # i += 1

#sonsuz döngüye girer. Ne zaman biteceğini belirtmen gerekir
""" i = 0
while i < 10:
    print("Merhaba") """




