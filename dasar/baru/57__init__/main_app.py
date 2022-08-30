# package adalah folder
# modul adalah file. contohnya ini main_app.py
# import
#cara import/mengambil variabel dari modul/file.py lain adalah dengan cara
#contoh: import nama_file
#print(nama_file.nama_variabel)
# from 
#caranya: from nama_package import nama_file.

# sumber : https://youtu.be/7GhxT1svylc

# didalam package / folder sains terdapat file __init__.py
#fungsi file __init__.py adalah di eksekusi saat kita import package
import sains

# karna difile __init__ folder matematika kita telang mengimport fungsi tambah & kali
#jadi disini kita tidak perlu ngetik file basicnya.
hasil_tambah = sains.matematika.tambah(1,2,3,4,5,6,7)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = sains.matematika.kali(1,2,3,4,5,6)
print(f"hasil kali = {hasil_kali}") 

hasil_pisika = sains.pisika.gaya(10,9.8)
print(f"hasil pisika = {hasil_pisika}")

# jika kita ingin langsung
from sains.matematika import scientific
pangkat3 = scientific.pangkat(3)
print(f"hasil pangkat 3 = {pangkat3(5)}")

# from sains import * # ini berpasangan dengan __all__ difile init sains. ini tidak disarankan