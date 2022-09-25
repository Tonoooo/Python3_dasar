# sumber : https://youtu.be/upngNSC9FU8
# Class variables dan Instance variables
# instance variabel adl variabel variabel (nama,helth,power,armor) akan di miliki oleh si objek(seprti hero1) saja
# class variable khusus untuk siclass nya dan instace variabel khusus untuk siinstace/objeknya
# kalo variabel instance akan nempel di objeknya(hero1,hero2..), tapi kalo class variabel akan nempel diclassnya


class Hero:  # ini tamplate
    # class variable / variabel statik. variabel ini akan nempel diclass
    jumlah = 0 # saat programnya dimulai jumlah akan nol, lalu setiap objeknya dibuat maka tambah 1. jadi jumlahnya bakal berubah setiap kita membuat objek baru
    
    def __init__(self, inputNama,inputHealth, inputPower, inputArmor): 
        # instance variabel. variabel ini akan nempel di objek
        self.nama = inputNama # ini instance variabel
        self.health = inputHealth
        self.power = inputPower 
        self.armor = inputArmor 
        Hero.jumlah += 1 # saat objek class hero dibuat kita tambah 1 divariabel jumlah . jadi jumlahnya bakal berubah setiap kita membuat objek baru
        print("membuat hero dengan nama ", inputNama)


# ini pembuatan objek
hero1 = Hero("Tono",1000,1000,1000) 
print(Hero.jumlah)
hero2 = Hero("Taat",100,500,200)
print(Hero.jumlah)
hero3 = Hero("Adom",100,200,150)
print(Hero.jumlah)
