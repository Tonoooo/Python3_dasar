# Latihan Inheritance

# Pejelasan Latihan Inheritance
# lebih baik tonton video penjelasannya
# videonya link: https://youtu.be/sSgKKLzxqS0


# ini berhubungan dengan modul Hero.py

from Hero import HeroIntelejen, HeroSreng 


tono = HeroIntelejen('Tono')
suep = HeroSreng('Suep')

tono.show_info()
suep.show_info()

tono.gainexp = 200
suep.gainexp = 250

tono.show_info()
suep.show_info()
