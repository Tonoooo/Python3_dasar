## Global dan Local scope
# sumber : https://youtu.be/KzinFz7ExJ4
## variabel global bisa diakses didalam fungsi atau dimanapun yang ada titik dua (:)
nama_global = "otong" # <- ini variabel global

# akses variabel global dalam fungsi
def fungsi1():
    print(f"fungsi menampilkan {nama_global}")

fungsi1()

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# akses variabel global dalam percabangan
if True:
    print(f"if menampilkan {nama_global}")
    
## Variabel Local Scope

def fungsi2():
    nama_local = "Ucup" # <- variabel lokal scope

fungsi2()
# print(nama_local) # tidak bisa dilakukan bos

## ~~~~ Contoh 1: penggunaan akses variabel
def say_otong():
    print(f"Hello {nama}")

nama = "Otong"
say_otong()
# itu tidak akan error karna si variabel nama dipanggil sebelum fungsi say_otong

## contoh 2: merubah variabel global
angka = 0
name = "Ucup"

def ubah(nilai_baru, nama_baru):
    global angka # dengan global fungsi ini bukan hanya mendapat akses membaca tetapi juga dapat merubah angka
    global name
    angka = nilai_baru
    name = nama_baru

print(f"Sebelum {angka,name}")
ubah(10,"Otong")
print(f"Sesudah {angka,name}")

## contoh 3:
# berbeda dengan fungsi jika ingin dapat akses untuk merubah variabel
#global harus pake global. tetapi jika di loop dan percabangan
#tanpa ketik global ia tetap bisa dapat akses untuk merubah variabel global
# begitu juga di variabel local yang ada di perbangan dan loop
#variabel local didalamnya bisa diakses diluar
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 5
    angka_dummy = 10

print(angka)
print(angka_dummy)