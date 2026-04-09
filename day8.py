#=== DATA ===#

# list untuk menyimpan semua user
users = []

#=== REGISTER ===#
def register():
    username = input("Masukkan username: ")  # input username
    password = input("Masukkan password: ")  # input password

    # simpan user baru ke dalam list users
    users.append({
        "username": username,
        "password": password,
        "data": []  # setiap user punya data sendiri (list)
    })

    print("Daftar berhasil")  # konfirmasi berhasil daftar

#=== LOGIN ===#
def login(users):
    while True:
        username = input("Masukkan username: ")  # input username login
        password = input("Masukkan password: ")  # input password login

        # cek setiap user dalam list
        for i in users:
            # jika username dan password cocok
            if username == i["username"] and password == i["password"]:
                print("Login berhasil")
                return i  # return user yang login

        # jika tidak ketemu user
        print("Username atau password salah")

#=== TAMBAH DATA ===#
def tambah_data(user):
    # input nama sampai valid
    while True:
        nama = input("Masukkan nama: ")  # input nama

        # cek hanya huruf (boleh spasi)
        if nama.replace(" ", "").isalpha():
            break
        print("Hanya huruf!")  # error jika bukan huruf

    # input umur sampai valid angka
    while True:
        try:
            umur = int(input("Masukkan umur: "))  # input umur
            break
        except ValueError:
            print("Hanya angka!")  # error jika bukan angka

    # simpan data ke user yang login
    user["data"].append({
        "nama": nama,
        "umur": umur
    })

#=== LIHAT DATA ===#
def lihat_data(user):
    print("\n=== DATA ===")

    # jika data kosong
    if not user["data"]:
        print("Belum ada data")
        return

    # tampilkan semua data user
    for i in user["data"]:
        print("Nama:", i["nama"], "| Umur:", i["umur"])

#=== HAPUS DATA ===#
def hapus(user):
    nama = input("Masukkan nama yang mau dihapus: ")  # input nama target

    # cari data berdasarkan nama
    for i in user["data"]:
        if i["nama"] == nama:
            user["data"].remove(i)  # hapus data dari list
            print("Data berhasil dihapus")
            return

    print("Data tidak ditemukan")  # jika tidak ketemu

#=== PROGRAM UTAMA ===#
register()  # jalankan register awal

while True:
    a = login(users)  # simpan user yang sedang login

    while True:
        print("\n=== MENU ===")
        print("1. Tambah data")
        print("2. Lihat data")
        print("3. Hapus data")
        print("4. Logout")

        pilihan = input("Pilih: ")  # input pilihan menu

        if pilihan == "1":
            tambah_data(a)  # tambah data ke user login
        elif pilihan == "2":
            lihat_data(a)  # tampilkan data user
        elif pilihan == "3":
            hapus(a)  # hapus data user
        elif pilihan == "4":
            print("Logout berhasil")  # keluar dari menu
            break
        else:
            print("Pilihan tidak ada")  # input tidak valid
