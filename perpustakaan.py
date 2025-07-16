### ====== PROGRAM PENGELOLAAN DATA PEMINJAMAN BUKU PERPUSTAKAAN ===== ###
'''
Fitur Utama :
- Create = Membuat data peminjaman baru
- Read = Melihat data peminjaman saat ini
- Update = Mengubah data peminjaman
- Delete = Menghapus data peminjaman buku

Fitur Tambahan :
- Filtering = Mencari data berdasarkan nama peminjam, nama buku, atau status
- Error Handling = Memastikan tidak ada salah input data dari user
- Confirmation message = Konfirmasi setiap akan melakukan perubahan data
'''

### ======================================================================= ###
''' IMPORT MODULE '''
from tabulate import tabulate
import time
from datetime import datetime
now = datetime.now()

### ======================================================================= ###
''' PLACEHOLDER DATA '''
# Data pada program ini disimpan dalam bentuk List of Dictionary
data_peminjaman = [{'id': 1, 'nama_peminjam': 'Nabila', 'nama_buku': 'Python for Cryptography', 'tgl_pinjam': '2025-07-06', 'tgl_kembali': '2025-07-12', 'status': 'Terlambat'},
                    {'id': 2, 'nama_peminjam': 'John Doe', 'nama_buku': 'Intro to SQL', 'tgl_pinjam': '2025-07-08', 'tgl_kembali': '2025-07-14', 'status': 'Terlambat'},
                    {'id': 3, 'nama_peminjam': 'Rina', 'nama_buku': 'Python for Data', 'tgl_pinjam': '2025-07-09', 'tgl_kembali': '2025-07-13', 'status': 'Dikembalikan'},
                    {'id': 4, 'nama_peminjam': 'Rafi', 'nama_buku': 'Machine Learning Methods', 'tgl_pinjam': '2025-07-10', 'tgl_kembali': '2025-07-15', 'status': 'Dipinjam'},
                    {'id': 5, 'nama_peminjam': 'Putri', 'nama_buku': 'Architecture Enterprise', 'tgl_pinjam': '2025-07-11', 'tgl_kembali': '2025-07-17', 'status': 'Dipinjam'},
                    {'id': 6, 'nama_peminjam': 'Joseph', 'nama_buku': 'Cyber Security', 'tgl_pinjam': '2025-06-28', 'tgl_kembali': '2025-07-05', 'status': 'Dikembalikan'},
                    {'id': 7, 'nama_peminjam': 'Fajar', 'nama_buku': 'Algoritma & Struktur Data', 'tgl_pinjam': '2025-07-05', 'tgl_kembali': '2025-07-12', 'status': 'Dikembalikan'},
                    {'id': 8, 'nama_peminjam': 'Ilham', 'nama_buku': 'Visualisasi Data dengan Matplotlib', 'tgl_pinjam': '2025-07-03', 'tgl_kembali': '2025-07-10', 'status': 'Terlambat'},
                    {'id': 9, 'nama_peminjam': 'Evan Susanto', 'nama_buku': 'Deep Learning Fundamentals', 'tgl_pinjam': '2025-07-08', 'tgl_kembali': '2025-07-16', 'status': 'Dipinjam'},
                    {'id': 10, 'nama_peminjam': 'Bambang Susanto', 'nama_buku': 'Object Oriented Programming with Python', 'tgl_pinjam': '2025-07-11', 'tgl_kembali': '2025-07-18', 'status': 'Dipinjam'}]

### ======================================================================= ###

''' FUNGSI-FUNGSI PROGRAM '''

### MAIN MENU ###
def print_menu():
    print("""
=== MENU PERPUSTAKAAN ===
1. Lihat Data Peminjaman
2. Tambah Peminjaman Baru
3. Edit Data Peminjaman
4. Hapus Data Peminjaman
0. Keluar
""")

### SUB-MENU 1 (READ) ###
''' Fungsi untuk menampilkan sub-menu 1 '''
def menu_read():
    while True:
        print('''
Menu 1 : Lihat Data Peminjaman
1. Lihat data keseluruhan
2. Cari data berdasarkan nama/buku/status

0. Kembali ke menu utama
''')
        pil_menu = validasi_input("Pilih menu : ", 2)
        if pil_menu == 0:
            print("Kembali ke menu utama.\n")
            break
        elif pil_menu == 1:
            print_tabel(data_peminjaman)
        elif pil_menu == 2:
            menu_read_sub2()

