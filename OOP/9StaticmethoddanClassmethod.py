# Staticmethod dan Classmethod
# sumber : https://youtu.be/r8QcqWXUy2k
# membuat encapsulasi diclass hero

class Hero:

    # variabel class privet
    __jumlah = 0

    def __init__(self,nama):
        self.__nama = nama
        Hero.__jumlah += 1 # kita tambahkan setiap objek baru
    
    # method ini hanya berlaku untuk objek
    def ambiljumlah(self):
        return Hero.__jumlah

    # method ini tidak berlaku untuk objek tapi berlaku untuk class
    def ambiljumlah1():
        return Hero.__jumlah

    # method static (decorator)
    #kita ingin metod yg bisa/nempel untuk objek dan class maka pake method static
    @staticmethod   # agar methodnya jadi Staticmethod pake lah @staticmethod
    def ambiljumlah2():
        return Hero.__jumlah

    # Classmethod
    # kita ingin benar benar nempel diclass , pakelah Classmethod
    @classmethod   # agar methodnya jadi Classmethod pake lah @classmethod
    def ambiljumlah3(cls):  # cls artinya class, knp pake cls tdk pke Hero?,karna jika suatu saat kita ingin merubah  
        return cls.__jumlah #  nama classnya kita tidak perllu lagi merubah nama yang ada diSini. jadi lebih elegan dan reusable


tono = Hero('Tono')
# print(Hero.__jumlah) # error karna var jumlah adalah privaet.
print(Hero.ambiljumlah1()) # mengambil jumlah, pake method ambiljumlah1. method ini hanya untuk class
print(tono.ambiljumlah()) # mengambil jumlah, pake method ambiljumlah1. method ini hanya untuk objek

suep = Hero("Suep")
# pake method ambiljumlah2 (ini static metho)
print(suep.ambiljumlah2()) # dengan objek
print(Hero.ambiljumlah2()) # dengan class

adom = Hero("Adom")
print(adom.ambiljumlah3())
print(Hero.ambiljumlah3())

# jadi bedanya kalo Staticmethod itu dia gak ngambil argumen dari objek ataupun class
# tapi kalo Classmethod dia bisa ngambil argumen.
# argumen yaitu kalo fungsi itu misalnya: def namanya(disini tempat argumen)