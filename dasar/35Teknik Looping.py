# Teknik Looping


## Teknik Looping di list dan tuple
nama_band = ['payung teduh',
             'fourtwnty',
             'dialog',
             'sonjaya',
             'perahyena',
             'bigbang']

kumpulan_lagu = ['akad',
        'nyaman',
        'rumahku',
        'sang',
        'sindoro',
        'bang bang bang']


# enumerate  = memberi nomor dan index
for iniindex,iniband in enumerate(nama_band):
    print(iniindex,':',iniband)


# zip = menggabungkan list
for band,lagu in zip(nama_band,kumpulan_lagu): # harus memiliki pasangan jika tidak maka tidak akan ditampilkan
    print(band,'menyanyikan lagu:',lagu)


## Teknik Looping di set
print("~~~~ S ~~~~~~~")
playlist = {'dynamit','ptd','dntd','dna','gee','butter','bang bang','love your self'}

for lagu in playlist:
    print(lagu)

# mengurutkan
for lagu in sorted(playlist):
    print(lagu)

## Teknik Looping di dictionary
print("~~~~ D ~~~~~~~")
playlist2 = {'payung teduh':'akad',
             'fourtwnty':'nyaman',
             'dialog':'rumahku'}

# ngambil keys nya saja
for i in playlist2.keys():
    print(i)

# ngambil value nya saja
for i in playlist2.values():
    print(i)

# ngambil semuanya
for i in playlist2.items():
    print(i)

# kalau mau dibagi 2 atau apalah namanya..
for i,o in playlist2.items(): # i itu key nya dan o value nya
    print(i,'lagunya:',o) 


### ini pengetahuan saja
for i in reversed(range(1,10,1)): # dibalik 1 sampai 10 dengan step 1
    print(i)