''' Fungsi untuk menampilkan sub-menu 1-2 '''
def menu_read_sub2():
    while True:
        print('''
Menu 1-2 : Cari data berdasarkan parameter
1. Cari data berdasarkan nama
2. Cari data berdasarkan buku
3. Cari data berdasarkan status

0. Kembali ke sub-menu 1
''')
        pil_menu = validasi_input("Pilih menu : ", 3)
        if pil_menu == 0:
            print("Kembali ke menu sub-menu 1.\n")
            break
        elif pil_menu == 1:
            filter = input("Masukkan nama : ")
            if cari_data(data_peminjaman, filter, "nama_peminjam") == []:
                print("Nama yang anda cari tidak ada.\n")
            else:
                print_tabel(cari_data(data_peminjaman, filter, "nama_peminjam"))
        elif pil_menu == 2:
            filter = input("Masukkan nama buku : ")
            if cari_data(data_peminjaman, filter, "nama_buku") == []:
                print("Buku yang anda cari tidak ada.\n")
            else:
                print_tabel(cari_data(data_peminjaman, filter, "nama_buku"))
        elif pil_menu == 3:
            filter = input("Masukkan status (dikembalikan/dipinjam/terlambat) : ")
            if cari_data(data_peminjaman, filter, "status") == []:
                print("Peminjaman dengan status yang anda cari tidak ada.\n")
            else:
                print_tabel(cari_data(data_peminjaman, filter, "status"))

### SUB-MENU 2 (CREATE) ###
''' Fungsi Sub-Menu 2 : Menambah pinjaman baru '''
def tambah_pinjaman(tabel):
    print(f'''
Menu 2 : Menambahkan data peminjaman baru

Tanggal hari ini : {now.date()}

Masukkan data nama peminjam, buku yang dipinjam, 
dan tentukan tanggal pengembalian buku!
''')
    # Proses meng-input data
    nama_peminjam = input("Nama peminjam : ")
    nama_buku = input("Nama buku : ")
    tgl_kembali = validasi_tanggal("Masukkan tanggal pengembalian (YYYY-MM-DD): ")
    
    # Proses konfirmasi input data
    print(f'''
Konfirmasi data yang akan di-input
Nama Peminjam : {nama_peminjam}
Nama Buku : {nama_buku}
Tgl Pinjam : {now.date()}
Tgl Pengembalian : {tgl_kembali}

Apakah anda yakin akan menambah data di atas?
1. Ya, tambah data
0. Tidak, batal tambah data

''')
    confirm = validasi_input("Pilih menu : ", 1)
    if confirm == 1:
        tabel.append({"id":(len(tabel) + 1), "nama_peminjam":nama_peminjam, "nama_buku":nama_buku, "tgl_pinjam":now.date(), "tgl_kembali": tgl_kembali, "status":"Dipinjam"})
        print(f"Buku {nama_buku} berhasil dipinjam.")
    else:
        print("Penambahan data peminjaman dibatalkan.")

### SUB-MENU 3 (EDIT) ###
''' Menampilkan sub-menu 3 '''
def menu_update():
    while True:
        print('''
Menu 3 : Edit data peminjaman buku
1. Perpanjang masa pinjam
2. Kembalikan buku

0. Kembali ke menu utama
''')
        pil_menu = validasi_input("Pilih menu : ", 2)
        if pil_menu == 0:
            print("Kembali ke menu utama.\n")
            break
        elif pil_menu == 1:
            menu_edit1()
        elif pil_menu == 2:
            menu_edit2()

