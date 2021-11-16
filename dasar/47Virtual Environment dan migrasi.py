# Virtual Environment dan migrasi
# Virtual Environment adalah kunci sebelum membuat projek

# penjelasan dan cara Virtual Environment dan migrasi
# ada di video :
# link https://youtu.be/twu1t_yo0PM
# atau dikomputer E:\belajar\code\python\VideoTutorialPython


### membuat Virtual Environment
## 1. (ini cara ribet ) membuat Virtual Environment dengan menggunakan command prompt

# cara ngecek package yang ada dipython kita 
"""
ketik :
pip list --format=columns
   lalu run/enter
"""
# cara membuat projek/Virtual Environment dicommand prompt
"""
ketik :
python -m venv (nama projek)      ,contoh:
python -m venv projeck1
   lalu run/enter
"""
# cara ngecek dimana projeknya/Virtual Environment dicommand prompt
"""
ketik :
dir
   lalu run/enter
"""
# cara masuk projek/Virtual Environment kita dicommand prompt
"""
ketik :
(nama projek)\Scripts\activate.bat        ,contoh:
projeck1\Scripts\activate.bat
   lalu run/enter
"""
# cara ngecek package yang ada dipython kita dengan menggunakan command prompt
"""
ketik :
pip list --format=columns
   lalu run/enter
"""
# cara keluar dari projek kita yang ada dicommand prompt
"""
ketik :
deactivate
   lalu run/enter
"""


## 2. cara ini menggunakan pycharm dan command prompt ( ini adalah cara paling mudah )

# (INGAT!! TEMPAT PENYIMPANAN PROJEK-PROJEK ADA DI C:\Users\JARVIS\Project)
# buat dulu projeknya
"""
new projek > new Environment > namanya
"""
# cara masuk projek kita dicommand prompt
"""
ketik :
cd Project
    lalu ketik:
cd (nama projek)      ,contoh:        cd projek11
    lalu ketik:
venv\Scripts\activate.bat
   lalu run/enter
"""
# cara keluar dari projek kita yang ada dicommand prompt
"""
ketik :
deactivate
   lalu run/enter, lalu ketik:
cd ..\        
   lalu run/enter, lalu ketik:
cd ..\ 
"""



# BENAR BENAR PENTING !!!!

### 
# jangan lupa python intertpreter nya


### 
# misalkan kita dah buat program lalu kita ingin migrasi dari virtual Environment ini ke virtual Environment yang lain / cloud server
# jadi kita mau ngambil semua defedensi(package/eksternal package) yang ada taro disebuah text lalu diinstal ditempat yang lain
# cara nya:
# ini masih diprojek/Environment awal (bukan yang kita ingin pindah)
# ketik di comandprompt nya (comandprompt nya sudah masuk di projek awal (bukan yang kita ingin pindah) )
"""
pip freeze --local > (namanya).txt       ,contoh:
pip freeze --local > requirement.txt                  # artinya taro semua defedensi(package/eksternal package) yang ada kedalam sebuah text
   lalu run/enter
"""
# lalu copy file txt nya, lalu paste di projek/Virtual Environment yang kita akan migrasi(bukan projek yang awal)
# setelah di paste di projek/Virtual Environment yang kita akan migrasi(bukan projek yang awal)
# lalu kita ketik di comandprompt nya (comandprompt nya sudah masuk di projek/Virtual Environment yang kita akan migrasi(bukan projek yang awal))
"""
pip install -r (namanya).txt       ,contoh:
pip install -r requirement.txt              # artinya dia akan menginstal semua package yang ada di file txt nya sesuai dengan serialnya/versinya
"""
