# Stacks(tumpukkan) and Queues(antrian)

# stacks adalah stacks itu dia menumpuk, seperti menumpuk buku yang kita ambil itu pasti yang atas terlebih dahulu
# Queues adalah seperti diantrian restoran orang yang datang pertama terus ada antrian baru, yang akan mendapatkan makanan terlebih dahulu adalah orang yang datang pertama
# jadi perbedan Stacks and Queues adalah keluarnya. Kalo stacks itu yang diakhir. jika Queues yang keluat itu yang depan


## Stacks (tumpukkan)

tumpukan = [1,2,3,4,5,6]
print('data sekarang: ',tumpukan)

# memasukkan data baru
tumpukan.append(7)
print('data masuk: ',7)
print('data sekarang: ',tumpukan)
tumpukan.append(8)
print('data masuk: ',8)
print('data sekarang: ',tumpukan)

# menghilangkan data yang terakhir
tumpukan.pop()
print('data sekarang: ',tumpukan)
# contoh lain
out = tumpukan.pop() # hati hati jika seperti ini bisa merubah data asli(tumpuka)
print('data keluar: ',out)
print('data sekarang: ',tumpukan)
