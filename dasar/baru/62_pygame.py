# sumber: https://youtu.be/cQOhLpmR6CY
# membuat game sederhana menggerakan kotak

import pygame

# biasanya saat kita buat game ada strukturnya:
#init(inisialisasi) -> bikin dunia, karakter
#user input / database input()
#update asset
#render ke display 



# 1. init
pygame.init() # init untuk memulai gamenya (menjalankan engine nya)
# variabel running game
isRun = True

# membuat display surface object. dimana ini akan menjadi tempat semua yang kita buat
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))# objek display (lebar,tinggi) atau (x,y)

# objek game. membuat si kotaknya (pemainnya/karakternya).
#posisinya. jika posisi kotanya pindah kekanan/kekiri maka x yang berubah, jika atas/bawah maka y
x = 250
y = 250
#ukuranya
panjang = 20 # pixel
lebar = 20
#kecepatan gerak
speed = 10 # pixel



## pake loop agar siwindownya tidak nutup langsung (agar tetap berjalan)
while isRun:
    # delay agar gerak kotaknya tidak terlalu cepat
    pygame.time.delay(10)
    # 2. user input
    #pygame.event.get() = mengambil semua yang terjadi dengan sipygame
    for event in pygame.event.get():
        # untuk keluar dari windownya pygame. tombol exit(yang dipojok kanan atas)
        if event.type == pygame.QUIT:
            isRun = False # ubah jadi false agar while loopnya berhenti
            break
    ## ambil semua keyboard press
    keys = pygame.key.get_pressed() # mengambil semua yang diketik
    # ambil ke kiri
    if keys[pygame.K_LEFT] and x > 0: # keys[pygame.K_LEFT]=mengambil tombol kiri. x>0 agar sikotaknya tidak jeblos keluar windownya (agar mentok sape sisi)
        x -= speed
    # ke kanan
    if keys[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed
    # ke bawah
    if keys[pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed
    # ke atas
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    # 3. update asset
    # merubah layar nya menjadi warna putih
    window.fill((255,255,255)) # rgb
    # membuat/gambar sebuah kotak
    pygame.draw.rect(window,(255,120,0),(x,y,lebar,panjang)) # (surface objeknya,(warna),(posisi&ukuran))
    # 4. render ke display
    pygame.display.update()

pygame.quit() # keluar 