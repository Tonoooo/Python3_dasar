# casting adalah merubah tipe data dari satu tipe ke tipe yang lain


## INTEGER
print("=====INTEGER=====")
data_int = 9
print("data = ", data_int," bertype = ", type(data_int))

# cara casting
data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int)  # akan false jika nilai int = 0, float=0
print("data = ", data_float," bertype = ", type(data_float))
print("data = ", data_str," bertype = ", type(data_str))
print("data = ", data_bool," bertype = ", type(data_bool))


## FLOAT
print("=====FLOAT=====")
data_float = 9.9
print("data = ", data_float," bertype = ", type(data_float))

# cara casting
data_int = int(data_float)  #akan dibulatkan kebawah
data_str   = str(data_float)
data_bool  = bool(data_float)  # akan false jika nilai int = 0, float=0
print("data = ", data_int," bertype = ", type(data_int))
print("data = ", data_str," bertype = ", type(data_str))
print("data = ", data_bool," bertype = ", type(data_bool))


## STRING
print("=====STRING=====")
data_str = "10"
print("data = ", data_str," bertype = ", type(data_str))

# cara casting
data_int = int(data_str)  #syaratnya string harus angka
data_float   = float(data_str) #syaratnya string harus angka
data_bool  = bool(data_str)  # akan false jika jika string kosong
print("data = ", data_int," bertype = ", type(data_int))
print("data = ", data_float," bertype = ", type(data_float))
print("data = ", data_str," bertype = ", type(data_str))