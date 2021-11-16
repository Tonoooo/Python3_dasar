import sys

data_list = [1,2,3,4,5,'pisang goreng','adom','tono', False, 3.14]
data_tuple = (1,2,3,4,5,'pisang goreng','adom','tono', False, 3.14)

besar_datalist = sys.getsizeof(data_list)   # ngecek besarnya data
besat_datatuple = sys.getsizeof(data_tuple)   # ngecek besarnya data

print("besar data list: ", besar_datalist)
print("besar data list: ", besat_datatuple) # ukuran data tuple lebih kecil dari pada list

# lanjut ke testTuple2.py