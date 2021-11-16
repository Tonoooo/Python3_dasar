### tipe data tuple
# tuple itu tidak bisa dirubah nilainya, nilai tuple itu tetap
# kalo list nilai nya bisa dirubah tapi tuple nilainya tetap
# tuple ini berguna kalo misalkn kita punya data tetap(gak bisa dirubah),misalnya data nomor induk, nomor ktp, 
# dan list dan tuple lebih ringan tuple untuk diproses


# contoh list
Ganjil = [1,3,5,7,9]  # ciri list pake []
print(type(Ganjil))  # ngecek tipe data

# ini Tuple
Genap = (2,4,6,8,10)  # ciri tuple pake ()
print(type(Genap)) # ngecek tipe data

print(Genap.count(6)) # ngecek ada berapa 6 di genap
print(Genap.index(8)) # ngecek posisi 8 ada dimana

# lanjut ke testTuple1.py dan testTuple2.py