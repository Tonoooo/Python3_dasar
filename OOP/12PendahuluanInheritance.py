# Pendahuluan Inheritance

# Inheritance(pewarisan) = sesuatu yang diwariskan atau diturunkan
# Inheritance ini berlaku dari class ke class 
# class utama/pertama disebut super class dan pewarisnya disebut sub class

# Pejelasan Pendahuluan Inheritance
# lebih baik tonton video penjelasannya
# videonya link: https://youtu.be/G6fmTwxx8rw
# atau di komputer : E:\belajar\Programming\python\VideoTutorialPytho


# super class
class Hero:

    def __init__(self,nama,health):
        self.nama = nama
        self.health = health

# sub class
# kelakuan sub class sama dengan kelakuan super class
class Hero_intelejen(Hero): # didalam kurung kita bisa msukkan nama super classnya (Hero) jadi si class ini mewarasi/turunan class Hero
    pass

class Hero_streng(Hero):
    pass

tono = Hero('tono',100)

suep = Hero_intelejen('suep',50) # suep ini ada di class Hero_intelejen yang mendapatkan warisan dari class Hero
print(suep.__dict__) # suep memiliki variabel yang diwariskan class Hero
print(suep.nama) 

adom = Hero_streng('Adom',25)
print(adom.nama)