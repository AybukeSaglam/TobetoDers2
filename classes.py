class Human:
    #property,attribute => nitelik, özellik
    # name = "İrem"
    # age = 25   #bu şekilde değer verme best pratice değildir.

    def __init__(self) -> None:
        print("Yapıcı blok çalıştı")
    
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        print("Yapıcı blok çalışıyor")

    #method,davranışlar
    def talk(self, message):  #class içinde def. tanımlarsan, self kullan
        print(message)
    
    def walk(self):
        print(f"{self.name} is Walking")


#instance üretmek => örnek ürettiğimi belirtiyorum.
human1 = Human("Şeyma", 24) #init def tanımlayacaksan burada yazmalısın
human1.name = "Şeyma"  #değişken
human1.age = 24        #değişken
human1.talk("Merhaba") #definition
human1.walk()          #definition 


