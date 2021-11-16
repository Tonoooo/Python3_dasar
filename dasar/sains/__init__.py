# folder sains ini pasangannya   Package.py

# file __init__.py ini yang bakal dieksekusi setiap kita memanggil si folder sains ini
# jika kita mengimport sains dia akan mengekseskusi __init__.py

# saat kita memanggil folder sains kita bisa mengakses fungsi tambah,kecepata,fisika aja,fisika,matemaktika dengan lebih mudah dan fleksible
# caranya:

from .matematika import *  ## dot(.) artinya folder sekarang ambil matematika,dan * artinya ambil semuanya
from .fisika import *