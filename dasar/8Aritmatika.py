# Operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,"+",b,"=",hasil)

# operasi perngurangan -
hasil = a - b
print(a,"-",b,"=",hasil)

# operasi perkalian *
hasil = a * b
print(a,"*",b,"=",hasil)

# operasi pembagian /
hasil = a / b
print(a,"/",b,"=",hasil)

# operasi eksponen (pangkat) **
hasil = a ** b   # artinya a pangkat b
print(a,"**",b,"=",hasil)

# operasi modulus (sisa bagi) %
hasil = a % b
print(a,"%",b,"=",hasil)

# operasi floor division(seperti pembagian tapi dibulatkan kebawah) //
hasil = a // b
print(a,"//",b,"=",hasil)

## prioritas operasi, operational precedence

"""
   prioritas operasi (urutan pengerjaan)
1. kurung ()
2. exponen **
3. perkalian dan termasuk pembagian ,modulus ,floor division * / % //
4. TAMBAH dan lalu KURANG  + -
"""

x = 3
y = 2
z = 4

hasill = x ** y * z + x / y - y % z // x
print(x ,"**", y ,"*" ,z ,"+" ,x ,"/" ,y ,"-" ,y ,"%" ,z ,"//", x,"=", hasill)

hasil = x + y * z
print(x,"+",y,"*",z,"=",hasil)

hasil =  (x + y) * z
print("(",x,"+",y,")","*",z,"=",hasil)