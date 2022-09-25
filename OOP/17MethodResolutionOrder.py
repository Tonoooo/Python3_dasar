# Method Resolution Order
# materi Method Resolution Order berhubungan dengan materi multiple inheritace
# urutan eksekusinya

class A:
    def show(self):
        print("ini adalah method A")

class B:
    def show(self):
        print("ini adalah method B")

class C(A,B):
    def show(self):
        print("ini adalah method C")

objek = C()
#objek.show()


# materi penjelasan Method Resolution Order:
# apa jadinya jika nama method sama?,dipython ada yang namanya Method Resolution Order-
#   kita liat dulu urutan eksekusinya dengan menggunakan help(namaobjek)
#   setelah kita melihat urutannya jadi urutannya/ordernya adalah dari C ke A ke B
#   maka methodnya diambilyang manadulu? dari class c ke class a ke class b
#   jadi Method Resolution Order yang diInheritace ke sebuah class itu tergantung dari urtuan
#   contoh:(class C(A,B)) maka urutan eksekusinya dari c ke a ke b
#   conoth lain: (class Z(B,A)) maka urutan eksekusinya dari z ke b ke a

help(objek)