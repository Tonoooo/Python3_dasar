#4. Private attribute merupakan sebuah attribute yang tidak dapat diakses diluar class untuk membuat Private Attribute Pada
#     pemprograman Python kita menggunakan double underscore (__) pada awal atribut yang kita buat.

# penjelasan Private attribute
# ada di video :
# link https://youtu.be/9quKCsUtXgk

## contoh penggunaan Private attribute
class mahasiswa(): 
    
    jurusan = "teknik tata boga"
    __nilai = 5  # ini Private Attribute(__) gunanya agar orang lain tidak dapat mengakses dan merubahnya

    def __init__(self,input_nama,input_nim): # 
        self.nama = input_nama  # ini public 
        self.nim = input_nim  # ini public 
    
    def uts(self,input_nilai):
        self.__nilai += input_nilai
    
    def uas(self,input_nilai): # input_nilai ini sama input_nilai uts beda karna dia scopenya ada didalam method ini
        self.__nilai += input_nilai
    
    def chek_status(self):
        if self.__nilai <= 50:
            print(self.nama,'tidak lulus')
        else:
            print(self.nama,'lulus')


# main programnya
tono = mahasiswa('tono taat',101)
adom = mahasiswa('adom tono',102)

tono.uts(10)
tono.uas(50)
tono.chek_status()
adom.uts(5)
adom.uas(25)
adom.chek_status()
