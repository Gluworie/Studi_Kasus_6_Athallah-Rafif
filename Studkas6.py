import json
import os

NAMA_FILE = r"C:\Users\Rapip\Downloads\KULIAH\PRAKTIKUM\Praktikum DDP\STUDI KASUS 6\Studkas6.json"


def baca_data():
    if os.path.exists(NAMA_FILE):
        with open(NAMA_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []
    return data

def simpan_data(data):
    with open(NAMA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def tampilkan_barang():
    data = baca_data()
    if len(data) == 0:
        print("belum ada barang di gudang")
        return
    print("\n--- DATA BARANG GUDANG ---")
    no = 1
    for barang in data:
        print(str(no) + ". " + barang["nama"] + " | stok: " + str(barang["stok"]) + " | harga: Rp" + str(barang["harga"]))
        no += 1
    print("--------------------------\n")

def tambah_barang():
    data = baca_data()
    nama = input("nama barang: ")
    stok = input("jumlah stok: ")
    harga = input("harga satuan: ")

    barang_baru = {
        "nama": nama,
        "stok": int(stok),
        "harga": int(harga)
    }

    data.append(barang_baru)
    simpan_data(data)
    print("barang berhasil ditambahin ke gudang!\n")

while True:
    print("=== MENU INVENTARIS TOKO ===")
    print("1. Lihat data barang")
    print("2. Tambah barang baru")
    print("3. Keluar")
    pilih = input("masukin pilihan: ")

    if pilih == "1":
        tampilkan_barang()
    elif pilih == "2":
        tambah_barang()
    elif pilih == "3":
        print("oke, program ditutup. sampai jumpa!")
        break
    else:
        print("pilihan ga valid, coba lagi\n")