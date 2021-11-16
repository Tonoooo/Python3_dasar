# ini pasangannya  folder sains
## Membuat Package
# package itu folder
# Package adalah kumpulan dari modul modul
# gunanya untuk mempermudah kerjaan,dan lebih rapih, tertata

### JIKA INGIN MENJALANKAN salah satu PROGRAM SILANGKAH HAPUS """"""


# penjelasa Menmbuat Package
# ada di video :
# link https://youtu.be/y3XBTeyAA-E

# cara memanggil/menggunakan package
## cara 1. cara biasa
"""
from sains import fisika,matematika

fisika.kecepatan(50,10)
matematika.tambah(4,5)"""

## cara 2. cara yang fleksibel cara ini sangat berhubungan erat dengan __init__.py . lebih baik lihat dulu __init__.py
# cara pertama 
"""
import sains   # jika kita mengimport sains dia akan mengekseskusi __init__.py
sains.kecepatan(4,5)
sains.tambah()
sains.kurang()
sains.waktu_tempuh()
"""
# cara kedua
"""
from sains import tambah,kecepatan
tambah(3,4)
kecepatan(6,5)"""
