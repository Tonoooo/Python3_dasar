# format string


# contoh generic
# string
nama = "tono"
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean {boolean}"
print(format_str)

# angka 
angka = 2021.7
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat 
angka = 15
format_str = f"bilangan bulat = {angka:d}"  # d bahwa si angka itu bilangan bulat
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2021.7341
format_str = f"desimal = {angka:.2f}"  # artinya mengambil 2 angka setelah titik,dan f artinya float
print(format_str)

# menampilkan leading zero
angka = 2021.7341
format_str = f"desimal = {angka:10.2f}" # 10 itu jumlahnya 
print(format_str)
angka = 2021.7341
format_str = f"desimal = {angka:010.2f}" # mengganti yang tadinya spasi diganti 0
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.357
format_minus = f"minus = {angka_minus:+d}"  # tanda plus untuk menampilkan + atau -
format_plus = f"plus = {angka_plus:+.2f}"   # tanda plus untuk menampilkan + atau -
print(format_minus)
print(format_plus)

# menformat persen 
persentase = 0.045
format_persenn = f"persen = {persentase:%}"  # agar menjadi persen maka gunakan %
format_persen = f"persen = {persentase:.2%}" # .2 artinya mengambil 2 angka setelah titik
print(format_persenn)
print(format_persen)

# melakukan operasi aritmatika didalam placeholder
harga = 10000
jumlah = 5
format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)
