# Return Value

# Fungsi return value di dalam pembuatan sebuah function yaitu ketika kita akan membuat sebuah fungsi dan di dalam
#  fungsi tersebut terdapat sebuah perhitungan seperti perkalian, pembagian, tambah, ataupun pengurangan kemudian
#  hasil dari perhitungan tersebut akan memberikan nilai balik.

# fungsi dengan return value
def kuadrat(argumen):
    total = argumen**2 # pangkat 2
    print('nilai kuadrat dari',argumen,'adalah:',total)
    return total  # jadi totalnya kita return, jadi nanti kalo misalnya kita memiliki syntax seperti a = kuadrat(3) sehinnga-
                  # nanti hasil dari fungsi kuadrat ini yang hasilnya total yang-
a = kuadrat(3)    #  di return nya nanti dia akan masuk ke variabel a
print(a)

print('~'*10)

# fungsi dengan return value dan multiple argumen
def tambah(argumen1,argumen2):
    total = argumen1 + argumen2
    print(argumen1,'+',argumen2,'=',total)
    return total  # return itu bisa list,number,string,atau macem macem

def kali(argumen1,argumen2):
    total = argumen1 * argumen2
    print(argumen1,'x',argumen2,'=',total)
    return total 

a = tambah(3,4)
b = kali(3,4)

# karna sudah return value jadi kita bisa seperti ini:
c = kali(3,a)
d = kali(3,tambah(5,5))
#print(a)
#print(b)
#print(c)
#print(d)
print('~~~~ e ~~~')
e = tambah(kali(2,2),a)  # nanti hitungnya 2 x 2 dulu baru hasil ini ditambah hasil a
print(e)
print('~~~ f ~~~~')
f = tambah(10,kali(2,5)) # nanti hitungnya 2 x 5 dulu baru hasil ini ditambah 10