# Pengenalan Class
# membuat method
# menggunakan __init__()
# Private Attribute
# Class Variable
# Class Inheritance

# penjelasan Pengenalan Class dan menggunakan __init__()
# ada di video :
# link https://youtu.be/LPVs38kR6tg  dan  https://youtu.be/yfSPeKVfusw

#1. Kelas atau class pada python bisa kita katakan sebagai sebuah blueprint (cetakan) dari objek (atau instance) yang
#      ingin kita buat. Kelas adalah cetakannya atau definisinya, sedangkan objek (atau instance) adalah objek nyatanya.
#    class harus diatas
#   - Instance adalah istilah lain dari objek suatu kelas
#      segala sesuatu yang ada self nya itu milik si instace, dan yang tidak ada self nya itu milik si class
#2. Method adalah fungsi yang menempel diclass. kalo fungsi aja itu adalah diluar class
#3. init adalah init akan berjalan saat class/mahasiswa dipanggil dia akan langsung menjalankan init.
#      ini berguna kalo misalkan kita mau memasukkan atribut langsung berubah saat menginstaceiet si class.
#      bedanya init dan method lain adalah jika init gausah dipanggil dia sudah jalan sendiri, tapi method lain harus dipanggil baru jalan
#      init itu seperti  inisialisasi atau membuat permulaan.
#  -Attribute sering disebut juga dengan properties merupakan nilai atau data yang terdapat pada suatu object yang berasal dari class.
#      atribut = nilai yang menempel pada class itu.
#4. Private attribute merupakan sebuah attribute yang tidak dapat diakses diluar class untuk membuat Private Attribute Pada
#     pemprograman Python kita menggunakan double underscore (__) pada awal atribut yang kita buat.
#5. Class Variable
#6. Class Inheritance


## class
class mahasiswa():  # mahasiswa punya atribut nama,nilai,nim,... dan punya method belajar,tidur.....
    
    __nilai = 5  # ini Private Attribute(__) gunanya agar orang lain tidak dapat mengakses dan merubahnya

    def __init__(self,input_nama,input_nim): # init akan berjalan saat class/mahasiswa dipanggil dia akan langsung menjalankan init
        self.nama = input_nama  # ini public 
        self.nim = input_nim  # ini public 

    def belajar(self,kondisi):  # self adalah untuk mengidentifikasi si mahasiswa ini dipakai/milik oleh siapa, dan  segala sesuatu yang ada selfnya itu milik si instace 
        print(self.nama,"sedang belajar",kondisi)
    
    def tidur(self):
        print(self.nama,'sedang tidur')

## main programnya
tono = mahasiswa('tono taat',101) # ini disebut instace. saat class/mahasiswa ini dipanggil dia akan langsung menjalankan init
adom = mahasiswa('adom tono',102) # adom itu instace dan mahasiswa adalah class. saat class/mahasiswa ini dipanggil dia akan langsung menjalankan init


print(tono.nama)  #  .nama itu artinya mengambil nama
print(adom.nim)

tono.belajar('dengan giat')
adom.tidur() 
