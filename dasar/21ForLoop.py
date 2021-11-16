# For Loop


# list sebagai iterable
gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']
for g in gorengan:  # artinya untuk setiap g di gorengan. Jadi si g ini akan mengakses setiap isi dari listnya. dan g ini merupakan variabel baru
    print(g)  # jadi dia akan mengambil komponen g didalam gorengan
    print(len(g))  # len() adalah jumlah item atau anggota

# string sebagai iterable
bakwan = 'bakwan'
for i in bakwan:
    print(i)

# for didalam for
gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']
buah = ['semangka','jeruk','anggur','apel']
sayur = ['kangkung','wortel','tomat','kentang']
Daftar_belanja = [gorengan,buah,sayur]

for subDaftarBelanja in Daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)
        # jadi for yang pertama akan mengambil list layer pertama dulu nah lalu dia akan ngeprint subdaftarbelanjanya
        # selanjutnya kita akan mengambil setiap komponen di subDaftarBelanja, nah yang pertam itu gorengan lalu....
