# Class Inheritance = warisan / turunan
# Inheritance biasa disebut dengan pewarisan
# Inheritance adalah konsep bahsa pemrograman di mana sebuah class dapat mewariskan’ property/atribut dan method yang dimilikinya kepada class lain

class Ojek():

    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id_abang(self):
        print('nama:',self.nama,'\ntransmisi:',self.transmisi,'\ndaerah:',self.daerah)


class Gojek(Ojek): # jadi si Gojek ini warisan/turunan dari si Ojek. jadi semua yang ojek punya itu akan diambil oleh gojek
    
    def cek_id_abang(self):  # ini di overide, jadi menimpah
        print('cek aplikasi gojek')


ojek1 = Ojek('tono','manual','semesta')
ojek2 = Gojek('adom','matic','bumi') 

ojek1.cek_id_abang()
ojek2.cek_id_abang()