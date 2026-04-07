# =========================================
# Day 7 - Login + Data Pribadi
# =========================================

# Soal:
# Buat program:
# - Register & Login
# - Setiap user punya data sendiri (nama & umur)
# - Setelah login:
#   1. Tambah data
#   2. Lihat data sendiri
#   3. Update data
#   4. Hapus data
#   5. Logout


# list untuk menyimpan semua user
users = []


# ================= REGISTER =================
def register():
    # input username & password
    username = input("Masukkan username:")
    password = input("Masukkan password:")

    print("Daftar berhasil")

    # simpan user ke dalam list users
    users.append({
        "username": username,   # menyimpan username
        "password": password,   # menyimpan password
        "data": {}              # data kosong (nanti diisi nama & umur)
    })


# ================= LOGIN =================
def login(users):
    while True:
        username = input("Masukkan username:")
        password = input("Masukkan password:")

        # looping semua user
        for i in users:
            # cek apakah username & password cocok
            if username == i["username"] and password == i["password"]:
                print("Login berhasil")
                return i  # return user yg login (disimpan ke variabel a)

        # kalau tidak ada yang cocok
        print("Username atau password salah")


# ================= MENU =================

def tambah_data():
    print("~Silahkan isi nama dan umur~")

    # kalau data sudah ada, tidak boleh tambah lagi
    if a["data"]:
        print("Data sudah ada, gunakan update")
        return

    # input nama (harus huruf)
    while True:
        nama = input("Masukkan nama:")
        # replace(" ","") supaya spasi tetap boleh
        if nama.replace(" ", "").isalpha():
            break
        else:
            print("Hanya huruf!\n")

    # input umur (harus angka)
    while True:
        try:
            umur = int(input("Masukkan umur:"))
            break
        except ValueError:
            print("Hanya angka")

    # simpan ke data milik user yg login
    a["data"] = {
        "nama": nama,
        "umur": umur
    }


def lihat_data():
    # kalau data kosong
    if not a["data"]:
        print("Belum ada data")
        return

    # tampilkan data milik user yg login
    print("\n===DATA===")
    print("Nama:", a["data"]["nama"])
    print("Umur:", a["data"]["umur"])


def update():
    # kalau belum ada data
    if not a["data"]:
        print("Belum ada data")
        return

    # input data baru
    nama = input("Masukkan nama:")
    umur = input("Masukkan umur:")

    # update data milik user
    a["data"]["nama"] = nama
    a["data"]["umur"] = umur


def hapus():
    # kalau sudah kosong
    if not a["data"]:
        print("Data sudah kosong")
        return

    # hapus data dengan mengosongkan dict
    a["data"] = {}
    print("Data berhasil dihapus")


# ================= MAIN =================

# daftar user dulu
register()

while True:
    # login → hasilnya disimpan ke variabel a (current_user)
    a = login(users)

    while True:
        print("\n=== MENU ===")
        print("1. Menambah data")
        print("2. Tampilkan data")
        print("3. Update data")
        print("4. Hapus data")
        print("5. Logout")

        pilihan = input("Pilih:")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            lihat_data()
        elif pilihan == "3":
            update()
        elif pilihan == "4":
            hapus()
        elif pilihan == "5":
            print("Telah logout")
            break
        else:
            print("Pilihan tidak ada!")
