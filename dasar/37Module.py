# ini pasangannya  mtk.py

##### cara mengakses module dengan menggunakan import

### JIKA INGIN MENJALANKAN salah satu PROGRAM SILANGKAH HAPUS """"""


## cara 1. 
"""
import matematika

matematika.tambah(3,4)
matematika.kurang(5,4)
"""



## cara 2. 
"""
import matematika as m  # as adalah sebagai, jadi matematika sebagai m

m.tambah(3,4)
m.kurang(5,4)
"""



## cara 3. meng import tapi lebih spesifik
"""
from matematika import tambah,kurang
tambah(4,5)
kurang(5,4)"""
"""
# jika ingin mengambil semuanya
from matematika import *  # tanda bintang ini artinnya mengambil semuanya
tambah(4,5)
kurang(5,4)"""


## cara 4. 
"""
from matematika import tambah as t  # dari matematika impor tambah sebagai t
t(5,5)"""