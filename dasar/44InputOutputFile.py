# Input dan Output File .txt
# menuliskan sebuah data kedalam text

"""
w = write mode/ mode menulis dan menghapus file lama, jika file tidak ada maka akan dibuat file baru
r = read mode only/ hanya bisa baca
a = appending mode/ menambahkan data diakhir baris
r+ = write dan read mode
"""


## membuat file baru
file = open("data.txt",'w')

file.write("ini adalah data text yang dibuat dengan python")
file.write("\nini baris kedua")
file.write("\nini baris ketiga")
file.write("\nini baris keempat")

file.close()  # setelah open jangan lupa close

## membaca file text
file2 = open("data.txt",'r') 

print(file2.read()) # membaca semua
# print(file2.read(10)) # (10) artinya dia akan menampilkan hanya 10 karakter
# print(file2.readline()) # membaca perbaris/ hanya satu baris saja
# print(file2.readline())

file2.close()

## appending mode
file3 = open("data.txt",'a') 

file3.write("\nbaris ini dibuat dengan menggunakan mode append")

file3.close()