''' Fungsi pemrosesan menu 3-1 : Perpanjang masa pinjam '''
def menu_edit1():
    while True:
        print("Menu 3-1 : Perpanjang masa peminjaman\n")
        buku_dipinjam = cari_data(data_peminjaman, "dipinjam", "status")
        print_tabel(buku_dipinjam)
        list_id = [item["id"] for item in buku_dipinjam]
        print('''
\nPilih buku yang ingin anda perpanjang!

Masukkan 'id' buku sesuai dengan yang tertera pada tabel!
Ketik 0 untuk membatalkan proses perpanjangan.
''')
        while True:
            id_buku = input("Pilih 'id' buku : ")
            if id_buku.isdigit() and (int(id_buku) in list_id or int(id_buku) == 0):
                id_buku = int(id_buku)
                break
            else:
                print("Masukkan harus sesuai dengan 'id' pada tabel!")
            
        if id_buku == 0:
            print("Kembali ke menu sebelumnya.\n")
            break
        else:
            buku = data_peminjaman[id_buku-1]
            print(f'''
Perpanjangan Masa Peminjaman
Nama peminjam : {buku["nama_peminjam"]}
Nama buku : {buku["nama_buku"]}
Tgl Kembali : {buku["tgl_kembali"]}

Tanggal hari ini : {now.date()}
''')
            tgl_baru = validasi_tanggal("Masukkan tanggal pengembalian baru (YYYY-MM-DD): ")
            print('''
Apakah anda yakin akan memperpanjang masa pinjam buku ini?
1. Ya, perpanjang
0. Tidak, batal perpanjang
''')
            pil_menu = validasi_input("Pilih menu : ", 1)
            if pil_menu == 0:
                print("Proses perpanjang dibatalkan")
            else:
                data_peminjaman[id_buku-1]["tgl_kembali"] = tgl_baru
                print("Proses perpanjangan berhasil.")
            break

''' Fungsi pemrosesan menu 3-2 : Kembalikan buku '''
def menu_edit2():
    while True:
        print("Menu 3-2 : Proses pengembalian buku\n")
        # filter hanya buku yang belum kembali
        buku_sudah_kembali = cari_data(data_peminjaman, "dikembalikan", "status")
        buku_dipinjam = [item for item in data_peminjaman if item not in buku_sudah_kembali]
        list_id = [item["id"] for item in buku_dipinjam]
        if buku_dipinjam == []:
            print("Tidak ada buku yang bisa dikembalikan.\n")
            print("Kembali ke menu sebelumnya.")
            break
        print_tabel(buku_dipinjam)
        print('''
\nPilih buku yang ingin anda kembalikan!

Masukkan 'id' buku sesuai dengan yang tertera pada tabel!
Ketik 0 untuk membatalkan proses pengembalian.
''')
        while True:
            id_buku = input("Pilih 'id' buku : ")
            if id_buku.isdigit() and int(id_buku) in list_id:
                id_buku = int(id_buku)
                buku = data_peminjaman[id_buku-1]
                print(f'''
Pengembalian Buku

Nama peminjam : {buku["nama_peminjam"]}
Nama buku : {buku["nama_buku"]}
Batas Tgl Kembali : {buku["tgl_kembali"]}

Apakah anda yakin akan mengembalikan buku ini?
1. Ya, kembalikan
0. Tidak, batal kembalikan
''')
                pil_menu = validasi_input("Pilih menu : ", 1)
                if pil_menu == 1:
                    if data_peminjaman[id_buku-1]["status"].lower() == "terlambat":
                        print("Buku terlambat dikembalikan,\n")
                        print("menghitung denda peminjaman...\n")
                        time.sleep(2)
                        tgl_kembali = data_peminjaman[id_buku-1]["tgl_kembali"]
                        tgl_kembali = datetime.strptime(tgl_kembali, "%Y-%m-%d").date()
                        selisih_hari = (now.date() - tgl_kembali).days
                        print(f'''
Tanggal kembali : {tgl_kembali}
Tanggal hari ini : {now.date()}

Terlambat : {selisih_hari} hari
Denda Rp 3000 per-hari

Total denda : Rp {3000*selisih_hari}

Penghitungan denda selesai,
proses pengembalian dilanjutkan...\n
''')
                    time.sleep(2)
                    data_peminjaman[id_buku-1]["status"] = "Dikembalikan"
                    print("Proses pengembalian berhasil.")
                else:
                    print("Proses pengembalian dibatalkan.")
                break
            elif id_buku.isdigit() and int(id_buku) == 0:
                print("Batal kembalikan buku,")
                print("kembali ke menu sebelumnya.")
                break
            else:
                print("Masukkan harus sesuai dengan 'id' pada tabel!")
        
        break

