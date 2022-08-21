nama = ['']
notlp = ['']

#fungsi daftar kontak
def daftarkontak():
    print("Daftar Kontak : \n")
    for n in range (len(nama)):
        print ("Nama : " + nama[n])
        print ("Nomor Telepon : " + notlp[n])
        print("")

#fungsi menambah kontak
def tambahkontak():
    nama.append(input("Nama : "))
    notlp.append(input("No Telepon : "))
    print("Kontak Berhasil Ditambahkan")
    print("")

#fungsi menu
print('Selamat Datang !')
while True:
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    menu = int(input("Pilih Menu : "))

    if menu == 1:
        daftarkontak()
    elif menu == 2:
        tambahkontak()
    elif menu == 3:
        print(" Program Selesai. Sampai Jumpa !")
        break
    else :
        print("Menu Tidak Tersedia\n")