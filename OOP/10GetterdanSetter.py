# Getter dan Setter

# penjelasan Getter dan Setter
# lebih baik tonton video penjelasannya
# videonya link: https://youtu.be/ZPU1X5C0DaE


# jadi ini cara encapsulasi dengan getter dan setter

class Hero:
    def __init__(self,nama,health,armor):
        self.nama = nama
        self.__health = health
        self.__armor = armor
        #self.__info = "nama {} : \n\thealth: {}".format(self.__nama,self.__health)

    @property  # artinya meruabah sebuah method menjadi seperti variabel
    def info(self): # jadi ini method tapi seperi variabel
        return "nama {} : \n\thealth: {}".format(self.nama,self.__health)
        # jadi keunggulan pake property kita bisa rubah simethod ini(yg diatas) berlaku sbg variable dan si variabel akan update terus

    # mulai materi getter dan setter dan deleter
    @property
    def armor(self):
        pass

    # getter / mengambil nilainya
    @armor.getter  # armor itu nama mathodnya yang diatas (@property def armor(self): pass)
    def armor(self):
        return self.__armor

    # merubah atau setter
    @armor.setter
    def armor(self,masukkan):
        self.__armor = masukkan
    
    # mendelet armor, fungsinya jika suatu saat armor tidak dibukan lg kita bisa menhapusnya jadi lebih hemat memori
    @armor.deleter
    def armor(self):
        print('armor didelet')
        self.__armor = None


tono = Hero("Tono",100,10)

# merubah info
print('--merubah info')
print(tono.info)
tono.nama = 'ToNo'
print(tono.info)

### getter dan setter untuk __armor
print("--getter dan setter untuk __armor")

## getter / mendapatkan nilai armor
print(tono.armor)

## setter / merubah nilai armor
#tono.armor(50) # kan kalo kita dulu mau merubah nulisnya seperti ini, tapi karna 
tono.armor = 50 # kita sudah pake decorator(@armor.__armor) jadi lebih mudah nulis nya,jadi seperti ini
print(tono.armor)

## delete armor
print("--delete armor")
del tono.armor
print(tono.__dict__)

# jadi ini cara encapsulasi dengan getter setter deleter pake decorator property
# yg @armor.getter/setter/deleter itu keyword 'armor' nya merujuk ke property
# salah satu keuntungan pake property di getter setter :
# -meruabah sebuah method menjadi seperti variabel
# -tetep method tpi bisa seperty variabel
# -kan variabel variabelnya privet dengan property getter setter 
#    kita bisa lihat nilai nya seperti variabel
# -lebih simple
# -dan masih banyak lagi
