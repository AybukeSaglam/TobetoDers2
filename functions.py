#definition => tanımlama

def ortalamaHesaplama():
    final = 69
    vize = 87
    ortalama = (vize*0.4) + (final*0.6)
    print(ortalama)


def ortalamaHesaplamaVeDöndür():
    final = 75
    vize = 80
    ortalama = (vize*0.4) + (final*0.6)
    return ortalama

def ortalamaHesapla(vize,final):
    return (vize*0.4) + (final*0.6)

vize = int(input("Vize notunuz: "))
final = int(input("Final notunuz: "))

def ortalamaHesaplaVeYazdır(vize=vize, final=final):
    return(vize*0.4) + (final*0.6)







ortalamaHesaplama()   #fonksiyon çağırma
print(ortalamaHesaplamaVeDöndür())  #return'de print olmadığı için
print(ortalamaHesapla(50,78)) #değerleri sen giriyorsun
print(ortalamaHesaplaVeYazdır) #değerleri başta input ile aldık



