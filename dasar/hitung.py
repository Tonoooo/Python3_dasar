# ini pasangannya     Menggunakan '__main__'.py


def tambah(a,b):
    print(a,'+',b,'=',a+b)

def kurang(a,b):
    print(a,'-',b,'=',a-b)


# penjelsan __main__

"""
print(__name__)  # jika dirun hasilnya __main__,dan jika dirun difile Menggunakan '__main__'.py maka hasilnya nama file ini(hitung)
"""

# penggunaan __main__
def main():
    print('ini adalah fungsi utama dari hitung')

if __name__ == '__main__':  # jika si__name__ ini  __main__ maka dia akan menjalankan main()
    main()

# jadi fungsi __main__ adalah
# jika kita bikin modul terus kita ingin ngetes/pengen membuat siprogram itu 
# mulai dari satu buah fungsi utama, maka kita bisa gunakan __main__
# tapi kita gamau kalau si__main__ dijalankan kalua dia diimport
# jika dirun hasilnya __main__ maka ini modul utama