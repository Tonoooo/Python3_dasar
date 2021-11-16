data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

"""
   1. dengan menggunakan single quote  '...'
   2. dengan menggunakan double quote  "..."
"""

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan single quote"
print(data)

print('"Halo, apa kabar?"')  # membuat tanda "" menjadi string
print("'Halo, apa kabar?'")  # membuat tanda ' menjadi string
print("ini adalah hari jum'at") # membuat tanda ' menjadi string

# 2. menggunakan tanda \
# membuat tanda ' menjadi string tanpa menggunakan "..."
print('mari sholat jum\'at') # gunanya \' jadi jum'at
print('g\'day, isn\'t it?')

# backlash (backlash(\) itu merupakan karakter khusus)
print("C\\User\\Tono") # gunanya \\ adalah untuk biar dianggap \ atau biar dianggap string \ 

# tab
print("tono\tsuep, jadi jauhan") # gunanya \t jadi jauhan (spasinya lega)

# backspace
print("tono \bsuep, jadi deketan") # gunanya \b jadi deketan 

# newline (jadi baris baru (seperti enter))
print("-baris pertama.\n-baris kedua") # LF -> Line Feed -> dipakai oleh  unix,linux,macos
print("baris pertama.\rbaris kedua")  # CR -> carriage return -> dipakai oleh  commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua") # CRLF -> Line Feed carriage return -> dipakai oleh  windows
                         # jadi kita bisa pake \n  


# 3. string literal atau raw

# hati hati 
print('c\new folder') # akan salah pathnya

# solusi menggunkana raw string
print(r'c\new folder') # r ini artinya menjadikan semua string

# multiline literal string
print("""
nama : tono
agama : islam
""")

# multiline literal string dan RAW
print(r"""
nama : tono
agama : islam
penyimpanan : c\new\newzaman
""")