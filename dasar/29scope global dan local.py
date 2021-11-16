# scope global dan local


### scope variabel : local

namaKucing = 'tono'  # disebut variabel global

def rubahNamaKucing(namaBaru):
    namaKucing = namaBaru  # namakucing ini local,dan ini tidak merubah variabel global. Jadi mau namakucing global dirubah apapun namakucing difungsi ini tidak akan berubah
    print('saya rubah nama kucing jadi',namaKucing)

rubahNamaKucing('adom') # ini tidak akan merubah variabel global
print('nama kucing saya menjadi',namaKucing) 


### scope variabel : global
# scope global selalu dimulai dengan global

print('~~~~~~~~~')
namaKucingg = 'taat'
def rubahNamaKucingg(namaBaru):
    global namaKucingg   # global artinya kita akan mengakses nilai global di fungsi ini
    namaKucingg = namaBaru
    print('saya rubah nama kucing jadi',namaKucingg)

rubahNamaKucingg('TONO')
print('nama kucing saya menjadi',namaKucingg)
# contoh lain
print('~~~~~~~~')
makananKucing = 'sosis'
def kasihMakanKucing(makanan,nama):
    global namaKucingg,makananKucing
    namaKucingg = nama
    makananKucing = makanan

kasihMakanKucing('makanan sisa','jalu')
print('nama kucing saya menjadi',namaKucingg,'dan makan',makananKucing)

# jadi kesimpulannya:
# - Scope lokal digunakan untuk/bertujuan/agar variabel globla(asli) tidak rubah
#   dan jadi jika tidak ingin merubah variabel grobal maka gunakan scope lokal.
# - Tapi jika ingin merubah varibel global gunakan scope lokal
#   dan scope global selalu dimulai dengan global
