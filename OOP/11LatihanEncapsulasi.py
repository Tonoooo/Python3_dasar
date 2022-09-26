# Latihan Encapsulasi

# Pejelasan Latihan Encapsulasi
# lebih baik tonton video penjelasannya
# videonya link: https://youtu.be/rakQ1ji9XRM


class Hero:

    __jumlah = 0

    def __init__(self,nama,health,attpower,armor):
        self.__nama = nama
        self.__healthstandar = health
        self.__attpowerstandar = attpower
        self.__armorstandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthmax = self.__healthstandar * self.__level
        self.__attpower = self.__attpowerstandar * self.__level
        self.__armor = self.__armorstandar * self.__level

        self.__health = self.__healthmax

        Hero.__jumlah += 1
    
    @property
    def info(self):
        return "{} \tlevel : {} \n\thealth - {}\{} \n\tatttack = {} \n\tarmor = {}".format(self.__nama,self.__level,self.__health,self.__healthmax,self.__attpower,self.__armor)
    
    # kita akan buat sebuah method getter setter untuk  experion
    @property
    def gainexp(self):
        pass

    @gainexp.setter
    def gainexp(self,addexp):
        self.__exp += addexp
        if (self.__exp >= 100): # jika exp nya lebih besar 100 mka dia akan naik level
            print("level up")
            self.__level += 1
            self.__exp -= 10
            # kita reset/update semuanya
            self.__healthmax = self.__healthstandar * self.__level
            self.__attpower = self.__attpowerstandar * self.__level
            self.__armor = self.__armorstandar * self.__level

    def serang(self,musuh):
        self.gainexp = 50


tono = Hero('Tono',100,5,10)
suep = Hero('Suep',100,5,10)

print(tono.info)

tono.serang(suep) 
tono.serang(suep)
# karna setiap kali tono nyerang otomatis menambah experion yang jika exp nya 
# nambah terus lebih besar 100 mka dia akan naik level

print(tono.info)

# 
print(tono.gainexp) # pasti hasilnya none. jadi yang bisa dilihat oleh clien/musuh itu hanya info saja, 
# gainexp tidak bisa ddilihat oleh dia
