# Operator Bitwise bisa dikatakan juga sbgai operasi biner atau binary

# penjelasan Operator Bitwise
# ada di video :
# link   https://youtu.be/-VrqfCGwr88
# atau dikomputer E:\belajar\code\python\VideoTutorialPython


# bitwise adalah operasi pada masing masing bit
# index dimulai dari 0


a = 9
b = 5

# bitwise OR (|)
c = a|b
print("\n========OR======")
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('-------------------------------(|)')
print('nilai :',c,', binary :',format(c,'08b'))

# bitwise AND (&)
c = a & b
print("\n========AND=====")
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('-------------------------------(&)')
print('nilai :',c,' , binary :',format(c,'08b'))

# bitwise XOR (&)
c = a ^ b
print("\n========XOR=====")
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('-------------------------------(^)')
print('nilai :',c,' , binary :',format(c,'08b'))

# bitwise NOT (~)
c = ~a
print("\n========NOT=====")
print('nilai :',a,' , binary :',format(a,'08b'))
print('-------------------------------(~)')
print('nilai :',c,' , binary :',format(c,'08b'))
print('-------------------------------(^)')
d = 0b00001001
e = 0b11111111
print('nilai :',e^d,' , binary :',format(e^d,'08b'))


# shifting

# shift right
c = a >> 1   # artinya a geser satu kali
print("\n======= >> ======")
print('nilai :',a,' , binary :',format(a,'08b'))
print('-------------------------------(>>)')
print('nilai :',c,' , binary :',format(c,'08b'))

# shift lefht
c = a << 1   # artinya a geser satu kali
print("\n======= << ======")
print('nilai :',a,' , binary :',format(a,'08b'))
print('-------------------------------(<<)')
print('nilai :',c,' , binary :',format(c,'08b'))