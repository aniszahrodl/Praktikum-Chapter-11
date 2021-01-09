from datetime import *

def Input():
    global kode
    global nama
    global judul
    global tglPinjam
    global maksPinjam
    kode=input('Masukkan Kode Member\t:')
    nama=input('Masukkan Nama Member\t:')
    judul=input('Masukkan Judul Buku\t:')
    tglPinjam= datetime.date(datetime.today())
    maksPinjam= tglPinjam+timedelta(days=7)
    i=maksPinjam-tglPinjam
    p=i.days

def addData(kd, nm, jd, tglP, maksP):    
    file.write(kode)
    file.write('|')
    file.write(nama)
    file.write('|')
    file.write(judul)
    file.write('|')
    file.write(str(tglPinjam))
    file.write('|')
    file.write(str(maksPinjam))
    file.write('\n')
    print('')
    global lagi
    lagi=input('Input lagi? (y/n)\t:')
    print('')

file=open('d:\dataPerpus.txt','w')

Input()
addData(kode, nama, judul, tglPinjam, maksPinjam)
while True:
    if lagi=='y':
        Input()
        addData(kode, nama, judul, tglPinjam, maksPinjam)
    elif lagi=='n':
        file.close()
        print('')
        file2=open('d:\dataPerpus.txt','r')
        print(file2.read())
        break
    else:
        break 

    

