''' Type hints untuk fungsi '''
# sumber : https://youtu.be/NR3m8VJA738

# bentuk standar fungsi yang udah kita pelajari
"""
# studi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)
fungsi(1)
fungsi("Ucup") # ini akan error
fungsi(True) # ini akan error
# saat menggunakannya kita tidak tau harus memasukan parameter
#bertipe apa. Maka dari itu kita pake type hints
"""

## penggunaan type hints
import string

# argument:int   = ini maksudnya kita harus memusakkan parameter
#bertipe integer.   -> int   = fungsi ini akan menguarkan output
#tipe integer
def sepuluh_pangkat(argumentnya:int) -> int:
    '''FUNGSI DENGAN HINTS'''
    output = 10**argumentnya
    return output

HASIL = sepuluh_pangkat(4)
print(HASIL)

# jadi type hints pada fungsi berguna sebagai petunjuk untuk melihat
#tipe data apa untuk input fungsi dan output fungsi tersebut