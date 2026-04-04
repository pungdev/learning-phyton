# Day 5 - CRUD Data Siswa

# Soal:
# Buat program untuk:
# - input data siswa (nama & nilai)
# - menyediakan menu:
#   1. Cari siswa
#   2. Update nilai siswa
#   3. Hapus siswa
#   4. Tampilkan semua data
#   5. Keluar
# - gunakan list of dictionary

# =========================
# PAUSE (BIAR USER GA LANGSUNG LONCAT)
# =========================
def pause():
    input("Tekan enter untuk lanjut...")


# =========================
# CARI SISWA
# =========================
def cari_siswa(data):
    cari = input("\nCari nama:")

    for i in data:  # loop semua data
        if cari == i["nama"]:  # cek nama cocok
            print(f"{i['nama']}-{i['nilai']}")  # tampilkan data
            pause()
            return  # berhenti kalau ketemu

    # kalau tidak ketemu sama sekali
    print("Tidak ditemukan")
    pause()


# =========================
# UPDATE NILAI
# =========================
def update(data):
    cari = input("\nCari nama:")

    for i in data:
        if cari == i["nama"]:
            while True:
                try:
                    baru = int(input("Masukkan nilai baru:"))  # input nilai baru
                    i["nilai"] = baru  # update langsung di dictionary
                    print("Berhasil update")
                    pause()
                    return
                except ValueError:  # error kalau bukan angka
                    print("Harus angka!\n")

    print("Data tidak ditemukan")
    pause()


# =========================
# HAPUS DATA
# =========================
def hapus(data):
    cari = input("\nCari nama:")

    for i in data:
        if cari == i["nama"]:
            data.remove(i)  # hapus data dari list
            print("Data berhasil dihapus")
            pause()
            return  # penting biar ga lanjut ke bawah

    print("Data tidak ditemukan")
    pause()


# =========================
# TAMPILKAN SEMUA DATA
# =========================
def tampilin(data):
    print()

    for i in data:
        print(f"{i['nama']}-{i['nilai']}")  # tampilkan satu per satu

    pause()


# =========================
# INPUT DATA AWAL
# =========================
data = []

while True:
    nama = input("Masukkan nama(ketik 'stop' for break):")

    if nama == "stop":
        break

    if nama.isdigit():  # validasi nama tidak boleh angka
        print("Harus huruf!\n")
        continue

    while True:
        nilai = input("Masukkan nilai:")

        try:
            nilai = int(nilai)  # ubah ke integer
            break
        except:
            print("Harus angka!\n")

    data.append({
        "nama": nama,
        "nilai": nilai
    })


# =========================
# MENU
# =========================
while True:
    print("\n=== MENU ===")
    print("1.Cari")
    print("2.Update")
    print("3.Hapus")
    print("4.Tampilkan")
    print("5.Keluar")

    pilihan = input("Masukkan pilihan:")

    if pilihan == "1":
        cari_siswa(data)

    elif pilihan == "2":
        update(data)

    elif pilihan == "3":
        hapus(data)

    elif pilihan == "4":
        tampilin(data)

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak ada")
