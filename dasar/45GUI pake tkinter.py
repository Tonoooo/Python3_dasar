# Membuat GUI dengan Built-in Package tkinter
# tkinter adalah GUI yang Built-in yang ada di python,
# graphical user interface atau GUI adalah jenis antarmuka pengguna yang menggunakan metode interaksi pada peranti elektronik 
#   secara grafis (bukan perintah teks) antara pengguna dan komputer.

#  penjelasan Membuat GUI dengan Built-in Package tkinter
# ada di video :
# link   https://youtu.be/RWCeiOCfIuY

import tkinter

main_window = tkinter.Tk()

def even_tekan():
    label2 = tkinter.Label(main_window, text="sudah ditekan ^_^")
    label2.pack()

label = tkinter.Label(main_window, text="halo, saya adalah \n GUI sederhana dengan \n menggunakan python")
tombol = tkinter.Button(main_window, text="tekan", command= even_tekan)

label.pack() # ini artinya ditaro
tombol.pack() # ini artinya ditaro dan ini ada dibawah si label

main_window.mainloop() # mainloop() adalah dia akan muter terus programnya sampai kita close baru berhenti
