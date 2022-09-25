# Methods
# method itu seperti fungsi/functon

# penjelasan Methods 
# ada di video https://youtu.be/DE-h_oR8Nmo
# atau di komputer : E:\belajar\Programming\python\VideoTutorialPytho


class Hero():
    # class variabel
    jumlah_hero = 0

    def __init__(self, input_nama, input_power, input_health, input_armor):
        self.nama = input_nama
        self.power = input_power
        self.health = input_health
        self.armor = input_armor
        Hero.jumlah_hero += 1
    ## method terbagi menjadi tiga:
    # 1. void function, method tanpa return dan tanpa ergument
    def siapa(self): # pake self karna ini nempel sama objeknya
        print("namaku adalah ", self.nama)
    
    # 2. method dengan argument
    def healthUp(self,up):
        self.health += up
    
    # 3. method dengan return. mengembalikan nilai
    def gethealth(self):
        return self.health


# membuat objek
hero1 = Hero("Tono",100,100,100)
hero2 = Hero("suep",90,100,80)

# menggunakan method
hero1.siapa()
hero1.healthUp(10) # masukkan () argumen untuk menaikan health 
print(hero1.gethealth())