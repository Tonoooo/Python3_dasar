# Private Variable dan protected
# sumber : https://youtu.be/6fIc2jV6HfY

# cara buat Private Variable adalah dengan double undercore(__) diawal nama variabelnya, contoh: __nama
# variabel private sifatnya tidak dapat diakses(dan tidak bisa diubah) diluar class 
# jadi hanya untuk class saja

# cara buat variabel protected adalah dengan saatu underscore(_) diawal nama variabelnya, contoh: _nama
# variabel protected sifatnya sama kaya variabel public bisa diakses , 
# tapi apa fungsinya? fungsinya untuk konfensi saja, jadi 
# yang ada underscore satu (_) namanya berarti dia hanya dipakai diclass saja, dan jangan diubah

class Hero:
    # class veriable
    jumlah = 0
    # class variabel private
    __privatjumlah = 0

    def __init__(self,nama,health):
        self.nama = nama  # ini public (bisa diakses nilainya)
        self.health = health  # ini public (bisa diakses nilainya)

        # variabel instance(variabel yg nempel pada objek) private
        self.__privat = "private"
        # varabel instance protected
        self._protected = "protected"



tono = Hero("Tono",100)

print(tono.__dict__) # ini kita mencari tau apa saja yang ada di si tono ini
print(tono.health)  #  kita bisa mengakses variabel ini karna variabel health sifatnya public
#print(tono.__privat)    # kita tidak bisa mengakses variabel ini karna variabel __privat bersifat private
print(tono._protected)  #  kita bisa mengakses variabel ini karna variabel _protected