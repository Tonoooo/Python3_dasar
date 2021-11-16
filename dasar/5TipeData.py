# a = 10 ,    a adalah variabel dengan nilia 10

## tipe data:

# integer = angka satuan yang gak ada komanya
data_integer = 1
print("data : ", data_integer)
print(" -bertipe : ", type(data_integer))

# float = angka dengan koma
data_float = 1.5
print("data : ", data_float)
print(" -bertipe : ", type(data_float))

# string = kumpulan karakter
data_string = "Tono"
print("data : ", data_string)
print(" -bertipe : ", type(data_string))

# boolean = biner  True/Flase
data_bool = True
print("data : ", data_bool)
print(" -bertipe : ", type(data_bool))

## tipe data khusus

# bilangan complex
data_complex = complex(5,6)
print("data : ", data_complex)
print(" -bertipe : ", type(data_complex))

# tipe data dari bahasa c

from ctypes import c_double, c_char, c_long

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print(" -bertipe : ", type(data_c_double))