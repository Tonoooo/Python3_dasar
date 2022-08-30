# sumber : https://youtu.be/2BSf8Kr-0cw
'''**kwargs'''

# fungsi biasa tanpa kwargs
def fungsi(nama,tinggi,berat):
    '''fungsi biasa'''
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
fungsi("ucup",183,79)


## ~~~~~~ fungsi dengan **kwargs (Keyword arguments)
print(10*"=","**kwargs")
def fungsi_kwargs(**kwargs):
    print(kwargs)
fungsi_kwargs(nama="tono",tinggi=200,berat=95)
# >>> **kwargs menghasilkan dictionary

def fungsi(**kwargs):
    '''karna kwargs hasilnya dictionary, kita jadi bisa menggunakannya
    dengan memanggil menggunakan key/kunci'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="ucup",tinggi=183,berat=79)


# studi kasus args dan kwargs

def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output +=angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("tidak ada operasi")

    return output

hasil = math(1,2,3,4,option="tambah")

print(f"hasil jumlah {hasil}")

hasil = math(1,2,3,4,option="kali")
print(f"hasil kali {hasil}")