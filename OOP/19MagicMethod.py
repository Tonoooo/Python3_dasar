# Magic Method
# tanda atau ciri Magic Method: awal dan akhir namanya pakai dable underscore(__)
#   contoh: __init__,__dict__,__repr__,__str__,dll



class Mangga:

    ### magic mathod

    ## 1. init merupakan salah satu magic mathod, fungsi init = dia akan dipanggil saat kita membuat class mangga
    def __init__(self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah

    ## 2.__repr__ dan __str__
    # repr fungsinya= kan biasanya kita saat ngeprint objek(contoh:print(belanja1)) hasilnya: <__main__.Mangga object at 0x000001985D351FD0>
    # kita bisa mengganti hasil output tersebut dengan semau/secreatif/terserahbebas kita dengan menggunakan repr
    # repr dipakainya saat debuging 
    def __repr__(self):
        return "Debug: Mangga : {} dengan jumlah : {}".format(self.nama,self.jumlah)
    # __str__   = kelakuannya sama kaya repr
    # __str__ fungsinya= kan biasanya kita saat ngeprint objek(contoh:print(belanja1)) hasilnya: <__main__.Mangga object at 0x000001985D351FD0>
    # kita bisa mengganti hasil output tersebut dengan semau/secreatif/terserahbebas kita dengan menggunakan __str__
    # str dipakai untuk kalo programnya sudahjadi atau sudah produksi, pakainya str
    # kalo repr dipakainya saat debuging 
    # cara manggil str print(objek) dan karna ada str jadi mau manggil repr tidak bisa seperti 
    # print(objek) jadi seperti print(repr(objek)), tapi kalo tidak ada str kita bisa
    # pakai print(objek).
    # jadi gak ada bedanya sih tinggal pilih aja mau pakai mana
    # tapi kebanyakan pakai __str__
    def __str__(self):
        return "Mangga : {} dengan jumlah : {}".format(self.nama,self.jumlah)

    ## 3. __add__
    # berguna untuk aritmatika. 
    # add harus masukkin argumen/input
    def __add__(self,objek):
        return self.jumlah + objek.jumlah
    
    ### 4. __dict__  = dictionary
    # ini kita mencari tau apa saja yang ada di si objek ini
    # cara menggunakannya:
    # print(namaobjek.__dict__)

    # cara mengubah hasil outputnya 
    # yang biasanya contoh: print(belanja1.__dict__) outputnya {'nama': 'arumanis', 'jumlah': 10}
    # kita bisa mengganti hasil output tersebut dengan semau/secreatif/terserahbebas
    @property  #pakai property
    def __dict__(self):
        return "objek ini mempunyai nama dan jumlah" 



belanja1 = Mangga("arumanis", 10)
belanja2 = Mangga("mana lagi", 5)

# cara memanggil/mengakses repr
print(repr(belanja1))
# cara memanggil/mengakses __str__ 
print(belanja2) # repr bisajuga manggilnya seperti ini tapi jika tidak pakai __str__

print(belanja1+belanja2)

# cara memanggil/mengakses dict
print(belanja1.__dict__)