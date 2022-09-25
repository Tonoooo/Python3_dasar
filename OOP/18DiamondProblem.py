# Diamond Problem
# salah satu masalah ketika kita menggunakan multiple inheritence
# kenapa disebut diamond problem? karna berbentuk diamond


class A:
    def show(self):
        print("ini adalah method A")

class B(A):
    def show(self):
        print("ini adalah method B")

class C(A):
    def show(self):
        print("ini adalah method C")

class D(B,C): # ini multiple inheritance
    pass


##class b inherit dari class a,class c juga inherit dari class a, dan class d inherit dari class b dan c
#  kita liat dulu urutan eksekusinya dengan menggunakan help(namaobjek)
#  maka setelah kita melihat urutannya jadi urutannya/ordernya adalah 
#  dari d jika tidak ada  ke b jika tidak ada ke c jika tidak ada ke a,
#  jadi sesuai urutannya (class D(B,C)) dari d jika tidak ada  ke b jika tidak ada ke c jika 
#  tidak ada ke a. kenapa jika tidak ada method atauapapunitu nyarinya malah ke class a padahal tidak ada 
#  disininya(class D(B,C)) ? karna class b dan c merupakan inheritance dari class a



objek = D()
objek.show()
#help(objek)