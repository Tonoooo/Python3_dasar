# Constructor __init__()
# sumber : https://youtu.be/w9emRmkbeps
# init akan berjalan saat class dipanggil dia akan langsung menjalankan init 
# self adalah untuk mengidentifikasi si Hero ini dipakai/milik oleh siapa, dan  segala sesuatu yang ada selfnya itu milik si instace 
# init adalah Inisialisasi (Initialization)

class Hero:  # ini tamplate
    # init / initialization untuk atribut objek
    def __init__(self, inputNama,inputHealth, inputPower, inputArmor): # init akan berjalan saat class/Hero dipanggil dia akan langsung menjalankan init,dan self ini adalah si objeknya (seperti hero1)
        # ini yang disebut atribut
        self.nama = inputNama
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


# ini pembuatan objek serta memasukkan argumen nya seperti (inputNama,inputHealth, inputPower, inputArmor)
hero1 = Hero("Tono",1000,1000,1000) # saat kita meninstansiet baru dari si class(Hero),saat kita pertama kali manggil clas(Hero) dia akan menjalankan init
hero2 = Hero("Taat",100,500,200)
hero3 = Hero("Adom",100,200,150)


# pemanggilan atau apapun itu 
print(hero1.nama)
print(hero2.health)
print(hero3.__dict__)  # __dict__ fungsinya agar kita tau si objek ini punya atribut apa aja


# jadi init akan dieksekusi saat objek dibuat 