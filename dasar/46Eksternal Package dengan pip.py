# Menggunakan dan Install Eksternal Package dengan pip

#  penjelasan Menggunakan dan Install Eksternal Package dengan pip
# ada di video :
# link   https://youtu.be/EC_N9sSLYLc
# atau dikomputer E:\belajar\code\python\VideoTutorialPython

"""
Menggunakan dan Install Eksternal Package dengan pip
*syarat - syarat
- python sudah diinstal
- koneksi internet
- dependency

*cara menginstal
pip install (nama Eksternal Package)     ,contoh:
pip install numpy

*cara uninstal Eksternal Package
pip uninstall (nama Eksternal Package)     ,contoh:
pip uninstall numpy
"""

## JIKA INGIN MENJALANKAN salah satu PROGRAM SILANGKAH HAPUS """"""

# contoh penggunaan Eksternal Package

### Eksternal Package numpy
"""
## perbedaan list biasa dan list menggunakan numpy
#list biasa
a = [1,2,3,4]
b = [5,6,7,8]

print(a+b) # jika list biasa ditambahnya maka disambung

# menggunakan numpy
import numpy as np

c = np.array([1,2,3,4])
d = np.array([5,6,7,8])

print(c+d) # ditambah perkomponen 
"""

### Eksternal Package Pillow. Pillow itu untuk image prosecing
from PIL import Image

im = Image.open("fotoElang.jpg")

print("format file: "+ im.format)
print("ukuran file: "+ str(im.size))
print("mode file: "+ im.mode)

im.show() # menampilkan fotonya