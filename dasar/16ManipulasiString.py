# Operasi dan manipulasi string 

# 1. menyambung string (concatenate)
nama_pertama = "tono"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah +"'"+ nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))  # mau pakai koma ataupun tambah akan sama saja

# 3. operator untuk string
# mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap  # jadii mengecek apakah d ada di nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status)) 

D = "D"
status = D in nama_lengkap  
print(D + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap  # jadii mengecek apakah d tidak ada di nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(10*"ha")

# indexing
# index dimulai dari nol
# tapi kalo hitung panjang/jumlah hitungny biasa (dari satu)
print("index ke-0: "+ nama_lengkap[0]) # index dimulai dari nol
print("index ke-6: "+ nama_lengkap[6]) # index dimulai dari nol
print("index ke-(-1): "+ nama_lengkap[-1]) # -1 dimulai dari akhir/ujung
print("index ke-(-2): "+ nama_lengkap[-2])
# mengambil range
print("index ke-(0:3): "+ nama_lengkap[0:4]) # artinya 0 sampai sebelum 4, jadi yang terakhir gak di ambil
print("index ke-(3:7): "+ nama_lengkap[3:8])
print("index ke-(0,2,4,6,8,10): "+ nama_lengkap[0:10:2])  # artinya 0 sampai 10 tapi diloncatin 2

# item paling kecil
print("paling kecil : "+ min(nama_lengkap)) # jadi dia akan ngeluarin teks/huruf paling kecil nilainya
# item paling besar
print("paling besar : "+ max(nama_lengkap)) # jadi dia akan ngeluarin teks/huruf paling besar nilainya
# maksud dari paling besar atau paling kecil itu nilainya
# ascii code ASCII sendiri adalah suatu standar internasional dalam kode huruf-
#  dan simbol seperti Hex dan Unicode tetapi ASCII lebih bersifat universal, contohnya 124 adalah untuk karakter "|".
ascii_code = ord(" ") # ord itu untuk mengambil unicodenya dari onestring karakter
print("Ascii code untuk spasi adalah " + str(ascii_code))
ascii_codee = ord("k")
print("Ascii code untuk k adalah " + str(ascii_codee))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk methods
data = "tono toon noo"
jumlah = data.count("o")
print("jumlah o pada "+ data + " = " + str(jumlah))



##  operator dalam bentuk methods
# merubah case dari string
print("~~~~~~~~~~~~~")

# merubah semua ke upper case
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKu KeCe AbiezZzZ"
print("normal = "+ alay)
alay = alay.lower()
print("lower = "+ alay)

## pengecekan dengan isX method
# contoh pengecekan lower dan upper case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = "+ str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = "+ str(apakah_upper))
# dan ini is yang bisa digunakan selain isupper dan islower adalah
# isalpha() <-- untuk mengecek semuanya huruf 
# isalnum() <-- untuk mengecek huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar
# dan masih banyak lagi

# contoh istitle
judul = "It Is Okay Not To Be Orkey"
cekjudul = judul.istitle() # hasilnya bool
print(judul + " is title = "+ str(cekjudul))

## mengecek kompenen startswith() endswith()
cek_start = "Fokus Belajar".startswith("Fokus") # mengecek kata Fokus apakah ada diawal cek_start
print("start = "+ str(cek_start))
cek_end = "Belajar Terus".endswith("Terus") # mengecek kata Terus ada diakhir cek_end
print("end = "+ str(cek_end))

## penggabungan komponen join() split()

pisah = ['aku','sedang','belajar']
gabungan = ",".join(pisah)
print(pisah)
print(gabungan)
gabungan = " ".join(pisah)
print(gabungan)
gabungan = " ehm ".join(pisah)
print(gabungan)

gabungan = "akuehmsedangehmbelajar"
print(gabungan.split('ehm'))

## alokasi karakter rjust(), ljust(), center()
# rjust() = rata kanan
# ljust() = rata kiri
# center() = tengah

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10)
print("'"+tengah+"'")

tengah = "tengah".center(20,"~") # bisa diganti bukan hanya spasi, tinggal tambahkan saja 
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = tengah.strip("~") # menghilangkan tanda ~
print("'"+tengah+"'")
