# More on List


Barang = ['kunci','ember','jaket','ban','mobil']
print(Barang)

## bebarapa method yang bisa digunakan untuk memanipulasi list

# method untuk menambah data kedalah list
Barang.append('sepeda')  # menambah data ke list tapi dibelakannya
print(Barang)

Barang.extend('dompet')  # menambahkan kelist dibelakangnya tapi ngambil iterable 
print(Barang)

Barang.insert(3,'sepeda') # menambah data ke list dan 3 itu posisi/index nya
print(Barang)

# method untuk menghitung anggota
jumlahSepeda = Barang.count('sepeda') # ini menghitung ada berapa sepeda. count artinya menghitung. 
print('jumlah sepeda adalah',jumlahSepeda)

# meremove data
Barang.remove('sepeda')
print(Barang) # kenapa cuma sepeda pertama saja yang diremove? karna si remove ini dia akan remove yang ketemu pertama kali

# kebalik datanya
Barang.reverse()
print(Barang)

# hati hati jika ingin mengambil / mengcopy list JANGAN seperti ini:
stuf = Barang # jika seperti ini, bisa merubah list asli(barang). ini mah bukan mengcopy/mengambil list tapi ini mah mengganti nama list
stuf.append('gelas') # jika seperti ini, bisa merubah list asli(barang) BAHAYA!!!
print(stuf)
print(Barang)
# biar aman jika ingin mengambil / mengcopy list:
stuf = Barang.copy()
stuf.append('piring')
print(stuf)
print(Barang)
