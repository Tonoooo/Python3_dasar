# sumber : https://youtu.be/k9ANKapvMKo
# Latihan OOP tkinter
# tkinter menggunakan konsep OOP untuk membuat library nya
# di python setiak class diawali hurup besar, kalo yang awal kecil(seperti pack() ) itu method/fungsi


import tkinter

# membuat objek main window (objek yang menjadi layarnya)
main_window = tkinter.Tk()

# membuat objek label
label1 = tkinter.Label(main_window, text= "label1")
label2 = tkinter.Label(main_window, text= "label2")

# membuat objek button
tombol1 = tkinter.Button(main_window, text= "tombol1")
tombol2 = tkinter.Button(main_window, text= "tombol2")

# method positioning. mathod pack tidak memiliki argumen dan tidak punya return
label1.pack() # dia akan menaro / menampilkan labelnya dilayar
label2.pack()
tombol1.pack() # dia akan menaro / menampilkan tombolnya dilayar
tombol2.pack()

# method menampilkan GUi(layarnya)
main_window.mainloop()
