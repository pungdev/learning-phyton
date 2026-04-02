# Day 3 - Ranking Siswa (Manual Sorting + Input)

# Soal:
# Buat program untuk:
# - input nama & nilai siswa
# - mengurutkan dari nilai tertinggi ke terendah (tanpa sort)
# - menampilkan ranking (1, 2, 3, dst)

# =========================
# FUNCTION
# =========================

def ranking(data):
    hasil = []

    while len(data) > 0:
        maks = data[0]["nilai"]

        # cari nilai terbesar
        for i in data:
            if i["nilai"] > maks:
                maks = i["nilai"]

        # ambil semua yg nilainya sama
        for i in data[:]:
            if i["nilai"] == maks:
                hasil.append(i)
                data.remove(i)

    return hasil


# =========================
# INPUT
# =========================

data = []

while True:
    nama = input("Masukkan nama (ketik 'stop' untuk berhenti): ")
    if nama == "stop":
        break

    if nama.isdigit():
        print("Nama tidak boleh angka!")
        continue

    while True:
        nilai = input("Masukkan nilai: ")
        try:
            nilai = int(nilai)
            break
        except:
            print("Harus angka!")

    data.append({
        "nama": nama,
        "nilai": nilai
    })


# =========================
# OUTPUT
# =========================

if data:
    hasil = ranking(data)

    for i, item in enumerate(hasil, start=1):
        print(f"{i}. {item['nama']} - {item['nilai']}")
else:
    print("Tidak ada data")
