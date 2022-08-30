# sumber https://youtu.be/pZye35-Nx4o
## ~~~~~ fungsi lambda
# fungsi biasa
def f_kuadrat(angka):
    return angka**2

print(f"hasil fungsi biasa kudrat = {f_kuadrat(5)}")

# dengan lambda
#output = lambda argument: expression
kuadrat = lambda angka:angka**2 # otomatis nge return
print(f"hasil fungsi lambda = {kuadrat(5)}")

# contoh lambda 2 argumen
pangkat = lambda num,pow : num**pow
print(f"fungsi lambda 2 arg = {pangkat(5,2)}\n")#5 pangkat 2

## kegunaannya
# sorting untuk list biasa pake fungsi bawaan
data_list = ["otongg","zucup","ana"]
data_list.sort() # menggunakan fungsi sort bawaan
print(f"sorted list biasa = {data_list}")
# sorting pake panjang
data_list.sort(key=len) # mengurutkan sesuai panjangnya
print(f"sorted list by len = {data_list}")
#sama tapi kita pake fungsi sendiri (ribet)
def panjang_nama(nama):
    return len(nama)
data_list.sort(key=panjang_nama) # mengurutkan sesuai panjangnya dengan key fungsi sendiri
print(f"sorted list by panjang = {data_list}")

# sort pakai lambda
data_list = ["otongg","zucup","ana"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by lambda = {data_list}")

# ~~~~ kegunaan yang lebih nyata. filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

# kasus ambil angka yang kurang dari lima
def kurang_dari_lima(angka):
    return angka < 5
data_angka_baru = list(filter(kurang_dari_lima,data_angka))
#pake lambda agar lebih simple
data_angka_barulmd = list(filter(lambda x:x<5, data_angka))
print(f"filter = {data_angka_baru}")
print(f"filter = {data_angka_barulmd}")

# kasus genap
data_genap = list(filter(lambda x:(x%2==0), data_angka))# berapapun angka itu jika dibagi 2 lalu sisa baginyahasilnya samadengan 0 maka itu genap
print(f"genap = {data_genap}")

# kasus ganjil
data_ganjil = list(filter(lambda x:(x%2!=0), data_angka))# berapapun angka itu jika dibagi 2 lalu sisa baginyahasilnya tidaksamadengan 0 maka itu ganjil
print(f"ganjil = {data_ganjil}")

# kasus kelipatan3
data_kelipatan3 = list(filter(lambda x:(x%3==0), data_angka))# berapapun angka itu jika dibagi 3 lalu sisa baginyahasilnya samadengan 0 maka itu kelipatan3
print(f"kelipatan3 = {data_kelipatan3}")

## ~~~~~~~ fungsi anonymous
# salah satu namanya adalah currying <- Huskell Curry
print("~~~~~~~~ fungsi anonimus")
# fungsi biasa
def dipangkat(angka,n):
    return angka**n
pangkat_pangkat = dipangkat(5,2)
print(f"fungsi pangkat biasa = {pangkat_pangkat}")
#     dengan fungsi anonymous
# fungsi currying / anonimos ini membuat si fungsi itu gak pasti
#dan kita bisa men asign dia menjadi variabel yang bersifat seperti fungsi. langsung buat fungsi anonimus:
def pangkatin(n):
    return lambda angka:angka**n # direturnnya dimasukin fungsi lambda
# misal kita bikin variabel untuk pangkat 2. otomatis akan menjadi fungsi 
pangkat2 = pangkatin(2) # saat kita memasukkan isi parameter, otomatis pangkatin(2) jadi lambda angka:angka...
print(f"pangkat 2 = {pangkat2(5)}")

pangkat3 = pangkatin(3)
print(f"pangkat 3 = {pangkat3(3)}")

print(f"pangkat bebas = {pangkatin(4)(5)}") # 5 pangkat 4

# jadi "variabel" pangkat2 dan pangkat3 itu adalah fungsi tapi
#fungsinya itu berbasis dari fungsi pangkatin tapi kita bisa
#merubah parameter didalamnya 