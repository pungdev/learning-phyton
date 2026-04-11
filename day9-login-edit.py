#login data pribadi
user = []#list data user
def register():
    username = input("Masukkan username:")
    password = input("Masukkan password:")
    print("Register berhasil!")
    user.append({
        "username":username,
        "password":password,
        "data":[]#untuk wadah data milik user
    })

def login():
    while True:
        username = input("Masukkan username:")
        password = input("Masukkan password:")
        for i in user:
            if i["username"] == username and i["password"] == password:
                print("Login berhasil")
                return i #return user yg login
        print("username atau password salah")

def tambah(a):
    while True:
        nama = input("Masukkan nama:")
        if nama.replace(" ","").isalpha():#validasi input
            print("nama valid")
            break
        print("Hanya huruf!")
    while True:
        try:
            umur = int(input("Masukkan umur:"))#validasi input
            break
        except ValueError:
            print("Hanya angka")
    a["data"].append({
        "nama":nama,
        "umur":umur
    })

def tampilkan(a):
    if not a["data"]:#jika tidak ada data
        print("Belum ada data")
        return
    for i in a["data"]:
        print(i)

def edit(a):
    nama = input("Cari nama:")
    for i in a["data"]:
        if i["nama"] == nama:
            nama_baru = input("Masukkan nama baru:")
            umur_baru = input("Masukkan umur baru:")
            i["nama"] = nama_baru
            i["umur"] = umur_baru
            return
    print("Data tidak ditemukan!")

register()
while True:
    a = login()
    while True:
        print("===MENU===")
        print("1.Tambah data")
        print("2.Lihat data")
        print("3.Edit data")
        print("4.Logout")
        pilih = input("Masukkan pilihan:")
        if pilih == "1":
            tambah(a)
        elif pilih == "2":
            tampilkan(a)
        elif pilih == "3":
            edit(a)
        elif pilih == "4":
            break
        else:
            print("Pilihan tidak valid")
