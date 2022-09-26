# Class Abstract dan Decorator

# Pejelasan Class Abstract dan Decorator
# lebih baik tonton video penjelasannya
# videonya link: https://youtu.be/nNWkm-Kv4Ps

# Python memiliki sebuah fitur menarik bernama decorator yang berfungsi menambah fungsionalitas pada kode program


## membuat Class Abstract
# abc = abstract base class
from abc import ABC,abstractmethod, abstractmethod


"""
class Tombol(ABC): # kalo mau pake Class Abstract harus menginherit ABC

    # ini bukan abstrakmetod
    def __init__(self,set_link):
        self.link = set_link

    # ini abstrakmetod 
    @abstractclassmethod 
    def klik(self):
        pass

# ini sub classnya
class Pushtombol(Tombol): 
    def klik(self):
        print("Go to : {}".format(self.link))
"""

## hubungan abstrak metod dari classabstrak dengan decorator(decorator yang pake @ seperti: @poperty,Dll) yang sudah ada dipython
# contoh:
# gimana caranya jika kita mau memaksa implementasi self.link ada di sub class Pushtombol 
#   bukan diclass abstrak (Tombol)? caranya pakai getter setter:

class Tombol(ABC): # kalo mau pake Class Abstract harus menginherit ABC

    # ini bukan abstrakmetod
    def __init__(self,set_link):
        self.link = set_link # ini sebenarnya adalah sama seperty setter

    # ini abstrakmetod 
    @abstractmethod 
    def klik(self):
        pass

    #1. pakai decorator property & abstrakmetod 
    @property
    @abstractmethod #urutannya property lalu abstractmethod lalu metodnya
    def link(slef): # karna pakai property yang tadinya link itu atribut sekarang menjadi metod tapi juga tetep atribut
        pass  # nah kalo begini link nya harus diimplementasikan ke subclassnya


# ini sub classnya
class Pushtombol(Tombol): 
    def klik(self):
        print("Go to : {}".format(self.link))
    
    #2. mengimplementasikan linknya
    # cara mengakses property dari class Tombol maka taro Tombol setelah @  barulah metod propertynya
    @Tombol.link.setter 
    def link(self,input):
        self.__link = input  # link nya jadi privet variabel 
    # lalu kita tambahkan getternya 
    @link.getter # kita tidak usah tambah kan Tombol disitu karna diatas sudah ada (@Tombol.link.setter) jadi sudah tau
    def link(self):
        return self.__link


tombol1 = Pushtombol("https://youtu.be/nNWkm-Kv4Ps")
tombol1.klik()
