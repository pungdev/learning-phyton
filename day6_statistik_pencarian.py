def pause():
    input("Tekan enter untuk melanjutkan...")


# =========================
# CARI SISWA (PARTIAL)
# =========================
def cari_siswa(data):
    cari = input("Cari nama:")
    siswa = []

    for i in data:
        if cari in i["nama"]:  # partial search (mengandung)
            siswa.append(i["nama"])

    if len(siswa) > 0:
        for i in siswa:
            print(i)
        pause()
        return

    print("Tidak ditemukan")
    pause()


# =========================
# STATISTIK NILAI
# =========================
def statistik_nilai(data):
    lulus = 0
    tidak = 0
    total = 0

    for i in data:
        total += i["nilai"]

        if i["nilai"] >= 75:
            lulus += 1
        else:
            tidak += 1

    jumlah = len(data)
    rata2 = total / len(data)

    print(f"\nRata-rata:{rata2}")
    print(f"Jumlah siswa:{jumlah}")
    print(f"Lulus:{lulus}")
    print(f"Tidak lulus:{tidak}")
    pause()


# =========================
# TOP 3 SISWA
# =========================
def top_siswa(data):
    hasil = []

    # ❗ pakai data copy dari luar biar aman
    while len(data) > 0 and len(hasil) < 3:
        maks = data[0]["nilai"]

        # cari nilai terbesar
        for i in data:
            if i["nilai"] > maks:
                maks = i["nilai"]

        # ambil semua yg nilainya sama
        for i in data[:]:  # pakai [:] biar aman saat remove
            if maks == i["nilai"]:
                hasil.append(i)
                data.remove(i)  # ❗ ini yang bikin data kehapus

    return hasil


# =========================
# CARI BERDASARKAN NILAI
# =========================
def cari_nilai(data):
    try:
        cari = int(input("Cari:"))  # ❗ error terjadi di sini kalau bukan angka
    except ValueError:
        print("Hanya angka")
        pause()
        return  # ❗ WAJIB, biar ga lanjut error

    siswa = []

    for i in data:
        if i["nilai"] >= cari:
            siswa.append(i)

    if len(siswa) > 0:
        for i in siswa:
            print(f"{i['nama']}-{i['nilai']}")
        pause()
        return

    print("Data tidak ada")
    pause()


# =========================
# TAMPILKAN SEMUA DATA
# =========================
def tampilkan(data):
    print()  # biar ada jarak
    for i in data:
        print(f"{i['nama']}-{i['nilai']}")
    pause()


# =========================
# INPUT DATA
# =========================
data = []

while True:
    nama = input("Masukkan nama(ketik 'stop' for break):")

    if nama == "stop":
        break

    if nama.isdigit():
        print("Hanya huruf!\n")
        continue

    while True:
        try:
            nilai = int(input("Masukkan nilai:"))
            break
        except ValueError:
            print("Hanya angka!")

    data.append({
        "nama": nama,
        "nilai": nilai
    })


# =========================
# MENU
# =========================
while True:
    print("\n=== MENU ===")
    print("1.Cari siswa")
    print("2.Statistik nilai")
    print("3.Top 3 siswa")
    print("4.Cari berdasarkan nilai")
    print("5.Tampilkan semua data")
    print("6.Keluar")

    pilihan = input("Pilih:")

    if pilihan == "1":
        cari_siswa(data)

    elif pilihan == "2":
        statistik_nilai(data)

    elif pilihan == "3":
        hasil = top_siswa(data[:])  # ❗ pakai copy biar data asli aman

        print()
        for i in hasil:
            print(f"{i['nama']}-{i['nilai']}")

        pause()

    elif pilihan == "4":
        cari_nilai(data)

    elif pilihan == "5":
        tampilkan(data)

    elif pilihan == "6":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak ada")
