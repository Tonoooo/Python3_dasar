# Try and Exception
# di pemrograman ada dua tipe error: error yang bisa dideteksi oleh kompiler (error syntax), dan runtime error 

# penjelasa Try and Exception
# ada di video :
# link https://youtu.be/WSCQt2x1bcU
# atau dikomputer E:\belajar\code\python\VideoTutorialPython

## JIKA INGIN MENJALANKAN salah satu PROGRAM SILANGKAH HAPUS """"""

## contoh syntax error
"""
print(halloo hai)  # error ini dapat dideteksi oleh di pycharm nya
"""

## contoh error runtime
""" 
angka = int(input("masukkan angka sembarang?\n"))
print(angka)  # masukkan huruf jangan angka dan lihatlah itu yang disebut error runtime
"""
# contoh lain error runtime
"""
def pembagian(a,b):
    return  a/b
penyebut = input("masukkan angka sembarang?\n")
pembilang = input("masukkan angka sembarang?\n")

print(pembagian(penyebut,pembilang))  # masukkan angka jangan huruf dan lihatlah itu yang disebut error runtime
"""
# contoh lain error runtime yang ada ZeroDevisionError

""" 
def pembagian(a,b):
    return  a/b
penyebut = int(input("masukkan angka sembarang?\n"))
pembilang = int(input("masukkan angka sembarang?\n"))

print(pembagian(penyebut,pembilang))  # masukkan penyebut: 1 dan pembilang: 0 dan lihat nanti ada ZeroDevisionError
"""

# error error seperti itu berbahaya kenapa?, karna nanti saat runtime error itu nanti program kita langsung close . Misalnya kita punya looping
#     tiba tiba ada error ditengah membuat program kita berhenti saat itu juga.
# Cara jika ada erro seperti itu kita bisa dihiraukan dan lanjut ke step berikutnya pake error handling.
### Cara error hendling menggunakan Try and Exception

# contoh paling gampang
"""
try:
    a = 1/0
except:
    print("error pembagi nol")

print("ini adalah akhir dari program")
"""

# contoh lain Try and Exception di while loop
"""
while True:
    try:
        angka = int(input("masukkan angka: "))  # masukkan huruf jangan angka dan lihatlah
        break
    except:
        print("yang anda masukkan bukan angka")

print("berhasil, anda memasukkan angka: ",angka)
"""

# contoh lain dan cara menanggapi ValueError dan ZeroDevisionError
"""
print("ini adalah program pembagian")
while True:
    try:
        penyebut = int(input("masukkan angka penyebut: "))
        pembilang = int(input("masukkan angka pembilang: "))
        hasil = penyebut/pembilang
        break
    except ValueError: # artinya jika ValueError lakukan ini:. ini berguna jika yang dimasukkan bukan angka
        print("yang anda masukkan bukan angka\n")
    except ZeroDivisionError: # ini berguna jika ada nol/ZeroDivisionError maka lakkukan ini:
        print("angka yang anda masukkan adalah nol, masukkan yang lain ya..\n")

print("berhasil, hasil pembagian adalah: ",hasil)
"""

# contoh Try and Exception yang lebih umum
# dan ini jadi nya bahasa ingris
"""
print("ini adalah program pembagian")
while True:
    try:
        penyebut = int(input("masukkan angka penyebut: "))
        pembilang = int(input("masukkan angka pembilang: "))
        hasil = penyebut/pembilang
        break
    except Exception as err:  # jadi kita ambil si Exception sebagai err
        print(err)
    # jadi si Exception nya akan menanggapi error dan nanti hasilnya akan bahasa ingris.
    # misalkan ada ValueError / ZeroDivisionError dia akan menanggapinya error tersebut tapi menggunakan bahasa inggris dan tapi programnya tetap berjalan tidak akan stop.
    # coba masukkan penyebut angka bebas tapi pembilangnya huruf jangan angka dan lihat apa yang terjadi, si Exception nya akan menanggapi tapi pake bhs inggris
    # coba masukkan penyebut bebas tapi pembilangnya 0 dan lihat apa yang terjadi, si Exception nya akan menanggapi tapi pake bhs inggris

print("berhasil, hasil pembagian adalah: ",hasil)
"""


#### ada beberapa  tipe error:
"""
type of Exception errors:
1. IOError = input output error
2. ImportError = import error. misalkan kita mengimport modul/package yang gak ada
3. ValueError
4. Division by zero
5. KeyboardInterupted
6. EOFError
"""