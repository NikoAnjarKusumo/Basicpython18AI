x = int(input("masukan nilai teori anda : "))
y = int(input("masukan nilai praktek anda : "))
if x >= 70 and y >= 70:
    print("Selamat, anda lulus!")
elif x >= 70 and y < 70:
    print("Anda harus mengulang ujian praktek")
elif x < 70 and y >= 70:
    print("Anda harus mengulang ujian teori.")
else :
    print("Anda harus mengulang ujian teori dan praktek.")