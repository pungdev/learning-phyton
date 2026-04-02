# Day 3 - Sorting Data Siswa (Manual)

# Soal:
# Buat program untuk mengurutkan data siswa berdasarkan nilai
# dari tertinggi ke terendah TANPA menggunakan sort() atau sorted().
# Data berupa list of dictionary (nama & nilai).
# Hasil berupa list baru yang sudah terurut.

# =========================
# DATA
# =========================

data = [
    {"nama": "Adit", "nilai": 80},
    {"nama": "Budi", "nilai": 70},
    {"nama": "Citra", "nilai": 90}
]

# =========================
# FUNCTION
# =========================

def urutkan_nilai(data):
    hasil = []

    while len(data) > 0:
        maks = data[0]["nilai"]

        # cari nilai terbesar
        for i in data:
            if i["nilai"] > maks:
                maks = i["nilai"]

        # ambil semua yang nilainya sama dengan maks
        for i in data[:]:  # pakai [:] biar aman saat remove
            if i["nilai"] == maks:
                hasil.append(i)
                data.remove(i)

    return hasil

# =========================
# OUTPUT
# =========================

print(urutkan_nilai(data))
