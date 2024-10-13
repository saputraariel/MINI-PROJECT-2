from prettytable import PrettyTable

#VARIABLE TABEL
tabel1 = PrettyTable()
tabel2 = PrettyTable()
#----------------------
tabel3 = PrettyTable()
tabel3.title = "-Rissyyyy Storeee-"
tabel3.field_names = ["aman dan terpercaya"]
#--------------------------------------------
tabel4 = PrettyTable()
tabel5 = PrettyTable()
tabel10 = PrettyTable()


#TABEL HARGA AWAL
gitar1 = "1. Gitar Klasik"
gitar2 = "2. Gitar Listrik"
gitar3 = "3. Gitar Bass"
gitar4 = "4. Gitar Akustik"
harga1 = "Rp. 600.000"
harga2 = "Rp. 2.000.000"
harga3 = "Rp. 1.800.000"
harga4 = "Rp. 900.000"
#TABEL
tabel10.title = "Rissy Store"
tabel10.field_names = ["Jenis Gitar", "Harga"]
tabel10.add_row([gitar1,harga1])
tabel10.add_row([gitar2,harga2])
tabel10.add_row([gitar3,harga3])
tabel10.add_row([gitar4,harga4])

def menu_utama():
    while True:
        print(tabel3)
        nama = input("Masukan Nama Anda = ")
        role = input("Masukan Role Anda 'Admin/Pembeli' = ")
        if role.lower() == "admin":
            tabel1.field_names = ["Nama", "Role"]
            tabel1.add_row([nama, role])
            print(tabel1)
            admin()
        elif role.lower() == "pembeli":
            saldo = 10000000
            tabel2.field_names = ["Nama", "Role", "Saldo"]
            tabel2.add_row([nama, role,saldo])
            print(tabel2)
            pembeli()

        else:
            print("Masukan Role Dengan Benar!")
            print("----------------------------")
            continue

def admin():
    print("Pilih Opsi Selanjutnya!")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    next1 = input("Masukan Pilihan Anda = ")

    #MEMBUAT LIST HARGA BARU
    if next1 == "1":
        print("----------------------------")
        gitarbaru = str(input("Masukan Barang Baru = "))
        hargabaru = str(input("Masukan Harga Baru = "))
        tabel10.add_row([gitarbaru,hargabaru])
        print(tabel10)
        print("Barang Berhasil Di Tambahkan!")
        opsi()
    
    elif next1 == "2":
        print(tabel10)
        opsi()

    elif next1 == "3":
        print("----------------------------------")
        print("Pilih Fitur yang mau Di Update!")
        print("1. Ganti Judul")
        print("2. Ganti Sub Judul")
        print("----------------------------------")
        ubah = input("Pilih Yang Mau Di Ubah = ")
        print("----------------------------------")
        if ubah == "1":
            judulbaru = input("Masukan Judul Baru = ")
            tabel10.title = judulbaru
            print(tabel10)
            opsi()
        elif ubah == "2":
            subjudul = input("Masukan SubJudul Pertama = ")
            subjudul1 = input("Masukan SubJudul Kedua = ")
            tabel10.field_names = [subjudul,subjudul1]
            print(tabel10)
            opsi()
    
    elif next1 == "4":
        print("-------------------------")
        print("1. Hapus Judul")
        print("2. Hapus Subjudul")
        print("-------------------------")
        opsidel = input("Masukan Yang ingin Di hapus = ")
        if opsidel == "1":
            tabel10.title = ""
            print(tabel10)
            opsi()
        
        elif opsidel == "2":
            tabel10.field_names = ""
            print(tabel10)
            opsi()
                

def pembeli():
    print(tabel10)
    beli = input("Pilih yang ingin anda beli = ")
    if beli == "1":
        saldo = 10000000
        buy = saldo - 6000000
        print("Barang Berhasil Di beli")
        print("Sisa Saldo Anda Adalah", buy)
        opsi()
    else:
        print()

def opsi():
    while True:
        print("-----------")
        print("1. Home")
        print("2. Log out")
        print("3. Exit")
        print("-----------")
        pilihan = input("Masukan Pilihan Anda = ")
        if pilihan == "1":
            print("Anda Kembali ke Home")
            print("-----------------------")
            admin()
        elif pilihan == "2":
            menu_utama()
        elif pilihan == "3":
            print("ANDA BERHASIL KELUAR")
            exit()
        else:
            print("Input Angka Tidak Sesuai!")
            continue
        


#BUAT NGEBACA DEF MENGGUNAKAN (VARIABLE = DEF)
while True:
    nama = menu_utama()
    role = menu_utama()
    saldo = 10000000



