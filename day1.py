# Soal:
# Buat program untuk analisis nilai siswa:
# - rata-rata
# - nilai tertinggi & terendah
# - jumlah lulus & tidak lulus
# - kategori nilai (A, B, C)
# - pola nilai
# - cek nilai sama

#Tracker nilai + kategori siswa(day 2 bljr dictionary)
def analisis_dasar(data): #rata2 nilai, nilai tertinggi, terendah
    total = 0
    tertinggi = data[0]["nilai"]
    terendah = data[0]["nilai"]
    for i in data:
        x = i["nilai"]#karna ada 2 "elemen" dalam list 'data'
        if x > tertinggi:
            tertinggi = x
        if x < terendah:
            terendah = x
        total += x
    rata2 = total/len(data)
    return {       #dictionary
        "maks":tertinggi,
        "minim":terendah,
        "rata2":rata2
    }

def status(data): #jmlh siswa lulus, tdk lulus, nama siswa tdk lulus
    lulus = 0 #siswa lulus
    tidak = 0 #siswa tidak lulus
    nama = [] #nama siswa tidak lulus
    for i in data:
        x = i["nilai"]
        if x >= 75:
            lulus += 1
        else:
            tidak += 1
            nama.append(i["nama"])
    return {
        "lulus":lulus,
        "tidak":tidak,
        "nama":nama
    }

def kategori_nilai(data): # >=85=="A", >=75=="B", <75=="C" 
    a = 0
    b = 0
    c = 0
    for i in data:
        x = i["nilai"]
        if x >= 85:
            a += 1
        elif x >= 75:
            b += 1
        else:
            c += 1
    return {
        "a":a,
        "b":b,
        "c":c
    }

def pola_nilai(data): #pola naik/turun/campuran
    naik = True #definisi gw naik harus strict
    turun = True #turun juga harus strict
    for i in range (1,len(data)):
        sebelumnya = data[i-1]["nilai"]
        sekarang = data[i]["nilai"]
        if sekarang <= sebelumnya:
            naik = False
        if sekarang >= sebelumnya:
            turun = False
    if len(data) < 2: #edge case bila data kurang dari 2
        return None
    if naik:
        return "Naik"
    elif turun:
        return "Turun"
    else:
        return "Campuran"

def nilai_sama(data): #mencari nilai yang sama
    sama = False
    seen = [] #penampung nilai yang sudah dicek
    for i in data:
        x = i["nilai"]
        if x in seen:
            sama = True
            break
        else:
            seen.append(x)
    return sama

def gabung(data): #untuk menggabungkan semua function agar mudah memanggilnya
    a = analisis_dasar(data)
    b = status(data)
    c = kategori_nilai(data)
    return {
        "maks":a["maks"],
        "minim":a["minim"],
        "rata2":a["rata2"],
        "lulus":b["lulus"],
        "tidak":b["tidak"],
        "nama":b["nama"],
        "a":c["a"],
        "b":c["b"],
        "c":c["c"],
        "pola":pola_nilai(data),
        "sama":nilai_sama(data)
    }

def output(data): #agar lebih rapi di main loop
    a = gabung(data)
    return f"""
Rata-rata:{round(a["rata2"],1)}
Nilai tertinggi:{a["maks"]}
Nilai terendah:{a["minim"]}

Lulus:{a["lulus"]}
Tidak lulus:{a["tidak"]}
siswa tidak lulus:{a["nama"]}

Kategori A:{a["a"]}
Kategori B:{a["b"]}
Kategori C:{a["c"]}

Pola nilai:{a["pola"]}
Ada nilai sama:{a["sama"]}
"""

#mulai loop utama
data = []
while True:
    nama = input(f"Masukkan nama(ketik 'stop' for break):") #input nama
    if nama == "stop": #break loop
        break
    if nama.isdigit(): #edge case jika user input angka
        print("Hanya huruf!")
        continue
    while True: #loop buat input nilai
        nilai = input(f"Masukkan nilai:")
        try:
            nilai = int(nilai)
            break
        except:
            print("Hanya angka!")
    data.append({ #nambah hasil ke list data
        "nama":nama,
        "nilai":nilai
    })
if data: #edge case, artinya jika data ga kosong
    print(output(data)) #nah kan lebih rapi
else:
    print("Tidak ada data")
