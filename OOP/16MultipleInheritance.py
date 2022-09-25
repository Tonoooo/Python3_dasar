# Multiple Inheritance
# adalah suatu class yang menerima warisan/turunan dari banyak class

# ini berhubungan dengan modeul contoh.py


class A:
    
    def method_a(self):
        print("ini adalah method A")

class B:
    
    def method_b(self):
        print("ini adalah method B")

# ini multipel inheritance jadi dia bisa ngambil dua buah super class
class C(A,B): # jadi si class C ini berlaku sbg class A iya dan juga berlaku class B
    pass


objek = C()
objek.method_a()
objek.method_b()