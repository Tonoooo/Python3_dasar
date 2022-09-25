# Super untuk inheritance
# jadi konsep super yaitu kita mengambil method  yang disuperclass ke subclass


class Hero:

    def __init__(self,nama,health):
        self.nama = nama
        self.health = health

    def showInfo(self):
        print("{} dengan health: {}".format(self.nama,self.health))
        
    def tulis(self):
        print(f"nama saya {self.nama} dan health saya {self.health}")

class Hero_intelejen(Hero):
    def __init__(self,nama):
        #disini kita bisa menggunakan def __init__ milik class Hero:
        #Hero.__init__(self,nama,100) # ini tidak pake super,
        super().__init__(nama,100) # artinya kita mengambil init yang ada di super class (Hero), dan tiak usah pake self karna dia sudah tau ada self
        super().showInfo() # kita mengambil method showinfo
        # keunggulan pake super: jika suatu saat kita mau mengganti superclass kita tidak perlu lagi mengubah ini

class Hero_streng(Hero):
    def __init__(self,nama):
        super().__init__(nama,200) # jadi konsep super yaitu kita mengambil method init yang disuperclass(Hero) ke seni
        super().showInfo()

tono = Hero_intelejen("Tono")
suep = Hero_streng("Suep")

tono.showInfo
suep.showInfo

# karna class Hero_intelejen&Hero_streng mewarisi class Hero, jadi objet
#tono dan suep bisa menggunakan method Hero
tono.tulis()
suep.tulis()