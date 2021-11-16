# If Elif Else

nilai = 50

if nilai == 60:  
    print("nilai anda: ", nilai)

if nilai != 60:   
    print("nilai anda bukan: 60")




print(20*"=")

nilai = 65

if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai <= 80:
    print("nilai anda adalah B")
elif 60 <= nilai <= 70:
    print("nilai anda adalah C")
elif 50 <= nilai <= 60:
    print("nilai anda adalah T, lakukan perbaikan")
else:
    print("maaf anda tidak lulus")

print(20*"+")
# operator logika untuk list dan string

gorengan = ['bakwan','cireng','bala-bala','gehu','combro','pisang goreng','pukis','risoles']
beli = 'basreng'

if beli in gorengan:  # artinya jika beli ada digorengan maka...
    print('penjual berkata "ya saya jual ',beli,'"')

if not beli in gorengan:  # artinya jika beli tidak ada di gorengan maka....
    print('"saya gak jual',beli,'"')

karakter = 'z'
if karakter in beli:
    print("ada",karakter,"di",beli)
else:
    print("tidak ada",karakter,"di",beli)