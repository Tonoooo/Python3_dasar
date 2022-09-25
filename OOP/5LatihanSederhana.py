# sumber : https://youtu.be/6F0T4IEzke4
# Latihan OOP sederhana

class Hero():
    def __init__(self,nama,health,atekPower,armorNumber):
        self.nama = nama
        self.health = health
        self.attackPower = atekPower
        self.armorNumber = armorNumber
    ## memiliki 2 method : serang dan diserang
    #di setiap method terdapat argumen self, self adalah objek, berarti kita bisa memasukkan objek selain self juga ke argumen. 
    def serang(self,lawan): # (self=objek yang manggil method ini, lawan=objek yang akan diserangnya)
        print(self.nama + ' menyerang ' + lawan.nama)
        lawan.diserang(self, self.attackPower) # objek lawan memanggil method diserang(objek dirisendiri bukan objek lawan ini, attackPower objek dirisendiri)
    
    def diserang(self,lawan, atekPower_lawan):# (objek yang manggil method ini, objek lawan, attackpower lawan)
        print(self.nama + ' diserang  ' + lawan.nama)
        atek_diterima = atekPower_lawan/self.armorNumber
        print('serangan terasa : ' + str(atek_diterima))
        self.health -= atek_diterima
        print('darah '+ self.nama + ' terasa '+str(self.health))
    

tono = Hero('Tono',100,20,10)
suep = Hero('Suep',100,10,5)

tono.serang(suep)
print('\n')
suep.serang(tono)
print('\n')
tono.serang(suep)
print('\n')
tono.serang(suep)
print('\n')
suep.serang(tono)