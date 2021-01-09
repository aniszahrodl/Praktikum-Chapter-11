from datetime import *
from datetime import datetime as dtm

dat=open('d:\dataPerpus.txt','r')
isi=list(dat.readlines())

List1=[]
for i in range(len(isi)):
    ekstrak=(isi[i]).split()
    List1.append(ekstrak[0])

List2=[]
for x in range(len(List1)):
    ekstrak2=List1[x].split('|')
    List2.append(ekstrak2)

data=[]
for y in range (len(List2)):
    P=List2[y]
    D=dict(kode=P[0],nama=P[1],judul=P[2],pinjam=P[3],maks=P[4])
    data.append(D)

#memecah data dan masing-masing dibuat list
KODE=[]
NAMA=[]
JUDUL=[]
PINJAM=[]
MAKS=[]
KEMBALI=[]
for i in range(len(data)):
    a=data[i]
    KODE.append(a['kode'])
    NAMA.append(a['nama'])
    JUDUL.append(a['judul'])
    PINJAM.append(a['pinjam'])
    MAKS.append(a['maks'])

def diffDate(x):
    Now= datetime.date(datetime.now())
    P= datetime.date(dtm.strptime(x, '%Y-%m-%d'))
    i=Now-P
    global T
    T=i.days

#cari NIP
cari=input('Masukkan kode Member yang dicari:')
if cari not in KODE:
    print('Data Member tidak ditemukan')
else:
    print('Kode Member\t\t:',cari)
    Q=KODE.index(cari)
    print('Nama Member\t\t:',NAMA[Q])
    print('Judul Buku\t\t:',JUDUL[Q])
    print('Tanggal Pinjam\t\t:',PINJAM[Q])
    print('Tanggal Maks Peminjaman\t:',MAKS[Q])
    print('Tanggal Pengembalian\t:',str(datetime.date(datetime.now())))
    diffDate(PINJAM[Q])
    print('Terlambat\t\t:',T,'hari')
    M=2000*T
    print('Denda\t\t\t: Rp.',str(M))

    
