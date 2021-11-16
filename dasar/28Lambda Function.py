# Lambda Function


## ini fungsi biasa
def jumlah(a,b):
    c = a+b
    return c
hasil = jumlah(4,5)
print(hasil)



## membuat anonymous function dengan lambda
kali = lambda x,y: x*y

# cara memanggilnya
print(kali(4,5))
# atau 
hasill = kali(5,4)
print(hasill)
