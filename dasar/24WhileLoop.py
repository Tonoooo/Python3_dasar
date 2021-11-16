# While Loop
# Pengulangan While Loop di dalam bahasa pemrograman Python dieksesusi statement berkali-kali selama
#  kondisi bernilai benar atau True. 

## JIKA INGIN MENJALANKAN salah satu PROGRAM SILANGKAH HAPUS """"""


# while sederhan
"""
angka = 0
while angka < 5:
    print('nilai angka adalah', angka)
    angka = angka + 1

print("diluar while")
"""

# while dengan boolean
"""
mulai = True  # variabel boolean
angka = 0
while mulai:
    print("didalam while")
    if angka is 100:
        mulai = False
        print('oke angka 100 ditemukan')
    angka += 1
"""



## else, continue, break, pass

# else
"""
# else ini fungsinya dia akan menunjukan akhir yang menunjukan bahwa while ini sudah beres
angka = 0
while angka < 10:
    print('nilai angka adalah', angka)
    angka += 1
else:  # else ini fungsinya dia akan menunjukan akhir yang menunjukan bahwa while ini sudah beres
    print('nilai angka diakhir while adalah',angka)
"""

# break
"""
angka = 0
while angka < 10:

    if angka is 5:
        print("chekpoint)
        break  # jadi break ini dia akan keluar langsung dari semua komponen loopingnya

    print('nilai angka adalah', angka)
    angka += 1
else: 
    print('nilai angka diakhir while adalah',angka)
print("diluar while")
"""

# pass
"""
angka = 0
while angka < 10:

    if angka is 5:
        pass  # pass tidak ngaruh apa apa

    print('nilai angka adalah', angka)
    angka += 1
else: 
    print('nilai angka diakhir while adalah',angka)
print("diluar while")
"""

# continue
# continue di while loop harus hati hati
# ingat continue dilooping dia akan berpotensi untuk membuat
#  si looping ini stak jadi infinity loop
"""
angka = 0
while angka < 10:

    if angka is 5:
        angka += 1 # kenapa ada ini?, karna jika tidak nanti akan infinity loop
        continue 

    print('nilai angka adalah', angka)
    angka += 1
else: 
    print('nilai angka diakhir while adalah',angka)
print("diluar while")
"""
