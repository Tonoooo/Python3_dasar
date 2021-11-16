# Function & Arguments

# fungsi dengan menggunakan argumen sederhana
def siswa(nama): # (nama) ini disebut argumen
    print('siswa ini bernama:',nama)

siswa('tono')  # harus memasukkan argumen jika tidak nanti error

# fungsi dengan menggunakan keywords arguments
print("~~~~~~~~~~~")
def guru(nama,pelajaran):
    print("guru ini bernama:",nama)
    print("mengajari:",pelajaran)

guru(nama='adom',pelajaran='bisnis') # ini disebut keywords arguments
guru(pelajaran='bisnis',nama='adom') # fungsinya keywords arguments adalh bisa tidak sesuai urutan,
#                                      dengan syarat harus menggunakan keywords (nama=  )
guru('bisnis','adom')   # ini contoh yang salah karna tidak berurutan,jika ingin tidak berurutan pakailah keywords


# fungsi dengan mwnggunakan default arguments
print("~~~~~~~~~~~")
def penjagasekolah(nama,sif='pagi',galak='tidak'):
    print("penjaga sekolah ini bernama:",nama)
    print("sifnya:",sif)
    print("galak?:",galak)

penjagasekolah('taat')  # arguments yang lain boleh diisi atau tidak,karna arguments yang lain telah diisi sebelumnya
penjagasekolah('taat',sif='malam')
penjagasekolah('taat',sif='sore',galak='sangat lembut')
#penjagasekolah(sif='siang',galak='sopan') # ini menghasilkan error karna nama nya tidak diisi
