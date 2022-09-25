# modul ini milik dan berhubungan dengan 16multipelinheritance




class team():
    def setteam(self,team):
        self.team = team

    def showteam(self):
        print(self.team)


class Tipe_Hero:
    def settipe(self,tipe):
        self.tipe = tipe

    def showtipe(self):
        print(self.tipe)


class Hero(team,Tipe_Hero):

    def __init__(self,nama,health):
        self.nama = nama
        self.health = health


tono = Hero("Tono",100)
tono.setteam("induk")
tono.settipe("AI")

tono.showteam()
tono.showtipe()