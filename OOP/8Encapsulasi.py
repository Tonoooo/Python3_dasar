# Encapsulasi
# sumber : https://youtu.be/NDjX-8kak2g

##Enkapsulasi (encapsulation) adalah sebuah metoda untuk mengatur 
#  component class dengan cara menyembunyikan alur kerja dari class tersebut.
#  Component class yang dimaksud adalah property dan method.
## aturan Encapsulasi:
# -buat semua variabel private
# - getter(untuk mengambil variabel) dan setter(untuk menseting variabel)
##jadi intinya si Encapsulasi menprotec varibelnya(__nama,__health,__atekPower)
#  kita jaga agar tidak dirubah dengan mudah dari luar (luar class)

class Hero:
    def __init__(self,nama,health,atekPower):
        # buat terlebih dahulu semua variabel private
        self.__nama = nama
        self.__health = health
        self.__atekPower = atekPower
        # encapsulasi -> kita memprotek semua variabel diatas, kita jaga agar tidak dirubah dengan mudah dari luar

    # getter(untuk mengambil variabel)
    # kan __nama sifat nya privet agar bisa ambil namanya maka kita gunakan getter
    def ambilnama(self):
        return self.__nama
    # kita ingin sihealt itu dia akan berubah kalo diserang tapi kita tidak ingin dirubah langsung 
    def ambilhealth(self):
        return self.__health
    
    # setter(untuk menseting )
    def diserang(self,serangPower):
        self.__health -= serangPower
    def setatpower(self,nilaibaru):
        self.__atekPower = nilaibaru

# awal dari game
tono = Hero("Tono",100,5)

# game berjalan
#print(tono.__nama)   # karna privet jadi kita tidak bisa akses/ambil namanya
print(tono.ambilnama())
print(tono.ambilhealth())
tono.diserang(10) # tono diserang dengan attack power nya 10
print(tono.ambilhealth())

