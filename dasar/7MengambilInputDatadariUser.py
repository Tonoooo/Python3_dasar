# data yang dimasukkan pasti string
data = input("Masukkan data =")
print("data = ",data,",type =", type(data))

# jika kita ingin mengambil int/float, maka
angka = int(input("masukkan angka = "))
angkaa = float(input("masukkan angka = "))
print("angka = ",angka,", type =", type(angka))

# boolean
biner = bool(int(input("masukkan boolean ="))) # dari input(String) > int > jadilah boolean
print("biner = ",biner,", type =", type(biner))
