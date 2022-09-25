# Class Abstract
# Bisa dikatakan bahwa abstract class itu blueprint atau kerangka dari class berikutnya(sub class).

# Pejelasan Class Abstract
# lebih baik tonton video penjelasannya
# videonya link: https://youtu.be/oLloOdOmCdQ
# atau di komputer : E:\belajar\Programming\python\VideoTutorialPytho

# abstrak class dia akan memaksa class inheritace(sub class nya) untuk 
#   mengimplamentasikan metodnya ke sub classnya. kalo tidak diimplamentasikan bakal error
# kalo mau pake abstrak class harus menggunakan sub class
# Abstract Class tidak bisa langsung ke inheritance objek harus ke sub class dulu
#   jadi kalo mau pake abstrak class harus dari abstrak class ke pewarisclassnya(sub class) lalu ke objek

## membuat Class Abstract
# abc = abstract base class
from abc import ABC,abstractmethod

# kalo mau pake Class Abstract harus menginherit ABC
class Tombol(ABC):

    # lalu kita akan memaksa subclass untuk mengimplamentasikan metod ini, dengan cara @abstractmethod
    @abstractmethod 
    def klik(self): # ini ada abstractmethod yang membuat metod ini dipaksakan untuk diimplementasikan disubclassnya
        pass

    def kliknyala(self):        # method ini tidak harus ada disubclass tapi bisa digunakan disubclass
        print("tombol menyala") # karna ini bukan abstrakmetod yang berarti subclass tidak harus mengimplamentasikan metod ini didalamnya
                                # tapi tetap bisa digunakan olehnya, tidak seperti metod yang pakai @abstractmethod(disebutnya abstrakmetod) yang harus mengimplamentasikan metodnya didalamnya kalo tidak nanti error

class Pushtombol(Tombol): # ini sub classnya

    # ini pengimplementasian abstrak metod, kalo tidak diimplementasi nanti error
    def klik(self):
        print("tombol klik")
    

"""
tombol2 = Tombol()  # kita tidak bisa membuat objek dari class abstrak
tombol2.klik()
"""
tombol1 = Pushtombol() # kita harus lewat sub class
tombol1.klik()
tombol1.kliknyala()

# salah satu kegunaannya Class Abstract misalkan kita punya Pushtombol/tipe tipe tombol yang banyak dan kita sudah
#   membuat disain bahwa class yang berhubungan dengan Tombol itu harus punya klik

# kalau pake abstract itu jadi kita memaksa metod harus dibuat di class anaknya. Bisa dikatakan bahwa abstract 
#   class itu blueprint atau kerangka dari class berikutnya.Contohnya tadi itu klik, jadi semua anak-anaknya harus 
#   terdapat metod klik sendiri-sendiri dan itu menjadi kerangka atau dasar dari anaknya