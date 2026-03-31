# Day 2 - Latihan Filter & Search Data

# Soal:
# Buat program untuk:
# 1. Mencari siswa berdasarkan nama (search)
# 2. Mengambil semua siswa yang lulus (nilai >= 75)
# 3. Mengambil siswa dengan nilai >= batas tertentu
# 4. Mengambil SEMUA siswa dengan nilai tertinggi

# =========================
# FUNCTION
# =========================

def cari_siswa(data, nama):  # search
    for i in data:
        if i["nama"] == nama:
            return i
    return "Tidak ditemukan"


def siswa_lulus(data):  # filter lulus
    lulus = []
    for i in data:
        if i["nilai"] >= 75:
            lulus.append(i["nama"])
    return lulus


def nilai_tertentu(data, batas):  # filter berdasarkan batas
    hasil = []
    for i in data:
        if i["nilai"] >= batas:
            hasil.append(i["nama"])
    return hasil


def cari_tertinggi(data):  # ambil semua nilai tertinggi
    maks = data[0]["nilai"]

    # cari nilai max
    for i in data:
        if i["nilai"] > maks:
            maks = i["nilai"]

    # ambil semua yg sama dengan max
    hasil = []
    for i in data:
        if i["nilai"] == maks:
            hasil.append(i["nama"])

    return hasil


# =========================
# DATA CONTOH
# =========================

data = [
    {"nama": "Adit", "nilai": 80},
    {"nama": "Budi", "nilai": 70},
    {"nama": "Citra", "nilai": 90},
    {"nama": "Dina", "nilai": 90},
]

# =========================
# TEST OUTPUT
# =========================

print("Cari siswa:", cari_siswa(data, "Adit"))
print("Siswa lulus:", siswa_lulus(data))
print("Nilai >= 80:", nilai_tertentu(data, 80))
print("Nilai tertinggi:", cari_tertinggi(data))
