#5. Class Variable = variabel yang dimiliki oleh class

# penjelasan Class Variable
# ada di video :
# link https://youtu.be/dBfAm6dQCcY

class mahasiswa():

    jumlah_mahasiswa = 0   # ini variabel class dan juga ini public 
    
    def __init__(self,input_nama,input_nim):
        self.nama = input_nama  # ini public 
        self.nim = input_nim  # ini public
        mahasiswa.jumlah_mahasiswa += 1 #kita mau simahasiswa nambah 1


# main programnya
tono = mahasiswa('tono taat',101)
adom = mahasiswa('adom tono',102)
taat = mahasiswa('taat patuh',103)

print(mahasiswa.jumlah_mahasiswa)

"""
adom.jurusan = 'ekonomi mikro' # jadi ini menimpah di dalam si objek nya si adom
adom.kegemaran = 'membantu'  # jadi ini menimpah di dalam si objek nya si adom

print(adom.jurusan)
print(adom.kegemaran)

print(mahasiswa.__dict__)  # __dict__ adalah dia mengambil semua komponen yang ada di suatu data
print(adom.__dict__)
"""
