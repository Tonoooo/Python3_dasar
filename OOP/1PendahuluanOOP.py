# Pendahuluan Object Oriented Programming
# lebih baik tonton video penjelasannya
# videonya link: https://youtu.be/1PjHsUnOkes
# atau di komputer : E:\belajar\Programming\python\VideoTutorialPytho

# dipython kita harus medeklarasikan class itu diatas, sebelum program kita

## membuat class
class Hero:  # ini tamplate
    pass

## membuat objek
hero1 = Hero() # variabel ini adalah sebagai objek/instace (atau prosesnya kita sebut sebagai instansiate)
hero2 = Hero()
hero3 = Hero()
## kita kasih para objek nya nama dan darah (menambahkan atribut untuk objeknya)
hero1.nama = "Adom"
hero1.sehat = 100

hero2.nama = "Tono"
hero2.sehat = 1000

hero3.nama = "Taat"
hero3.sehat = 500

print(hero1)
print(hero1.__dict__) # ngecek si hero1 ini punya apa aja /atribut nya
# mengakses nama objek/menampilkan nama objek hero1
print(hero1.nama)