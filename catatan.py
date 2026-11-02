import json
import os

NAMA_FILE = "catatan.json"

def muat():
    if os.path.exists(NAMA_FILE):
        try:
            with open(NAMA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            os.replace(NAMA_FILE, "catatan_rusak.json")
            print("File catatan rusak, mulai dari kosong.")
    return []

def simpan(data):
    with open(NAMA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

catatan = muat()

while True:
    print("\n1. Tambah 2. Lihat 3. Hapus 4. Keluar")
    pilihan = input("Pilih: ")

    if pilihan == "1":
        while True:
            teks = input("Tulis catatan: ")
            if not teks.strip():
                print("Catatan tidak boleh kosong: ")
                continue
            catatan.append(teks)
            simpan(catatan)           
            print(f"Tersimpan! Total catatan: {len(catatan)}")
            break

    elif pilihan == "2":
        if not catatan:
            print("Belum ada catatan.")
        else:
            print("\n=== Daftar catatan ===")
            for nomor, teks in enumerate(catatan, start=1):
                print(f"{nomor}. {teks}")

    elif pilihan == "3":
        if not catatan:
            print("Belum ada catatan untuk di hapus.")
        else:
            print("\n=== Daftar catatan ===")
            for nomor, teks in enumerate(catatan, start=1):
                print(f"{nomor}. {teks}")
            while True:
                try:
                    nomor = int(input("Nomor yang dihapus: "))
                except ValueError:
                    print("Input harus berupa nomor:")
                    continue
                if 1 <= nomor <= len(catatan):
                    dihapus = catatan.pop(nomor -1)
                    simpan(catatan)
                    print(f"Dihapus: {dihapus}")
                    break
                else:
                    print("Nomor tidak ada.")
    elif pilihan =="4":
        print("Sampai jumpa")
        break
    else:
        print(f"Kamu memilih {pilihan}")