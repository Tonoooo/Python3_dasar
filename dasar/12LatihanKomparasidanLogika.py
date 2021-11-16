# Latihan Komparasi dan Logika

# membuat gabungan area rentang dari angka
# ++++++3--------10+++++++
inputUser = float(input('masukkan angka yang bernilai kurang dari 3 \natau \nlebih besar dari sepuluh ='))

# ++++++3--------
# memeriksa angka kurang dari 3
isKurangdari = (inputUser < 3)
print('kurang dari 3 =',isKurangdari)

# -----10+++++
# memeriksa angka lebih dari 10
isLebihbesar = (inputUser > 10)
print('lebih dari 10 =',isLebihbesar)

# ++++++3--------10+++++++
isBenar = isKurangdari or isLebihbesar
print('angka yang anda masukkan =', isBenar)


#------3++++++10-------
# kasus irisan
print('\n',10*"=",'\n')
inputUser = float(input('masukkan angka yang bernilai lebih dari 3 \ndan \nkurang dari sepuluh ='))
#----3++++
# lebih dari tiga
isLebihbesar = inputUser > 3
print("lebih dari 3 =",isLebihbesar)

#kurang dari 10
iskurangdari = inputUser < 10
print("kurang dari 10 =",iskurangdari)

# ++++++3--------10+++++++
isBenar = iskurangdari and isLebihbesar
print('angka yang anda masukkan =', isBenar)