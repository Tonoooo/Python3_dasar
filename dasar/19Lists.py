# Lists

Data = [1,4,9,16,25,36,49,64] # ciri list pake []

# mengakses list
subdata1 = Data[0]    # list itu dimulai/dihitung dari 0
subdata2 = Data[-1]   # list itu terakhir/ujung itu -1

# memotong list
subdata3 = Data[0:4]  # diambilnya 0 sampai sebulum 4
subdata4 = Data[-2:]  
subdata5 = Data[2:]
subdata6 = Data[:5]
subdata7 = Data[:-5]

Data2 = [100,200,300,400,500,600,700,800]

# menambah list
Data3 = Data + Data2

# merubah konten dari list
Data[4] = 87

# mengcopy list ke variabel baru
a = Data[:]  # [:] artinya a akan mengakses semua komponen dari data ke a. Dan agar tidak mengubah data aslinya 
a[7] = 87

# merubah content list dengan menggunakan metode slicing 
Data[3:5] = [11,12]

# list dalam list
x = [Data,Data2]

# mengakses list dalam multidimensional list
y = x[0][3]  # [0] maksudnya list yang pertama, dan [3] adalah komponen dalam list
yy = x[1][4]
print(x)
print(y)
print(yy)

# methods untuk list
Data.append(30)  # append adalah menambah

# Function yang bisa digunakan kepada list
panjang_list = len(Data) # len() digunakan  untuk mengetahui panjang (jumlah item atau anggota) 
print(Data)
print(panjang_list)