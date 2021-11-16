# Function

# Function adalah kumpulan perintah atau baris kode yang dikelompokkan menjadi satu kesatuan untuk kemudian bisa dipanggil atau 
# digunakan berkali-kali. Sebuah fungsi bisa menerima parameter, bisa mengembalikan suatu nilai, dan bisa dipanggil 
# berkali-kali secara independen

# mendefisinikan fungsi
def namafungsinya():
    print("ini adalah fungsi")

# memanggil fungsi
namafungsinya()

# membuat funsi sederhana
def suaraayam():
    print("kukuruyuk!!!")

def hargaayam():
    suaraayam()
    print("harga ayam per 1 kg adalah Rp. 20.000")

hargaayam()

# membuat fungsi dengan input argumen
def hargatotalayam(kg): # (kg) itu disebut input argumen, dan kg itu hanya namanya ini bebas mau apa aja
    suaraayam()
    harga = 20000
    hargatotal = kg*harga
    print('harga',kg,' kg ayam adalah ',hargatotal)

hargatotalayam(5)
hargatotalayam(0.5)
hargatotalayam(9)
hargatotalayam(1)
