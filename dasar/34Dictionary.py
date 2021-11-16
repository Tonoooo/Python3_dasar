#  tipe data Dictionary

# Dictionary adalah sbuah struktur data asosiatif atau menggunakan maping
# cara membuat Dictionary:     nama = {key:value}


member1 = {"ID":101,
           "Nama":"Tono",
           "pekerjaan":"tangan kanan",
           "status member":"kepercayaan setia"
           }


member2 = {"ID":102,
           "Nama":"Adom",
           "pekerjaan":"babu",
           "status member":"patuh"}


memberlist = {101:member1,102:member2}


# cara mengakses data
print(member1)
print(member1["ID"]) # [key] jadi di dictionary itu bisa pake key
print(member1["Nama"]) # [key] jadi di dictionary itu bisa pake key
print(memberlist[101])

# jika kita ingin mengetahui key nya saja
print(member1.keys())
# jika kita ingin mengetahui value nya saja
print(member1.values())

# mau ngambil semuanya
print(member1)
# atau
print(member1.items())