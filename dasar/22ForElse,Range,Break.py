# For Else, Range, Break

## JIKA INGIN MENJALANKAN salah satu PROGRAM SILANGKAH HAPUS """"""

"""
for i in range(0,10):  # ini akan menampilkan 0 sampai sebelum 10, kenapa tidak ada sepuluh? karna emang yang terakhir tidak ditampilkan
    print(i)

for i in range(10,40,5): # artinya dimulai dari 10 sampai 40 dengan Increment/loncat 5
    print(i)
"""

"""
for i in range(0,5):
    print(i)
else:  # else ini dia akan ngeprint setiap for ini telah mencapai looping akhirnya
    print("heloo") # dan salah satu fungsi else ini adalah untuk ngecek for ini sampai diakhir 
"""


number = 25
for i in range(0,40):
    print(i)
    if i is number:  # jika i adalah nnumber maka:
        print("angka ditemukan ",i)
        break  # break ini akan membuat keluar dari proses looping 
else:  # jika benar maka else ini akan dilewat karna jika benar break akan keluar dari looping,tp jika angka tdk ketemu maka else tampil
    print("angka tidak ditemukan")
print("space diluar for")
