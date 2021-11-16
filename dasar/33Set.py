# tipe data Set (himpunan)

# karakteristik set(himpunan): tidak punya urutan, misalkan kita punya 1 himpunan  ada 2 nama yang sama itu dianggapnya satu data
# dan set tidak suport indexing 

## cara membuat set
# 1. pake {}

superhero = {"wiro sableng",
             "si buta dari goa hantu",
             "saras 008",
             "gundala",
             "gatot kaca"}

# 2. 
superr = set()
superr.add("wiro sableng") # ditambah 
superr.add("si buta dari goa hantu") # ditambah 
superr.add("saras 008") # ditambah 



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


## cara menambah
superhero.add("mak lampir") # ini urutannya akan ngacak, karna emang himpunan/set urutan tidak penting
superhero.add("gundala")  # kenapa gundalanya gak jadi 2 ? karna gundala sudah ada,dan si set memperhatikan jumlah dari data nya ada berapa,dia cuma tau siapa aja yang ada
# set juga bisa ditambahkan string, integer,....
superhero.add(212)


print(superhero)

## jika mau mengurutkan
print(sorted(superr)) # ini diurutkan sesuai abjad



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}

print(ganjil.union(genap)) # union itu digabung
print(ganjil.intersection(prima))  # irisan