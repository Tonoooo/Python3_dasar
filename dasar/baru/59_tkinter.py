# GUI -> Graphical User Interface
# sumber : https://youtu.be/L4dbeLNDFlc

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo #  untuk window info

# si GUI / app kita mau dikasih variabel apa?. nama variabelnya bebas
window = tk.Tk() # divariabel ini kita bikin jadi objek  

## untuk merubah sesuatu
window.configure(bg="white")# salahsatu contohnya dimethod configure adl untuk warna background
window.geometry("300x200")# mengatur ukuran. (x,y)=(lebar, tinggi)
window.resizable(False,False) # (x,y)agar ukurannya tetap
window.title("Sapa Dia!")

###  widget/frame input
input_frame = ttk.Frame(window) # objek untuk  widget/frame kita.  widget/frame kita taro di dalam window tadi
## Penempatan
#penempatan ada 3 = Grid, Pack, Place. disini kita pake pack, agar ngurut/numpuk kebawah
input_frame.pack(padx=10,pady=10,fill="x",expand=True)
#(padding x, padding y, fill=framenya horizontal sumbu x, expand=digunakan untuk memperluas widget).
## komponen-komponen didalam widget/frame input_frame
# 1. label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan:")# (objek framenya, textnya)
#untuk menampilkan labelnya pake pack seperti tadi. jadi ada pack dilevelnya frame, ada pack didalamnya frame
nama_depan_label.pack(padx=10,fill="x",expand=True)
# 2. input/entry nama depan
NAMA_DEPAN = tk.StringVar() # variabel tempat  menangkap/menmpung inputnya .StringVar() agar mudah mengelolanya
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)# (objek framenya, nama variabel untuk menangkap/menmpung inpunya)
nama_depan_entry.pack(padx=10,fill="x",expand=True)
# 3. label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama belakang:")# (objek framenya, textnya)
#untuk menampilkan labelnya pake pack seperti tadi. jadi ada pack dilevelnya frame, ada pack didalamnya frame
nama_belakang_label.pack(padx=10,fill="x",expand=True)
# 4. input/entry nama belakang
NAMA_BELAKANG = tk.StringVar() # variabel tempat  menangkap/menmpung inpunya
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)# (objek framenya, nama variabel untuk menangkap/menmpung inpunya)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)
# 5. Tombol
# fungsi ini akan dipanggil oleh tombol
#saat tombol diklik NAMA_DEPAN DAN NAMA_BELAKANG akan ditampilkan di window baru
def tombol_click():
    print(NAMA_BELAKANG.get())
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Apa kabar"
    showinfo(title="menyapa",message=pesan)

#tombolnya
tombol_sapa = ttk.Button(input_frame, text="Sapa!",command=tombol_click)
#(objek freme, text tombolnya, command=Tindakan yang akan dipanggil saat tombol ditekan)
tombol_sapa.pack(padx=10,pady=10,fill="x",expand=True)


window.mainloop()