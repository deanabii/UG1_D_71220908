total = 0
while True:
    harga = input("Harga barang : ")
    try:
        harga = int(harga)
        total  += harga
        tambah = input("Apakah anda membeli barang lagi? [yes/no]: ")
        if tambah.lower() == "no":
            break
    except:
        print("INVALID")

print("Total harga:", total)

