# Day 4 - Analisis + Ranking Siswa

# Soal:
# Buat program untuk:
# - input nama & nilai siswa
# - menghitung rata-rata nilai
# - mencari nilai tertinggi & terendah (nama + nilai)
# - menampilkan jumlah siswa lulus (>=75) dan yang tidak lulus
# - mengecek apakah ada nilai yang sama
# - menampilkan ranking dari tertinggi ke terendah (tanpa sort)

# =========================
# FUNCTION ANALISIS
# =========================
def analisis(data):
    total = 0
    tertinggi = []  # menampung semua siswa dengan nilai tertinggi
    terendah = []   # menampung semua siswa dengan nilai terendah

    maks = data[0]["nilai"]   # ambil nilai pertama sebagai awal
    minim = data[0]["nilai"]

    for i in data:
        total += i["nilai"]  # jumlahkan semua nilai

        # cari nilai maksimum
        if i["nilai"] > maks:
            maks = i["nilai"]

        # cari nilai minimum
        if i["nilai"] < minim:
            minim = i["nilai"]

    rata2 = total / len(data)

    # ambil semua siswa yang punya nilai tertinggi & terendah
    for i in data:
        if maks == i["nilai"]:
            tertinggi.append(i)
        if minim == i["nilai"]:
            terendah.append(i)

    return {
        "maks": tertinggi,
        "minim": terendah,
        "rata2": rata2
    }


# =========================
# FUNCTION RANKING (MANUAL)
# =========================
def ranking(data):
    hasil = []

    # ulangi selama data masih ada
    while len(data) > 0:
        maks = data[0]["nilai"]

        # cari nilai terbesar
        for i in data:
            if i["nilai"] > maks:
                maks = i["nilai"]

        # ambil semua yang nilainya sama dengan maks
        for i in data[:]:  # pakai [:] biar aman saat remove
            if maks == i["nilai"]:
                hasil.append(i)
                data.remove(i)  # hapus dari data supaya tidak dipakai lagi

    return hasil


# =========================
# FUNCTION FILTER LULUS
# =========================
def filter_lulus(data):
    lulus = []
    tdklulus = []

    # cek siapa saja yang lulus
    for i in data:
        if i["nilai"] >= 75:
            lulus.append(i["nama"])

    # cek yang tidak lulus
    for i in data:
        if i["nama"] not in lulus:
            tdklulus.append(i["nama"])

    jumlah = len(lulus)

    return {
        "jumlah": jumlah,
        "tidak": tdklulus
    }


# =========================
# FUNCTION CEK NILAI SAMA
# =========================
def same(data):
    seen = []   # penampung nilai yang sudah dicek
    sama = False

    for i in data:
        if i["nilai"] in seen:
            sama = True
            break
        else:
            seen.append(i["nilai"])

    return sama


# =========================
# FUNCTION GABUNG SEMUA
# =========================
def gabung(data):
    a = analisis(data)
    b = filter_lulus(data)

    return {
        "maks": a["maks"],
        "minim": a["minim"],
        "rata2": a["rata2"],
        "jumlah": b["jumlah"],
        "tidak": b["tidak"],
        "hasil": ranking(data[:]),  # pakai copy biar data asli ga kehapus
        "sama": same(data)
    }


# =========================
# FUNCTION OUTPUT
# =========================
def output(data):
    a = gabung(data)

    return f"""
Rata-rata:{a["rata2"]}
Tertinggi:{a["maks"][0]["nama"]}-{a["maks"][0]["nilai"]}  # [0] ambil data pertama dari list
Terendah:{a["minim"][0]["nama"]}-{a["minim"][0]["nilai"]}
Lulus:{a["jumlah"]}
Tidak lulus:{a["tidak"]}
Ada nilai sama:{a["sama"]}
"""


# =========================
# INPUT DATA
# =========================
data = []

while True:
    nama = input("Masukkan nama(ketik 'stop' untuk berhenti):")

    if nama == "stop":
        break

    if nama.isdigit():  # validasi nama tidak boleh angka
        print("Hanya huruf!")
        continue

    while True:
        nilai = input("Masukkan nilai:")

        try:
            nilai = int(nilai)  # ubah ke integer
            break
        except:
            print("Hanya angka!")

    data.append({
        "nama": nama,
        "nilai": nilai
    })


# =========================
# OUTPUT AKHIR
# =========================
if data:
    hasil = ranking(data[:])  # pakai copy biar data asli tetap aman

    print(output(data))

    # tampilkan ranking
    for i, item in enumerate(hasil, start=1):
        print(f"{i}. {item['nama']} - {item['nilai']}")
else:
    print("Tidak ada data")
