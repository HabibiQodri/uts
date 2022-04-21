
print("Banyak bilangna genap yang akan ditampilkan (dimulai dari 2) : ")
bilangan = int(input("Masukkan banyak bilangan = "))

bilagan_genap = 2
i = 1

while i <= bilangan:
    i += 1
    bilagan_genap += 2
    # menghentikan perulangan jika bilangan lebih dari 20
    if bilagan_genap > 50:
        print("Perulangan dihentikan karena melewati batas jumlah bilangan")
        break

    # menampilkan string pada kondisi bilangan = 10
    if bilagan_genap == 10:
        print("Anda Telah Sampai Pada Bilangan 10 ")
        continue
    print(f"{bilagan_genap} ")
