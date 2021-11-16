# Stacks(tumpukkan) and Queues(antrian)

# stacks adalah stacks itu dia menumpuk, seperti menumpuk buku yang kita ambil itu pasti yang atas terlebih dahulu
# Queues adalah seperti diantrian restoran orang yang datang pertama terus ada antrian baru, yang akan mendapatkan makanan terlebih dahulu adalah orang yang datang pertama
# jadi perbedan Stacks and Queues adalah keluarnya. Kalo stacks itu yang diakhir. jika Queues yang keluat itu yang depan

## Queues(antrian)

from collections import deque
from typing import Annotated

antrian = deque([1,2,3,4,5])  # jadi ini tipe data deque, fungsi nya nanti bisa menambah dan mengurangi didepan
print('data sekarang: ',antrian)

# menambahkan data
antrian.append(6)
print('data masuk: ',6)
print('data sekarang: ',antrian)

antrian.append(7)
print('data masuk: ',7)
print('data sekarang: ',antrian)

# mengurangi antrian 
out = antrian.popleft() # menghilangkan yang didepan
print('data keluar: ',out)
print('data sekarang: ',antrian)

out = antrian.popleft() # menghilangkan yang didepan
print('data keluar: ',out)
print('data sekarang: ',antrian)

out = antrian.popleft() # menghilangkan yang didepan
print('data keluar: ',out)
print('data sekarang: ',antrian)




antrian.append(8)
print('data masuk: ',8)
print('data sekarang: ',antrian)

