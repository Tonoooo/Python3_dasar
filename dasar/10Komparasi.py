# Operasi Komparasi untuk membandingkan nilai
# setiap hasil dari Operasi Komparasi adalah bolean
# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >  (ingat harus lebih besar baru true jika sama akan false)
print("===== LEBIH BESAR DARI (>) ")
hasil = a > 3
print(a,">",3,"=",hasil)
hasil = b > 3
print(b,">",3,"=",hasil)
hasil = b > 2
print(b,">",2,"=",hasil)

# KURANG DARI <  (ingat harus kurang dari baru true jika sama akan false)
print("===== KURANG DARI DARI (<) ")
hasil = a < 3
print(a,"<",3,"=",hasil)
hasil = b < 3
print(b,"<",3,"=",hasil)
hasil = b < 2
print(b,"<",2,"=",hasil)

# lebih besar sama dengan dari >=
print("===== LEBIH BESAR DARI SAMA DENGAN (>=) ")
hasil = a >= 3
print(a,">=",3,"=",hasil)
hasil = b >= 3
print(b,">=",3,"=",hasil)
hasil = b >= 2
print(b,">=",2,"=",hasil)

# kurang dari sama dengan dari <=
print("===== LEBIH BESAR DARI SAMA DENGAN (<=) ")
hasil = a <= 3
print(a,"<=",3,"=",hasil)
hasil = b <= 3
print(b,"<=",3,"=",hasil)
hasil = b <= 2
print(b,"<=",2,"=",hasil)

# sama dengan (==)
print("===== SAMA DENGAN (==) ")
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,"==",4,"=",hasil)

# tidak sama dengan (!=)
print("===== TIDAK SAMA DENGAN (!=) ")
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,"!=",4,"=",hasil)

# 'is' sebagai komparasi object indentity
print("===== object indentity (is)")
# ingat!!! jika ingin menggunakannya harus:
# -jangan literal
# -harus seperti ini x is y 
# -jangan seperti ini a is 4
x = 5 # ini adalah assigment object
y = 5
print('nilai x =',x,',id =',hex(id(x))) # baik x atau y samasama memiliki identitas sama karna- 
print('nilai x =',y,',id =',hex(id(y))) # keduanya memiliki nilai yang sama yaitu 5
hasil = x is y 
print('x is y =',hasil)
a = 2
b = 2
hasil = a is b
print('a is b =',hasil)
c = 5
d = 4
print('nilai c =',c,',id =',hex(id(c)))
print('nilai d =',d,',id =',hex(id(d)))
hasil = c is d
print('c is d =',hasil)

print("===== object indentity (is not)")
x = 5 # ini adalah assigment object
y = 5
print('nilai x =',x,',id =',hex(id(x))) # baik x atau y samasama memiliki identitas sama karna- 
print('nilai x =',y,',id =',hex(id(y))) # keduanya memiliki nilai yang sama yaitu 5
hasil = x is not y 
print('x is not y =',hasil)
a = 2
b = 2
hasil = a is not b
print('a is not b =',hasil)
c = 5
d = 4
print('nilai c =',c,',id =',hex(id(c)))
print('nilai d =',d,',id =',hex(id(d)))
hasil = c is not d
print('c is not d =',hasil)
