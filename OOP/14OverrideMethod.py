# Override Method 
# ini masih di inheritance

# jadi kita menimpa fungsi yang di super class 

# Pejelasan Override Method
# lebih baik tonton video penjelasannya
# videonya link: https://youtu.be/sYKhxqcDu3w
# atau di komputer : E:\belajar\Programming\python\VideoTutorialPytho


class Hero:

    def __init__(self,nama,health):
        self.nama = nama
        self.health = health
    def showInfo(self):
        print("showInfo yang ada di class Hero")
        print("{} dengan health: {}".format(self.nama,self.health))


class Hero_intelejen(Hero):
    def __init__(self,nama):   # ini mengambil
        super().__init__(nama,100) 

    # override
    # ini menimpa
    def showInfo(self):   # namanya sama tapi printnya beda ini disebut override/menimpa  
        print("showInfo yang ada di subclass Hero_intelejen")
        print("{} \n\ttipe: intelejen, \n\tdengan health: {}".format(self.nama,self.health))
        # jadi dia meng override sesuatu yang sama

class Hero_streng(Hero):
    def __init__(self,nama):
        super().__init__(nama,200)


tono = Hero_intelejen("Tono")
suep = Hero_streng("Suep")

tono.showInfo()
suep.showInfo()

# showinfo dioveride di Hero_intelejen tapi tidak di Hero_streng