### SUB-MENU 4 (DELETE) ###
''' Menampilkan sub-menu 4 '''
def menu_delete():
    while True:
        print('''
Menu 4 : Hapus data peminjaman buku
1. Hapus data peminjaman sesuai pilihan
2. Hapus semua data peminjaman yang sudah dikembalikan

0. Kembali ke menu utama
''')
        pil_menu = validasi_input("Pilih menu : ", 2)
        if pil_menu == 0:
            print("Kembali ke menu utama.\n")
            break
        elif pil_menu == 1:
            menu_delete1()
        elif pil_menu == 2:
            menu_delete2()

''' Fungsi pemrosesan menu 4-1 : Hapus 1 row data '''
def menu_delete1():
    global data_peminjaman
    print_tabel(data_peminjaman)
    print("Menu 4-1 : Hapus satu data berdasarkan 'id'\n")
    print("Untuk menghapus pilih nomor 'id' yang tertera pada tabel!")
    print("Ketik 0 untuk membatalkan proses delete.")
    id_del = validasi_input("Pilih nomor 'id' data yang ingin anda hapus : ", len(data_peminjaman))

    if id_del != 0:
        item_table = [item for item in data_peminjaman if item["id"] == id_del]
        print("===== Data yang akan di hapus =====")
        print(tabulate(item_table, headers="keys", tablefmt="fancy_grid"))
        print('''

Apakah anda yakin akan menghapus data di atas?
1. Ya, hapus data
0. Tidak, batal hapus data
''')
        confirm = validasi_input("Pilih menu : ", 1)
        if confirm == 1:
            del data_peminjaman[id_del-1]
            print("Data berhasil dihapus.")
        else:
            print("Hapus data peminjaman dibatalkan.")
    else:
        print("Hapus data peminjaman dibatalkan.")

''' Fungsi pemrosesan menu 4-2 : Hapus data buku yang sudah kembali '''
def menu_delete2():
    global data_peminjaman
    print("Menu 4-2 : Hapus data peminjaman yang sudah dikembalikan")
    print("===== Data Buku yang telah Dikembalikan =====")
    tabel_kembali = cari_data(data_peminjaman, "dikembalikan", "status")
    print(tabulate(tabel_kembali, headers="keys", tablefmt="fancy_grid"))

    print('''

Apakah anda yakin akan menghapus data di atas?
1. Ya, hapus data
0. Tidak, batal hapus data
''')
    confirm = validasi_input("Pilih menu : ", 1)
    if confirm == 1:
        for item in tabel_kembali:
            del data_peminjaman[data_peminjaman.index(item)]
        print("Data berhasil dihapus.")
    else:
        print("Hapus data peminjaman dibatalkan.")

### FUNGSI PEMROSESAN DATA ###
''' Fungsi untuk Error Handling Input '''
def validasi_input(msg, range):
    while True:
        value = input(msg)
        if value.isdigit() and int(value) <= range:
            value = int(value)
            break
        else:
            print(f"Masukkan harus di antara angka 0-{range}")
    return value

''' Fungsi untuk menampilkan tabel '''
def print_tabel(tabel):
    print("===== Daftar Peminjaman Buku =====\n")
    print(tabulate(tabel, headers="keys", tablefmt="fancy_grid"))

''' Fungsi untuk mengecek validasi input tanggal '''
def validasi_tanggal(msg):
    while True:
        user_input = input(msg)
        try:
            tanggal_input = datetime.strptime(user_input, "%Y-%m-%d").date()
            if tanggal_input > datetime.today().date():
                return tanggal_input
            else:
                print("Tanggal harus lebih dari hari ini.")
        except ValueError:
            print("Format salah! Contoh: 2025-07-11")

''' Fungsi Filtering Data dengan Parameter '''
def cari_data(tabel, filter, parameter):
    hasil_filter = []
    for item in tabel:
        if filter.lower() not in item[parameter].lower():
            continue
        hasil_filter.append(item)
    return hasil_filter

### ======================================================================= ###
''' ### --- MAIN PROGRAM --- ### '''

print("""
======== SELAMAT DATANG DI PERPUSTAKAAN PURWADHIKA ========""")

while True:
    print_menu()

    # Input pilihan menu
    menu = validasi_input("Pilih menu: ", 4)

    # Pemrosesan pilihan menu
    if menu == 0:
        print("Program dihentikan.\n")
        print("Terima kasih.")
        break
    elif menu == 1:
        menu_read()
    elif menu == 2:
        tambah_pinjaman(data_peminjaman)
    elif menu == 3:
        menu_update()
    elif menu == 4:
        menu_delete()
