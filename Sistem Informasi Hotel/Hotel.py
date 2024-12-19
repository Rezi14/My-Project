import pandas as pd
from tabulate import tabulate
from datetime import datetime
import os 
import sys

# header = ['Username', 'Password']
# data_admin = [['sava', '123'], ['cleon', '456'], ['rezi', '789']]
# admin = pd.DataFrame(data_admin, columns=header)
# admin.to_csv('akun admin.csv', index=False)

# header = ['Nama Hotel', 'Alamat Hotel', 'Kontak']
# data_hotel = [['Hotel LeXa','Jalan Jawa,Sumbersari,Sumbersari,Jember','12345678']]
# admin = pd.DataFrame(data_hotel, columns=header)
# admin.to_csv('data hotel.csv', index=False)

# header = ['Nama Fasilitas', 'Biaya Tambahan']
# data_fasilitas = [['WiFi', '50000'], ['Gym', '50000']]
# fasilitas = pd.DataFrame(data_fasilitas, columns=header)
# fasilitas.to_csv('data fasilitas.csv', index=False)

# header = ['Nama Tamu', 'Nomor Identitas', 'Nomor Kamar', 'Tipe Kamar', 'Fasilitas']
# data_pesanan = []
# pesanan = pd.DataFrame(data_pesanan, columns=header)
# pesanan.to_csv('data pesanan.csv', index=False)

# header = ['Nama Tamu', 'Nomor Identitas', 'Nomor Kamar', 'Ulasan']
# data_ulasan = []
# Ulasan = pd.DataFrame(data_ulasan, columns=header)
# Ulasan.to_csv('data ulasan.csv', index=False)

# header = ['Nomor Kamar', 'Tipe Kamar', 'Harga Kamar', 'Status']
# data_kamar_hotel = []
# hotel = pd.DataFrame(data_kamar_hotel, columns=header)
# hotel.to_csv('data kamar hotel.csv', index=False)

# header = ['Nama Tamu', 'Nomor Identitas', 'Nomor Kamar', 'Tipe Kamar', 'Fasilitas', 'Total Biaya', 'Metode Pembayaran','Tanggal Check-In','Tanggal Check-Out', 'Staf']
# data_transaksi = []
# transaksi = pd.DataFrame(data_transaksi, columns=header)
# transaksi.to_csv('data transaksi.csv', index=False)

#==================
#Untuk Clear Screen
#==================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#==============
#Tampilan Tabel 
#==============
def tampilan_tabel(df):
    """
    Menampilkan DataFrame dalam format tabel menggunakan tabulate dengan gaya heavy_grid.
    """
    # Konversi DataFrame ke list
    headers = df.columns.tolist()  # Nama kolom
    data = df.values.tolist()      # Data sebagai list of lists

    # Tampilkan tabel menggunakan tabulate
    print(tabulate(data, headers=headers, tablefmt="double_grid"))

#================================
#Tampilan Fitur Kelola Data Hotel 
#================================
def kelola_data_hotel():
    while True:
        print("DATA HOTEL")
        try:
            hotel = pd.read_csv('data hotel.csv')
            hotel.index += 1
            tampilan_tabel(hotel)
        except FileNotFoundError:
            print("File 'data hotel.csv' Tidak Ditemukan. Membuat File Baru")

        print("╔═════════════════════════════════════════╗")
        print("║            Kelola Data Hotel            ║")
        print("╠═════════════════════════════════════════╣")
        print("║ 1. Perbarui Kontak Hotel                ║")
        print("║ 2. Keluar                               ║")
        print("╚═════════════════════════════════════════╝")

        pilihan = input("Masukkan Pilihan (1-2): ")
        
        if pilihan == "1":
            clear_screen()
            perbarui_kontak_hotel()
        elif pilihan == "2":
            clear_screen()
            menu_utama()
        else:
            clear_screen()
            print("Input Tidak Valid Harap Masukkan Angka (1-2)'\n")

#==============================
#Fitur Memperbarui Kontak Hotel
#==============================
def perbarui_kontak_hotel():
    while True:
        print('DATA HOTEL')
        try:
            hotel = pd.read_csv('data hotel.csv')
            hotel.index += 1
            tampilan_tabel(hotel)
        except FileNotFoundError:
            print("File 'data hotel.csv' Tidak Ditemukan. Membuat File Baru\n")
            
        try:
            nomor = int(input("Masukkan Angka 1 Untuk Memperbarui: "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return

        if nomor in hotel.index:
            try:
                ubah_kontak = int(input("Kontak Mau Diperbarui Berapa? "))
                if (ubah_kontak == ("")):
                    clear_screen()
                    print("Input Harus Berupa Angka. Kembali\n")
                    return
                elif ubah_kontak <= 0:
                    clear_screen()
                    print("Input Tidak boleh 0 atau dibawah 0. Kembali\n")
                    return
                else:
                    hotel.loc[nomor, 'Kontak'] = ubah_kontak
                    hotel.to_csv('data hotel.csv', index=False)
                    clear_screen()
                    print("Kontak Berhasil Diperbarui\n")
            except ValueError:
                clear_screen()
                print("Input Harus Berupa Angka. Kembali\n")
                return
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan\n")
            
        while True:
                pilihan = input("Ingin Memperbarui Kontak Lagi? (Y/N): ").lower()
                if pilihan == ('Y').lower():
                    clear_screen()
                    print("Kontak Berhasil Diperbarui")
                    print("Tambah Kontak Baru Lagi\n")
                    break  
                elif pilihan == ('N').lower():
                    clear_screen()
                    print("Kontak Berhasil Ditambahkan")
                    print("Kembali Ke Menu Utama\n")
                    return  
                else:
                    print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#=====================================
#Tampilan Fitur Kelola Fasilitas Hotel 
#=====================================
def kelola_fasilitas():
    while True:
        print('DATA FASILITAS HOTEL')
        try:
            data_fasilitas = pd.read_csv('data fasilitas.csv')
            data_fasilitas.index += 1
            tampilan_tabel(data_fasilitas)    
        except FileNotFoundError:
            print("File 'data fasilitas.csv' Tidak Ditemukan. Membuat File Baru")

        print("╔═════════════════════════════════════════╗")
        print("║          Kelola Fasilitas Hotel         ║")
        print("╠═════════════════════════════════════════╣")
        print("║ 1. Tambah Fasilitas Hotel               ║")
        print("║ 2. Perbarui Biaya Fasilitas Hotel       ║")
        print("║ 3. Hapus Fasilitas Hotel                ║")
        print("║ 4. Keluar                               ║")
        print("╚═════════════════════════════════════════╝")

        
        pilihan = input("Masukkan Pilihan (1-4): ")

        if pilihan == "1":
            clear_screen()
            tambah_fasilitas()
        elif pilihan == "2":
            clear_screen()
            perbarui_fasilitas()
        elif pilihan == "3":
            clear_screen()
            hapus_fasilitas()
        elif pilihan == "4":
            clear_screen()
            menu_utama()
        else:
            clear_screen()
            print("Inputan Tidak Valid Harap Masukkan Angka (1-4)\n")

#=================================
#Fitur Menambahkan Fasilitas Hotel
#=================================
def tambah_fasilitas():
    while True:
        print('DATA FASILITAS HOTEL')
        try:
            data_fasilitas = pd.read_csv('data fasilitas.csv')
            data_fasilitas.index += 1
            tampilan_tabel(data_fasilitas)    
        except FileNotFoundError:
            print("File 'data fasilitas.csv' Tidak Ditemukan. Membuat File Baru\n")
        
        nama_fasilitas = input("Masukkan Nama Fasilitas Yang Ingin Ditambahkan: ")
        
        if (nama_fasilitas == ""):
            clear_screen()
            print("Nama Fasilitas Harus Berupa Huruf. Kembali\n")
            return
        elif not all(part.isalpha() for part in nama_fasilitas.split()):
            clear_screen()
            print("Nama Fasilitas Harus Berupa Huruf. Kembali\n")
            return
        else:
            try:
                biaya_tambahan = float(input("Masukkan Biaya Tambahan Fasilitas: "))
                if biaya_tambahan <= 0:
                    clear_screen()
                    print("Input Tidak boleh 0 atau dibawah 0. Kembali\n")
                    return
            except ValueError:
                clear_screen()
                print("Biaya Tambahan Harus Berupa Angka\n")
                return

            data_fasilitas = pd.DataFrame({
                'Nama fasilitas' : [nama_fasilitas],
                'Biaya tambahan' : [biaya_tambahan]})
            
        data_fasilitas.to_csv('data fasilitas.csv', mode="a", header=False, index=False)
        clear_screen()
        print("Fasilitas Berhasil Ditambahkan\n")

        while True:
                pilihan = input("Ingin Tambah Fasilitas Lagi? (Y/N): ").lower()
                if pilihan == ('Y').lower():
                    clear_screen()
                    print("Fasilitas Berhasil Ditambahkan")
                    print("Tambah Fasilitas Baru Lagi\n")
                    break  
                elif pilihan == ('N').lower():
                    clear_screen()
                    print("Fasilitas Berhasil Ditambahkan")
                    print("Kembali Ke Menu Utama\n")
                    return  
                else:
                    print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#================================================
#Fitur Memperbarui Biaya Tambahan Fasilitas Hotel
#================================================
def perbarui_fasilitas():
    while True:
        print('DATA FASILITAS HOTEL')
        try:
            data_fasilitas = pd.read_csv('data fasilitas.csv')
            data_fasilitas.index += 1
            tampilan_tabel(data_fasilitas)    
        except FileNotFoundError:
            print("File 'data fasilitas.csv' Tidak Ditemukan. Membuat File Baru\n")
    
        try:
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Diperbarui (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return

        if nomor in data_fasilitas.index:
            try:
                ubah_biaya = float(input("Biaya Tambahan Mau Diperbarui Apa? "))
                if (ubah_biaya == ("")):
                    clear_screen()
                    print("Input Harus Berupa Angka. Kembali\n")
                    return
                elif ubah_biaya <= 0:
                    clear_screen()
                    print("Input Tidak boleh 0 atau dibawah 0. Kembali\n")
                    return
                else:
                    data_fasilitas.loc[nomor, 'Biaya Tambahan'] = ubah_biaya
                    data_fasilitas.to_csv('data fasilitas.csv', index=False)
                    clear_screen()
                    print("Biaya Tambahan Berhasil Diperbarui\n")
            except ValueError:
                clear_screen()
                print("Input Harus Berupa Angka. Kembali\n")
                return
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan.\n")    

        while True:
            pilihan = input("Ingin Memperbarui Biaya Tambahan Lagi? (Y/N): ").lower()
            if pilihan == ('Y').lower():
                clear_screen()
                print("Biaya Tambahan Berhasil Diperbarui")
                print("Perbarui Biaya Tambahan Lagi\n")
                break  
            elif pilihan == ('N').lower():
                clear_screen()
                print("Biaya Tambahan Berhasil Diperbarui")
                print("Kembali Ke Menu Utama\n")
                return  
            else:
                print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#===============================
#Fitur Menghapus Fasilitas Hotel
#===============================
def hapus_fasilitas():
    while True:
        print('DATA FASILITAS HOTEL')
        try:
            data_fasilitas = pd.read_csv('data fasilitas.csv')
            data_fasilitas.index += 1
            tampilan_tabel(data_fasilitas)    
        except FileNotFoundError:
            print("File 'data fasilitas.csv' Tidak Ditemukan. Membuat File Baru\n")

        try:    
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Dihapus (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Input Harus Berupa Angka. Kembali\n")
            return
        
        if nomor in data_fasilitas.index:
            data_fasilitas = data_fasilitas.drop(nomor)
            data_fasilitas.to_csv('data fasilitas.csv', index=False)
            clear_screen()
            print("Fasilitas Berhasil Dihapus\n")
        else:
            clear_screen()
            print(f"Nama Fasilitas {nomor} Tidak Ditemukan Dalam Data.\n")
            

        while True:
            pilihan = input("Ingin Hapus Fasilitas Lagi? (Y/N): ").lower()
            if pilihan == ('Y').lower():
                clear_screen()
                print("Fasilitas Berhasil Dihapus")
                print("Hapus Fasilitas lagi\n")
                break  
            elif pilihan == ('N').lower():
                clear_screen()
                print("Fasilitas Berhasil Dihapus")
                print("Kembali Ke Menu Utama\n")
                return  
            else:
                print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#=====================================
#Tampilan Fitur Kelola Pemesanan Hotel 
#=====================================
def kelola_pesanan():
    while True:
        print('DATA PESANAN HOTEL')
        try:
            data_pesanan = pd.read_csv('data pesanan.csv')
            data_pesanan.index += 1
            tampilan_tabel(data_pesanan)    
        except FileNotFoundError:
            print("File 'data .csv' Tidak Ditemukan. Membuat File Baru")

        print("╔═════════════════════════════════════════╗")
        print("║             Kelola Pesanan              ║")
        print("╠═════════════════════════════════════════╣")
        print("║ 1. Check-In Tamu                        ║")
        print("║ 2. Check-Out Tamu                       ║")
        print("║ 3. Keluar                               ║")
        print("╚═════════════════════════════════════════╝")

        pilihan = input("Masukkan pilihan (1-3): ")
        
        if pilihan == "1":
            clear_screen()
            checkin()
        elif pilihan == "2":
            clear_screen()
            checkout()
        elif pilihan == "3":
            clear_screen()
            menu_utama()
        else:
            clear_screen()
            print("Inputan Tidak Valid Harap masukkan angka (1-3)\n")

#=========================
#Fitur Check-In Tamu Hotel
#=========================
def checkin():
    while True:
        print('DATA KAMAR HOTEL')
        try:
            kamar_hotel = pd.read_csv('data kamar hotel.csv')
            kamar_hotel.index += 1
            tampilan_tabel(kamar_hotel)    
        except FileNotFoundError:
            print("File 'data kamar hotel.csv' Tidak Ditemukan. Membuat File Baru\n")

        print('DATA FASILITAS HOTEL')
        try:
            data_fasilitas = pd.read_csv('data fasilitas.csv')
            data_fasilitas.index += 1
            tampilan_tabel(data_fasilitas)    
        except FileNotFoundError:
            print("File 'data fasilitas.csv' Tidak Ditemukan. Membuat File Baru\n")
    
        print('DATA PESANAN HOTEL')
        try:
            data_pesanan = pd.read_csv('data pesanan.csv')
            data_pesanan.index += 1
            tampilan_tabel(data_pesanan)    
        except FileNotFoundError:
            print("File 'data pesanan.csv' tidak ditemukan. Membuat File Baru\n")
    
        nama = input("Masukkan Nama Tamu: ")
        if nama == (""):
            clear_screen()
            print("Nama Tamu Harus Berupa Huruf. Kembali\n")
            return
        elif not all(part.isalpha() for part in nama.split()):
            clear_screen()
            print("Nama Tamu Harus Berupa Huruf. Kembali\n")
            return
        try:
            no_identitas = int(input("Masukkan Nomor Identitas Tamu: "))
            if no_identitas <= 0:
                clear_screen()
                print("Input Tidak boleh 0 atau dibawah 0. Kembali\n")
                return
        except ValueError:
            clear_screen()
            print("Nomor Identitas Harus Berupa Angka. Kembali\n")
            return
        try:
            no_kamar = int(input("Masukkan Nomor Kamar: "))
            if no_kamar in data_pesanan["Nomor Kamar"].values:
                clear_screen()
                print("Nomor Kamar Sudah Dipesan. Cari Kamar Lain\n")
                return
            elif no_kamar > len(kamar_hotel):
                clear_screen()
                print("Nomor Kamar Tidak Ada")
                return
            elif no_kamar <= 0:
                clear_screen()
                print("Input Tidak boleh 0 atau dibawah 0. Kembali\n")
                return
        except ValueError:
            clear_screen()
            print("Nomor Kamar Harus Berupa Angka. Kembali\n")
            return
        tipe_kamar = input("Masukkan Tipe Kamar Tamu (1 Untuk Single, 2 Untuk Double, 3 Untuk Premium): ")
        fasilitas = input("Masukkan Nomor Fasilitas Tambahan Sesuai Baris: ")
        print("Enter untuk langsung mengisi hari ini")
        tanggal_checkin = input("Tanggal Check-In (DD-MM-YYYY): ").strip()
        # Memeriksa format tanggal
        try:
            if tanggal_checkin == '':
                tanggal_checkin = datetime.now().date()
            else:
                datetime.strptime(tanggal_checkin, '%d-%m-%Y')
        except Exception:
            clear_screen()
            print('Tanggal tidak valid!')
            return
        
        staf_login = input("Masukkan Nama Staf Login: ")
        if not staf_login.isalpha():
            clear_screen()
            print("Nama Staf Harus Berupa Huruf. Kembali\n")
            return
        # Hitung total biaya kamar
        if tipe_kamar == "1":
            tipe_kamar_value = "Single"
            harga_per_malam = kamar_hotel.iloc[0, 2]  # Ambil harga dari index 0
        elif tipe_kamar == "2":
            tipe_kamar_value = "Double"
            harga_per_malam = kamar_hotel.iloc[4, 2]  # Ambil harga dari index 4
        elif tipe_kamar == "3":
            tipe_kamar_value = "Premium"
            harga_per_malam = kamar_hotel.iloc[8, 2]  # Ambil harga dari index 8
        else:
            clear_screen()
            print("Tipe kamar tidak valid. Harap masukkan tipe kamar yang benar.\n")
            return

        total_biaya_kamar = harga_per_malam

        # Hitung biaya fasilitas
        biaya_fasilitas = 0
        fasilitas_list = fasilitas.split(",")  # Untuk mendukung beberapa fasilitas
        fasilitas_terpilih = []
        
        for item in fasilitas_list:
            try:
                biaya_fasilitas += data_fasilitas.iloc[int(item) - 1, 1]
                fasilitas_terpilih.append(data_fasilitas.iloc[int(item) - 1, 0])
            except Exception:
                clear_screen()
                print(f"Fasilitas '{item}' Tidak Valid. Harap Masukkan Fasilitas Yang Benar.\n")
                return

        total_biaya = total_biaya_kamar + biaya_fasilitas
        print(f"Total Biaya Yang Harus Dibayar: Rp {total_biaya}")
        
        # Proses pembayaran
        metode_pembayaran = input("Pilih Metode Pembayaran (Cash/Qris): ").lower()
        
        if metode_pembayaran in ['cash', 'qris']:
            print("Pembayaran Berhasil Diproses!\n")

            # Simpan data transaksi ke dalam data transaksi.csv
            data_transaksi = pd.DataFrame({
                'Nama Tamu': [nama],
                'Nomor Identitas': [no_identitas],
                'Nomor Kamar': [no_kamar],
                'Tipe Kamar': [tipe_kamar_value],
                'Fasilitas': [", ".join(fasilitas_terpilih)],  # Gabung fasilitas dengan koma
                'Total Biaya': [total_biaya],
                'Metode Pembayaran': [metode_pembayaran],
                'Tanggal Check-In' : [tanggal_checkin],
                'Tanggal Check-Out' : '',
                'Staf' : [staf_login]})

            # Append data transaksi ke file CSV
            data_transaksi.to_csv('data transaksi.csv', mode='a', header=False, index=False)

            # Simpan data pesanan ke dalam data pesanan.csv
            data_pesanan = pd.DataFrame({
                'Nama': [nama],
                'Nomor Identitas': [no_identitas],
                'Nomor Kamar': [no_kamar],
                'Tipe Kamar': [tipe_kamar_value],
                'Fasilitas': [", ".join(fasilitas_terpilih)]})
                    
            data_pesanan.to_csv('data pesanan.csv', mode='a', header=False, index=False)
            clear_screen()
            print("Tamu Berhasil Ditambahkan.\n")
        else:
            clear_screen()
            print("Metode Pembayaran Tidak Valid. Silakan Coba Lagi.\n")
            continue

        while True:
            pilihan = input("Ingin Tambah Pesanan Tamu Lagi? (Y/N): ").lower()
            if pilihan == ('Y').lower():
                clear_screen()
                print("Pesanan Tamu Berhasil Ditambahkan")
                print("Tambah Pesanan Tamu Lagi\n")
                break  
            elif pilihan == ('N').lower():
                clear_screen()
                print("Pesanan Tamu Berhasil Ditambahkan")
                print("Kembali ke menu utama\n")
                return  
            else:
                print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#==========================
#Fitur Check-Out Tamu Hotel
#==========================
def checkout():
    while True:
        print('DATA PESANAN HOTEL')
        try:
            data_transaksi = pd.read_csv("data transaksi.csv")
            data_pesanan = pd.read_csv('data pesanan.csv')
            data_pesanan.index += 1
            tampilan_tabel(data_pesanan)    
        except FileNotFoundError:
            print("File 'data pesanan.csv' Tidak Ditemukan. Membuat File Baru\n")
        
        print("Enter Untuk Mengisi Tanggal Hari Ini")
        tanggal_checkout = input("Tanggal Check-Out (DD-MM-YYYY): ").strip()
        # Memeriksa format tanggal
        try:
            if tanggal_checkout == '':
                tanggal_checkout = datetime.now().date()
            else:
                datetime.strptime(tanggal_checkout, '%d-%m-%Y')
        except Exception:
            clear_screen()
            print('Tanggal tidak valid!')
            return
        try:    
            nomor = int(input("Masukkan Nomor Baris Yang Check-Out (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Input Harus Berupa Angka. Kembali\n")
            return
        
        if nomor in data_pesanan.index:
            try:
                transaksi_index = data_transaksi[(data_transaksi['Nomor Kamar'] == data_pesanan.loc[nomor, "Nomor Kamar"]) 
                                                 & (data_transaksi['Tanggal Check-Out'].isna())].index
                if not transaksi_index.empty:
                    data_transaksi.loc[transaksi_index, 'Tanggal Check-Out'] = tanggal_checkout
                data_transaksi.to_csv('data transaksi.csv',index=False)
            except Exception as e:
                print(e)
                return
            data_pesanan = data_pesanan.drop(nomor)
            data_pesanan.to_csv('data pesanan.csv', index=False)
            clear_screen()
            print("Tamu Berhasil Check-Out\n")
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan Dalam Data.\n")
            return
        
        while True:
            pilihan = input("Ingin Check-Out Tamu Lagi? (Y/N): ").lower()
            if pilihan == ('Y').lower():
                clear_screen()
                print("Tamu Berhasil Check-Out")
                print("Check-Out Tamu Lagi\n")
                break  
            elif pilihan == ('N').lower():
                clear_screen()
                print("Tamu Berhasil Check-Out")
                print("Kembali Ke Menu Utama\n")
                return  
            else:
                print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#=================================
#Tampilan Fitur Kelola Kamar Hotel 
#=================================
def kelola_kamar_hotel():
   while True:
        print("DATA KAMAR HOTEL")
        try:
            kamar_hotel = pd.read_csv('data kamar hotel.csv')
            kamar_hotel.index += 1
            tampilan_tabel(kamar_hotel)
    
        except FileNotFoundError:
            print("File 'data kamar hotel.csv' Tidak Ditemukan. Membuat File Baru")

        print("╔═════════════════════════════════════════╗")
        print("║           Kelola Kamar Hotel            ║")
        print("╠═════════════════════════════════════════╣")
        print("║ 1. Tambah Kamar Hotel                   ║")
        print("║ 2. Perbarui Tipe Kamar Hotel            ║")
        print("║ 3. Perbarui Harga Kamar Hotel           ║")
        print("║ 4. Perbarui Status Kamar                ║")
        print("║ 5. Hapus Kamar Hotel                    ║")
        print("║ 6. Keluar                               ║")
        print("╚═════════════════════════════════════════╝")


        pilihan = input("Masukkan Pilihan (1-6): ")

        if pilihan == "1":
            clear_screen()
            tambah_kamar_hotel()
        elif pilihan == "2":
            clear_screen()
            perbarui_tipe_kamar()
        elif pilihan == "3":
            clear_screen()
            perbarui_harga_kamar()
        elif pilihan == "4":
            clear_screen()
            perbarui_status_kamar()
        elif pilihan == "5":
            clear_screen()
            hapus_kamar()
        elif pilihan == "6":
            clear_screen()
            menu_utama()
        else:
            clear_screen()
            print("Inputan Tidak Valid Harap Masukkan Angka (1-6)\n")

#=============================
#Fitur Menambahkan Kamar Hotel
#=============================
def tambah_kamar_hotel():
    while True:
        print('DATA KAMAR HOTEL')
        try:
            kamar_hotel = pd.read_csv('data kamar hotel.csv')
            kamar_hotel.index += 1
            tampilan_tabel(kamar_hotel)
        except FileNotFoundError:
            print("File 'data kamar hotel.csv' Tidak Ditemukan. Membuat File Baru\n")
        
        try:
            nomor_kamar = int(input("Masukkan Nomor Kamar: "))
            if (nomor_kamar == ("")):
                clear_screen()
                print("Nomor Kamar Harus Berupa Angka. Kembali\n")
                return
            elif nomor_kamar <= 0:
                clear_screen()
                print("Input Tidak boleh 0 atau dibawah 0. Kembali\n")
                return
            else:
                tipe_kamar = input("Masukkan Tipe Kamar: ")
                if not tipe_kamar.isalpha():
                    clear_screen()
                    print("Tipe Kamar Harus Berupa Huruf. Kembali\n")
                    return
                try:
                    harga_kamar = float(input("Masukkan Harga Kamar: "))
                    if harga_kamar <= 0:
                        clear_screen()
                        print("Input Tidak boleh 0 atau dibawah 0. Kembali\n")
                        return
                except ValueError:
                    print("Harga Kamar Harus Berupa Angka. Kembali\n")
                    return
        except ValueError:
            clear_screen()
            print("Nomor Kamar Harus Berupa Angka. Kembali\n")
            return

        kamar_hotel = pd.DataFrame({
            'Nomor Kamar' : [nomor_kamar],
            'Tipe Kamar' : [tipe_kamar],
            'Harga Kamar' : [harga_kamar],
            'Status' : ["Tersedia"]})

            
        kamar_hotel.to_csv('data kamar hotel.csv', mode="a", header=False, index=False)
        clear_screen()
        print("Kamar Berhasil Ditambahkan\n")

        while True:
                pilihan = input("Ingin Tambah Kamar Lagi? (Y/N): ").lower()
                if pilihan == ('Y').lower():
                    clear_screen()
                    print("Kamar Berhasil Ditambahkan")
                    print("Tambah Kamar Baru\n")
                    break  
                elif pilihan == ('N').lower():
                    clear_screen()
                    print("Kamar Berhasil Ditambahkan")
                    print("Kembali Ke Menu Utama\n")
                    return  
                else:
                    print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#==================================
#Fitur Memperbarui Tipe Kamar Hotel
#==================================
def perbarui_tipe_kamar():
    while True:
        print('DATA KAMAR HOTEL')
        try:
            kamar_hotel = pd.read_csv('data kamar hotel.csv')
            kamar_hotel.index += 1
            tampilan_tabel(kamar_hotel)    
        except FileNotFoundError:
            print("File 'data kamar hotel.csv' Tidak Ditemukan. Membuat File Baru\n")

        try:
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Diperbarui (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return

        if nomor in kamar_hotel.index:
            ubah_tipe = input("TIpe Kamar Mau Diperbarui Apa? ")
            if (ubah_tipe == ""):
                clear_screen()
                print("Tipe Kamar Harus Berupa Huruf. Kembali\n")
                return
            elif not ubah_tipe.isalpha():
                clear_screen()
                print("Tipe Kamar Harus Berupa Huruf. Kembali\n")
                return
            else:
                kamar_hotel.loc[nomor, 'Tipe Kamar'] = ubah_tipe
                kamar_hotel.to_csv('data kamar hotel.csv', index=False)
                clear_screen()
                print("Tipe Kamar Berhasil Diperbarui\n")
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan\n")
                
        while True:
            pilihan = input("Ingin Memperbarui Tipe Kamar Lagi? (Y/N): ").lower()
            if pilihan == ('Y').lower():
                clear_screen()
                print("Tipe Kamar Berhasil Diperbarui")
                print("Perbarui Tipe Kamar Lagi\n")
                break  
            elif pilihan == ('N').lower():
                clear_screen()
                print("Tipe Kamar Berhasil Diperbarui")
                print("Kembali Ke Menu Utama\n")
                return  
            else:
                print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#===================================
#Fitur Memperbarui Harga Kamar Hotel
#===================================
def perbarui_harga_kamar():
    while True:
        print('DATA KAMAR HOTEL')
        try:
            kamar_hotel = pd.read_csv('data kamar hotel.csv')
            kamar_hotel.index += 1
            tampilan_tabel(kamar_hotel)    
        except FileNotFoundError:
            print("File 'data kamar hotel.csv' Tidak Ditemukan. Membuat File Baru\n") 

        try:
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Diperbarui (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return

        if nomor in kamar_hotel.index:
            try:
                ubah_harga = float(input("Harga Kamar Mau Diperbarui Berapa? "))
                if (ubah_harga == ("")):
                    clear_screen()
                    print("Input Harus Berupa Angka. Kembali\n")
                    return
                elif ubah_harga <= 0:
                    clear_screen()
                    print("Input Tidak boleh 0 atau dibawah 0. Kembali\n")
                    return
                else:
                    kamar_hotel.loc[nomor, 'Harga Kamar'] = ubah_harga
                    kamar_hotel.to_csv('data kamar hotel.csv', index=False)
                    clear_screen()
                    print("Harga Kamar Berhasil Diperbarui\n")
            except ValueError:
                clear_screen()
                print("Input Harus Berupa Angka. Kembali\n")
                return
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan\n")
                
        while True:
            pilihan = input("Ingin Memperbarui Harga Kamar Lagi? (Y/N): ").lower()
            if pilihan == ('Y').lower():
                clear_screen()
                print("Harga Kamar Berhasil Diperbarui")
                print("Perbarui Harga Kamar Lagi\n")
                break  
            elif pilihan == ('N').lower():
                clear_screen()
                print("Harga Kamar Berhasil Diperbarui")
                print("Kembali Ke Menu Utama\n")
                return  
            else:
                print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#====================================
#Fitur Memperbarui Status Kamar Hotel
#====================================
def perbarui_status_kamar():
    while True:
        print('DATA KAMAR HOTEL')
        try:
            kamar_hotel = pd.read_csv('data kamar hotel.csv')
            kamar_hotel.index += 1
            tampilan_tabel(kamar_hotel)    
        except FileNotFoundError:
            print("File 'data kamar hotel.csv' Tidak Ditemukan. Membuat File Baru\n") 

        try:
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Diperbarui (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return

        if nomor in kamar_hotel.index:
            ubah_status = input("Status Kamar Mau Diperbarui Apa? ")
            if (ubah_status == ""):
                clear_screen()
                print("Status Kamar Harus Berupa Huruf. Kembali\n")
                return
            elif not ubah_status.isalpha():
                clear_screen()
                print("Status Kamar Harus Berupa Huruf. Kembali\n")
                return
            else:
                kamar_hotel.loc[nomor, 'Status'] = ubah_status
                kamar_hotel.to_csv('data kamar hotel.csv', index=False)
                clear_screen()
                print("Status Kamar Berhasil Diperbarui\n")
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan\n")
                
        while True:
            pilihan = input("Ingin Memperbarui Status Kamar Lagi? (Y/N): ").lower()
            if pilihan == ('Y').lower():
                clear_screen()
                print("Status Kamar Berhasil Diperbarui")
                print("Perbarui Status Kamar Lagi\n")
                break  
            elif pilihan == ('N').lower():
                clear_screen()
                print("Status Kamar Berhasil Diperbarui")
                print("Kembali Ke Menu Utama\n")
                return  
            else:
                print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#===========================
#Fitur Menghapus Kamar Hotel
#===========================
def hapus_kamar():
    while True:
        print('DATA KAMAR HOTEL')
        try:
            kamar_hotel = pd.read_csv('data kamar hotel.csv')
            kamar_hotel.index += 1
            tampilan_tabel(kamar_hotel)    
        except FileNotFoundError:
            print("File 'data kamar hotel.csv' Tidak Ditemukan. Membuat File Baru\n")

        try:    
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Dihapus (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return
        
        try:
            pesanan = pd.read_csv("data pesanan.csv")
            hapus_kamar = kamar_hotel.loc[nomor, 'Nomor Kamar']
            
            if not pesanan[pesanan['Nomor Kamar'] == hapus_kamar].empty:
                print("Kamar Tidak Dapat Dihapus")
                return
        except (FileNotFoundError, pd.errors.EmptyDataError):
            print("File Tidak Ditemukan. Membuat File")

        if nomor in kamar_hotel.index:
            kamar_hotel = kamar_hotel.drop(nomor)
            kamar_hotel.to_csv('data kamar hotel.csv', index=False)
            clear_screen()
            print("Kamar Hotel Berhasil Dihapus\n")
        else:
            clear_screen()
            print(f"Nomor {nomor} Tidak Ditemukan Dalam Data.\n")
            return

        while True:
            pilihan = input("Ingin Hapus Kamar Lagi? (Y/N): ").lower()
            if pilihan == ('Y').lower():
                clear_screen()
                print("Kamar Berhasil Dihapus")
                print("Hapus Kamar lagi\n")
                break  
            elif pilihan == ('N').lower():
                clear_screen()
                print("Kamar Berhasil Dihapus")
                print("Kembali Ke Menu Utama\n")
                return  
            else:
                print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#=======================================
#Tampilan Fitur Kelola Data Ulasan Hotel 
#=======================================
def kelola_data_ulasan():
    while True:
        print('DATA ULASAN HOTEL')
        try:
            data_ulasan = pd.read_csv('data ulasan.csv')
            data_ulasan.index += 1
            tampilan_tabel(data_ulasan)    
        except FileNotFoundError:
            print("File 'data ulasan.csv' Tidak Ditemukan. Membuat File Baru")

        print("╔═════════════════════════════════════════╗")
        print("║            Kelola Ulasan Tamu           ║")
        print("╠═════════════════════════════════════════╣")
        print("║ 1. Tambah Ulasan Tamu                   ║")
        print("║ 2. Perbarui Nama Tamu                   ║")
        print("║ 3. Perbarui Nomor Identitas             ║")
        print("║ 4. Perbarui Nomor Kamar                 ║")
        print("║ 5. Perbarui Ulasan Tamu                 ║")
        print("║ 6. Hapus Ulasan Tamu                    ║")
        print("║ 7. Keluar                               ║")
        print("╚═════════════════════════════════════════╝")

            
        pilihan = input("Masukkan pilihan (1-7): ")

        if pilihan == "1":
            clear_screen()
            tambah_ulasan()
        elif pilihan == "2":
            clear_screen()
            perbarui_nama_tamu_ulasan()
        elif pilihan == "3":
            clear_screen()
            perbarui_nomor_identitas_ulasan()
        elif pilihan == "4":
            clear_screen()
            perbarui_nomor_kamar_ulasan()
        elif pilihan == "5":
            clear_screen()
            perbarui_ulasan()
        elif pilihan == "6":
            clear_screen()
            hapus_ulasan()
        elif pilihan == "7":
            clear_screen()
            menu_utama()
        else:
            clear_screen()
            print("Inputan Tidak Valid Harap masukkan angka (1-7)\n")

#=============================
#Fitur Menambahkan Ulasan Tamu
#=============================
def tambah_ulasan():
    while True:
        print('DATA TRANSAKSI HOTEL')
        try:
            data_fasilitas = pd.read_csv('data transaksi.csv')
            data_fasilitas.index += 1
            tampilan_tabel(data_fasilitas)    
        except FileNotFoundError:
            print("File 'data transaksi.csv' Tidak Ditemukan. Membuat File Baru\n")

        print('DATA PESANAN HOTEL')
        try:
            data_pesanan = pd.read_csv('data pesanan.csv')
            data_pesanan.index += 1
            tampilan_tabel(data_pesanan)    
        except FileNotFoundError:
            print("File 'data pesanan.csv' tidak ditemukan. Membuat File Baru\n")

        print('DATA ULASAN HOTEL')
        try:
            data_ulasan = pd.read_csv('data ulasan.csv')
            data_ulasan.index += 1
            tampilan_tabel(data_ulasan)    
        except FileNotFoundError:
            print("File 'data ulasan.csv' Tidak Ditemukan. Membuat File Baru\n")
        try:
            kamar_hotel = pd.read_csv("data kamar hotel.csv")
        except FileNotFoundError:
            print("File 'data kamar hotel.csv Tidak Ditemukan. Membuat File Baru")

        nama = input("Masukkan Nama Tamu: ")
        if nama == (""):
            clear_screen()
            print("Nama Tamu Harus Berupa Huruf. Kembali\n")
            return
        elif not all(part.isalpha() for part in nama.split()):
            clear_screen()
            print("Nama Tamu Harus Berupa Huruf. Kembali\n")
            return
        try:
            no_identitas = int(input("Masukkan Nomor Identitas Tamu: "))
            if no_identitas <= 0:
                clear_screen()
                print("Input Tidak boleh 0 atau dibawah 0. Kembali\n")
                return
        except ValueError:
            clear_screen()
            print("Nomor Identitas Harus Berupa Angka. Kembali\n")
            return
        try:
            no_kamar = int(input("Masukkan Nomor Kamar: "))
            if no_kamar > len(kamar_hotel):
                clear_screen()
                print("Nomor Kamar Tidak Ada")
                return
            elif no_kamar <= 0:
                clear_screen()
                print("Input Tidak boleh 0 atau dibawah 0. Kembali\n")
                return
        except ValueError:
            clear_screen()
            print("Nomor Kamar Harus Berupa Angka. Kembali\n")
            return
        
        ulasan = input("Masukkan Ulasan Tamu: ")
        if ulasan == "":
            ulasan = "-"
        elif not all(part.isalpha() for part in ulasan.split()):
            clear_screen()
            print("Ulasan Harus Berupa Huruf. Kembali\n")
            return

        ulasan_tamu = pd.DataFrame({
        'Nama Tamu' : [nama],
        'Nomor Identitas' : [no_identitas],
        "Nomor Kamar": [no_kamar],
        "Ulasan" : [ulasan]})

        ulasan_tamu.to_csv('data ulasan.csv', mode='a',header=False,index=False)
        clear_screen()
        print("Ulasan Tamu Berhasil Ditambahkan\n")

        while True:
                pilihan = input("Ingin Tambah Ulasan Tamu Lagi? (Y/N): ").lower()
                if pilihan == ('Y').lower():
                    clear_screen()
                    print("Ulasan Berhasil Ditambahkan")
                    print("Ulasan Tamu Baru\n")
                    break  
                elif pilihan == ('N').lower():
                    clear_screen()
                    print("Ulasan Tamu Berhasil Ditambahkan")
                    print("Kembali Ke Menu Utama\n")
                    return  
                else:
                    print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")        

#==================================================
#Fitur Memperbarui Nama Tamu Yang Memberikan Ulasan
#==================================================
def perbarui_nama_tamu_ulasan():
    while True:
        print('DATA ULASAN HOTEL')
        try:
            data_ulasan = pd.read_csv('data ulasan.csv')
            data_ulasan.index += 1
            tampilan_tabel(data_ulasan)    
        except FileNotFoundError:
            print("File 'data ulasan.csv' Tidak Ditemukan. Membuat File Baru\n")

        try:
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Diperbarui (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return

        if nomor in data_ulasan.index:
            ubah_nama = input("Nama Tamu Mau Diperbarui Apa? ")
            if (ubah_nama == ""):
                clear_screen()
                print("Nama Tamu Harus Berupa Huruf. Kembali\n")
                return
            elif not ubah_nama.isalpha():
                clear_screen()
                print("Nama Tamu Harus Berupa Huruf. Kembali\n")
                return
            else:
                data_ulasan.loc[nomor, 'Nama Tamu'] = ubah_nama
                data_ulasan.to_csv('data ulasan.csv', index=False)
                clear_screen()
                print("Nama Tamu Berhasil Diperbarui\n")
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan\n")

        while True:
                pilihan = input("Ingin Memperbarui Nama Tamu Lagi? (Y/N): ").lower()
                if pilihan == ('Y').lower():
                    clear_screen()
                    print("Nama Tamu Berhasil Diperbarui")
                    print("Perbarui Nama Tamu Lagi\n")
                    break  
                elif pilihan == ('N').lower():
                    clear_screen()
                    print("Nama Tamu Berhasil Diperbarui")
                    print("Kembali Ke Menu Utama\n")
                    return  
                else:
                    print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#=============================================================
#Fitur Memperbarui Nomor Identitas Tamu Yang Memberikan Ulasan
#=============================================================
def perbarui_nomor_identitas_ulasan():
    while True:
        print('DATA ULASAN HOTEL')
        try:
            data_ulasan = pd.read_csv('data ulasan.csv')
            data_ulasan.index += 1
            tampilan_tabel(data_ulasan)    
        except FileNotFoundError:
            print("File 'data ulasan.csv' Tidak Ditemukan. Membuat File Baru\n")

        try:
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Diperbarui (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return

        if nomor in data_ulasan.index:
            try:
                ubah_no_identitas = int(input("Nomor Identitas Mau Diperbarui Berapa? "))
                if (ubah_no_identitas == ("")):
                    clear_screen()
                    print("Input Harus Berupa Angka. Kembali\n")
                    return
                elif ubah_no_identitas <= 0:
                    clear_screen()
                    print("Input Tidak boleh 0 atau dibawah 0. Kembali\n")
                    return
                else:
                    data_ulasan.loc[nomor, 'Nomor Identitas'] = ubah_no_identitas
                    data_ulasan.to_csv('data ulasan.csv', index=False)
                    clear_screen()
                    print("Nomor Identitas Berhasil Diperbarui\n")
            except ValueError:
                clear_screen()
                print("Input Harus Berupa Angka. Kembali\n")
                return
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan\n")

        while True:
                pilihan = input("Ingin Memperbarui Nomor Identitas Lagi? (Y/N): ").lower()
                if pilihan == ('Y').lower():
                    clear_screen()
                    print("Nomor Identitas Berhasil Diperbarui")
                    print("Nomor Identitas Baru Lagi\n")
                    break  
                elif pilihan == ('N').lower():
                    clear_screen()
                    print("Nomor Identitas Berhasil Diperbarui")
                    print("Kembali Ke Menu Utama\n")
                    return  
                else:
                    print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#=========================================================
#Fitur Memperbarui Nomor Kamar Tamu Yang Memberikan Ulasan
#=========================================================
def perbarui_nomor_kamar_ulasan():
    while True:
        print('DATA ULASAN HOTEL')
        try:
            data_ulasan = pd.read_csv('data ulasan.csv')
            data_ulasan.index += 1
            tampilan_tabel(data_ulasan)    
        except FileNotFoundError:
            print("File 'data ulasan.csv' Tidak Ditemukan. Membuat File Baru\n")

        try:
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Diperbarui (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return

        if nomor in data_ulasan.index:
            try:
                ubah_no_kamar = int(input("Nomor Kamar Mau Diperbarui Berapa? "))
                if (ubah_no_kamar == ("")):
                    clear_screen()
                    print("Input Harus Berupa Angka. Kembali\n")
                    return
                elif ubah_no_kamar <= 0:
                    clear_screen()
                    print("Input Tidak boleh 0 atau dibawah 0. Kembali\n")
                    return
                else:
                    data_ulasan.loc[nomor, 'Nomor Kamar'] = ubah_no_kamar
                    data_ulasan.to_csv('data ulasan.csv', index=False)
                    clear_screen()
                    print("Nomor Kamar Berhasil Diperbarui\n")
            except ValueError:
                clear_screen()
                print("Nomor Baris Harus Berupa Angka. Kembali\n")
                return
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan\n")

        while True:
                pilihan = input("Ingin Memperbarui Nomor Kamar Lagi? (Y/N): ").lower()
                if pilihan == ('Y').lower():
                    clear_screen()
                    print("Nomor Kamar Berhasil Diperbarui")
                    print("Nomor Kamar Baru Lagi\n")
                    break  
                elif pilihan == ('N').lower():
                    clear_screen()
                    print("Nomor Kamar Berhasil Diperbarui")
                    print("Kembali Ke Menu Utama\n")
                    return  
                else:
                    print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#=============================
#Fitur Memperbarui Ulasan Tamu 
#=============================
def perbarui_ulasan():
    while True:
        print('DATA ULASAN HOTEL')
        try:
            data_ulasan = pd.read_csv('data ulasan.csv')
            data_ulasan.index += 1
            tampilan_tabel(data_ulasan)    
        except FileNotFoundError:
            print("File 'data ulasan.csv' Tidak Ditemukan. Membuat file baru\n")

        try:
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Diperbarui (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return

        if nomor in data_ulasan.index:
            ubah_ulasan = input("Ulasan Tamu Mau Diperbarui Apa? ")
            if ubah_ulasan == "":
                ubah_ulasan = "-"
                data_ulasan.loc[nomor, 'Ulasan'] = ubah_ulasan
                data_ulasan.to_csv('data ulasan.csv', index=False)
                clear_screen()
                print("Ulasan Tamu Berhasil Diperbarui\n")
            elif not all(part.isalpha() for part in ubah_ulasan.split()):
                clear_screen()
                print("Ulasan Harus Berupa Huruf. Kembali\n")
                return
            else:
                data_ulasan.loc[nomor, 'Ulasan'] = ubah_ulasan
                data_ulasan.to_csv('data ulasan.csv', index=False)
                clear_screen()
                print("Ulasan Tamu Berhasil Diperbarui\n")
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan")

        while True:
                pilihan = input("Ingin Memperbarui Ulasan Tamu Lagi? (Y/N): ").lower()
                if pilihan == ('Y').lower():
                    clear_screen()
                    print("Ulasan Tamu Berhasil Diperbarui")
                    print("Ulasan Tamu Baru\n")
                    break  
                elif pilihan == ('N').lower():
                    clear_screen()
                    print("Ulasan Tamu Berhasil Diperbarui")
                    print("Kembali Ke Menu Utama\n")
                    return  
                else:
                    print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")        

#===========================
#Fitur Menghapus Ulasan Tamu 
#===========================
def hapus_ulasan():
    while True:
        print('DATA ULASAN HOTEL')
        try:
            data_ulasan = pd.read_csv('data ulasan.csv')
            data_ulasan.index += 1
            tampilan_tabel(data_ulasan)    
        except FileNotFoundError:
            print("File 'data ulasan.csv' Tidak Ditemukan. Membuat File Baru\n")

        try:    
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Dihapus (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return
        
        if nomor in data_ulasan.index:
            data_ulasan = data_ulasan.drop(nomor)
            data_ulasan.to_csv('data ulasan.csv', index=False)
            clear_screen()
            print("Ulasan Tamu Berhasil Dihapus\n")
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan Dalam Data.\n")
            return

        while True:
            pilihan = input("Ingin Hapus Kamar Lagi? (Y/N): ").lower()
            if pilihan == ('Y').lower():
                clear_screen()
                print("Ulasan Tamu Berhasil Dihapus")
                print("Hapus Ulasan Tamu lagi\n")
                break  
            elif pilihan == ('N').lower():
                clear_screen()
                print("Ulasan Tamu Berhasil Dihapus")
                print("Kembali Ke Menu Utama\n")
                return  
            else:
                print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#==========================================
#Tampilan Fitur Kelola Data Transaksi Hotel 
#==========================================
def kelola_data_transaksi():
    while True:
        print('DATA TRANSAKSI HOTEL')
        try:
            data_ulasan = pd.read_csv('data transaksi.csv')
            data_ulasan.index += 1
            tampilan_tabel(data_ulasan)    
        except FileNotFoundError:
            print("File 'data transaksi.csv' Tidak Ditemukan. Membuat File Baru")

        print("╔═════════════════════════════════════════╗")
        print("║             Kelola Transaksi            ║")
        print("╠═════════════════════════════════════════╣")
        print("║ 1. Perbarui Nama Tamu                   ║")
        print("║ 2. Perbarui Nomor Identitas             ║")
        print("║ 3. Perbarui Nomor Kamar                 ║")
        print("║ 4. Perbarui Tipe Kamar                  ║")
        print("║ 5. Perbarui Fasilitas                   ║")
        print("║ 6. Perbarui Metode Pembayaran           ║")
        print("║ 7. Perbarui Staf                        ║")
        print("║ 8. Hapus Transaksi                      ║")
        print("║ 9. Keluar                               ║")
        print("╚═════════════════════════════════════════╝")

            
        pilihan = input("Masukkan pilihan (1-9): ")

        if pilihan == "1":
            clear_screen()
            perbarui_nama_tamu_transaksi()
        elif pilihan == "2":
            clear_screen()
            perbarui_nomor_identitas_transaksi()
        elif pilihan == "3":
            clear_screen()
            perbarui_nomor_kamar_transaksi()
        elif pilihan == "4":
            clear_screen()
            perbarui_tipe_kamar_transaksi()
        elif pilihan == "5":
            clear_screen()
            perbarui_fasilitas_transaksi()
        elif pilihan == "6":
            clear_screen()
            perbarui_metode_pembayaran()
        elif pilihan == "7":
            clear_screen()
            perbarui_staf()    
        elif pilihan == "8":
            clear_screen()
            hapus_transaksi()
        elif pilihan == "9":
            clear_screen()
            menu_utama()
        else:
            clear_screen()
            print("Input tidak valid. Harap masukkan angka (1-9)\n")

#==========================================
#Fitur Memperbarui Nama Tamu Pada Transaksi 
#==========================================
def perbarui_nama_tamu_transaksi():
    while True:
        print('DATA TRANSAKSI HOTEL')
        try:
            data_transaksi = pd.read_csv('data transaksi.csv')
            data_transaksi.index += 1
            tampilan_tabel(data_transaksi)    
        except FileNotFoundError:
            print("File 'data transaksi.csv' Tidak Ditemukan. Membuat File Baru\n")

        try:
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Diperbarui (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return

        if nomor in data_transaksi.index:
            ubah_nama = input("Nama Tamu Mau Diperbarui Apa? ")
            if (ubah_nama == ""):
                clear_screen()
                print("Nama Tamu Harus Berupa Huruf. Kembali\n")
                return
            elif not ubah_nama.isalpha():
                clear_screen()
                print("Nama Tamu Harus Berupa Huruf. Kembali\n")
                return
            else:
                data_transaksi.loc[nomor, 'Nama Tamu'] = ubah_nama
                data_transaksi.to_csv('data transaksi.csv', index=False)
                clear_screen()
                print("Nama Tamu Berhasil Diperbarui\n")
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan\n")

        while True:
                pilihan = input("Ingin Memperbarui Nama Tamu Lagi? (Y/N): ").lower()
                if pilihan == ('Y').lower():
                    clear_screen()
                    print("Nama Tamu Berhasil Diperbarui")
                    print("Perbarui Nama Tamu Baru Lagi\n")
                    break  
                elif pilihan == ('N').lower():
                    clear_screen()
                    print("Nama Tamu Berhasil Diperbarui")
                    print("Kembali Ke Menu Utama\n")
                    return  
                else:
                    print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")        

#=====================================================
#Fitur Memperbarui Nomor Identitas Tamu Pada Transaksi 
#=====================================================
def perbarui_nomor_identitas_transaksi():
    while True:
        print('DATA TRANSAKSI HOTEL')
        try:
            data_transaksi = pd.read_csv('data transaksi.csv')
            data_transaksi.index += 1
            tampilan_tabel(data_transaksi)    
        except FileNotFoundError:
            print("File 'data transaksi.csv' Tidak Ditemukan. Membuat File Baru\n")

        try:
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Diperbarui (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return

        if nomor in data_transaksi.index:
            try:
                ubah_no_identitas = int(input("Nomor Identitas Mau Diperbarui Berapa? "))
                if (ubah_no_identitas == ("")):
                    clear_screen()
                    print("Input Harus Berupa Angka. Kembali\n")
                    return
                elif ubah_no_identitas <= 0:
                    clear_screen()
                    print("Input Tidak boleh 0 atau dibawah 0. Kembali\n")
                    return
                else:
                    data_transaksi.loc[nomor, 'Nomor Identitas'] = ubah_no_identitas
                    data_transaksi.to_csv('data transaksi.csv', index=False)
                    clear_screen()
                    print("Nomor Identitas Berhasil Diperbarui\n")
            except ValueError:
                clear_screen()
                print("Nomor Baris Harus Berupa Angka. Kembali\n")
                return
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan\n")

        while True:
                pilihan = input("Ingin Memperbarui Nomor Identitas Lagi? (Y/N): ").lower()
                if pilihan == ('Y').lower():
                    clear_screen()
                    print("Nomor Identitas Berhasil Diperbarui")
                    print("Perbarui Nomor Identitas Baru Lagi\n")
                    break  
                elif pilihan == ('N').lower():
                    clear_screen()
                    print("Nomor Identitas Berhasil Diperbarui")
                    print("Kembali Ke Menu Utama\n")
                    return  
                else:
                    print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#=================================================
#Fitur Memperbarui Nomor Kamar Tamu Pada Transaksi 
#=================================================
def perbarui_nomor_kamar_transaksi():
    while True:
        print('DATA TRANSAKSI HOTEL')
        try:
            data_transaksi = pd.read_csv('data transaksi.csv')
            data_transaksi.index += 1
            tampilan_tabel(data_transaksi)    
        except FileNotFoundError:
            print("File 'data transaksi.csv' Tidak Ditemukan. Membuat File Baru\n")

        try:
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Diperbarui (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return

        if nomor in data_transaksi.index:
            try:
                ubah_no_kamar = int(input("Nomor Kamar Mau Diperbarui Berapa? "))
                if (ubah_no_kamar == ("")):
                    clear_screen()
                    print("Input Harus Berupa Angka. Kembali\n")
                    return
                elif ubah_no_kamar <= 0:
                    clear_screen()
                    print("Input Tidak boleh 0 atau dibawah 0. Kembali\n")
                    return
                else:
                    data_transaksi.loc[nomor, 'Nomor Kamar'] = ubah_no_kamar
                    data_transaksi.to_csv('data transaksi.csv', index=False)
                    clear_screen()
                    print("Nomor Kamar Berhasil Diperbarui\n")
            except ValueError:
                clear_screen()
                print("Nomor Baris Harus Berupa Angka. Kembali\n")
                return
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan\n")

        while True:
                pilihan = input("Ingin Memperbarui Nomor Kamar Lagi? (Y/N): ").lower()
                if pilihan == ('Y').lower():
                    clear_screen()
                    print("Nomor Kamar Berhasil Diperbarui")
                    print("Perbarui Nomor Kamar Baru Lagi\n")
                    break  
                elif pilihan == ('N').lower():
                    clear_screen()
                    print("Nomor Kamar Berhasil Diperbarui")
                    print("Kembali Ke Menu Utama")
                    return  
                else:
                    print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#================================================
#Fitur Memperbarui Tipe Kamar Tamu Pada Transaksi 
#================================================
def perbarui_tipe_kamar_transaksi():
    while True:
        print('DATA TRANSAKSI HOTEL')
        try:
            data_transaksi = pd.read_csv('data transaksi.csv')
            data_transaksi.index += 1
            tampilan_tabel(data_transaksi)    
        except FileNotFoundError:
            print("File 'data transaksi.csv' Tidak Ditemukan. Membuat File Baru\n")

        try:
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Diperbarui (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali")
            return

        if nomor in data_transaksi.index:
            ubah_tipe = input("TIpe Kamar Mau Diperbarui Apa? ")
            if (ubah_tipe == ""):
                clear_screen()
                print("Tipe Kamar Harus Berupa Huruf. Kembali\n")
                return
            elif not ubah_tipe.isalpha():
                clear_screen()
                print("Tipe Kamar Harus Berupa Huruf. Kembali\n")
                return
            else:
                data_transaksi.loc[nomor, 'Tipe Kamar'] = ubah_tipe
                data_transaksi.to_csv('data transaksi.csv', index=False)
                clear_screen()
                print("Tipe Kamar Berhasil Diperbarui\n")
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan\n")
                
        while True:
            pilihan = input("Ingin Memperbarui Tipe Kamar Lagi? (Y/N): ").lower()
            if pilihan == ('Y').lower():
                clear_screen()
                print("Tipe Kamar Berhasil Diperbarui")
                print("Perbarui Tipe Kamar Lagi\n")
                break  
            elif pilihan == ('N').lower():
                clear_screen()
                print("Tipe Kamar Berhasil Diperbarui")
                print("Kembali Ke Menu Utama\n")
                return  
            else:
                print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#==========================================
#Fitur Memperbarui Fasilitas Pada Transaksi 
#==========================================
def perbarui_fasilitas_transaksi():
    while True:
        print('DATA TRANSAKSI HOTEL')
        try:
            data_transaksi = pd.read_csv('data transaksi.csv')
            data_transaksi.index += 1
            tampilan_tabel(data_transaksi)    
        except FileNotFoundError:
            print("File 'data transaksi.csv' Tidak Ditemukan. Membuat File Baru\n")

        try:
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Diperbarui (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return

        if nomor in data_transaksi.index:
            ubah_fasilitas = input("Fasilitas Mau Diperbarui Apa? ")
            if (ubah_fasilitas == ""):
                clear_screen()
                print("Nama Fasilitas Harus Berupa Huruf. Kembali\n")
                return
            elif not ubah_fasilitas.isalpha():
                clear_screen()
                print("Nama Fasilitas Harus Berupa Huruf. Kembali\n")
                return
            else:
                data_transaksi.loc[nomor, 'Fasilitas'] = ubah_fasilitas
                data_transaksi.to_csv('data transaksi.csv', index=False)
                clear_screen()
                print("Fasilitas Berhasil Diperbarui\n")
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan\n")
                
        while True:
            pilihan = input("Ingin Memperbarui Fasilitas Lagi? (Y/N): ").lower()
            if pilihan == ('Y').lower():
                clear_screen()
                print("Fasilitas Berhasil Diperbarui")
                print("Perbarui Fasilitas Lagi\n")
                break  
            elif pilihan == ('N').lower():
                clear_screen()
                print("Fasilitas Berhasil Diperbarui")
                print("Kembali Ke Menu Utama\n")
                return  
            else:
                print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#===================================
#Fitur Memperbarui Metode Pembayaran 
#===================================
def perbarui_metode_pembayaran():
    while True:
        print('DATA TRANSAKSI HOTEL')
        try:
            data_transaksi = pd.read_csv('data transaksi.csv')
            data_transaksi.index += 1
            tampilan_tabel(data_transaksi)    
        except FileNotFoundError:
            print("File 'data transaksi.csv' Tidak Ditemukan. Membuat File Baru\n")
        
        try:
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Diperbarui (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return

        if nomor in data_transaksi.index:
            ubah_metode = input("Metode Pembayaran Mau Diperbarui Apa? ")
            if (ubah_metode == ""):
                clear_screen()
                print("Metode Pembayaran Harus Berupa Huruf. Kembali\n")
                return
            elif not ubah_metode.isalpha():
                clear_screen()
                print("Pembayaran Harus Berupa Huruf. Kembali\n")
                return
            else:
                data_transaksi.loc[nomor, 'Metode Pembayaran'] = ubah_metode
                data_transaksi.to_csv('data transaksi.csv', index=False)
                clear_screen()
                print("Metode Pembayaran Berhasil Diperbarui\n")
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan\n")
                
        while True:
            pilihan = input("Ingin Memperbarui Metode Pembayaran Lagi? (Y/N): ").lower()
            if pilihan == ('Y').lower():
                clear_screen()
                print("Metode Pembayaran Berhasil Diperbarui")
                print("Perbarui Metode Pembayaran Lagi\n")
                break  
            elif pilihan == ('N').lower():
                clear_screen()
                print("Metode Pembayaran Berhasil Diperbarui")
                print("Kembali Ke Menu Utama\n")
                return  
            else:
                print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#================================================
#Fitur Memperbarui Nama Staf Hotel Pada Transaksi 
#================================================
def perbarui_staf():
    while True:
        print('DATA TRANSAKSI HOTEL')
        try:
            data_transaksi = pd.read_csv('data transaksi.csv')
            data_transaksi.index += 1
            tampilan_tabel(data_transaksi)    
        except FileNotFoundError:
            print("File 'data transaksi.csv' Tidak Ditemukan. Membuat File Baru\n")

        try:
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Diperbarui (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali\n")
            return

        if nomor in data_transaksi.index:
            ubah_staf = input("Staf Mau Diperbarui Siapa? ")
            if (ubah_staf == ""):
                clear_screen()
                print("Tipe Kamar Harus Berupa Huruf. Kembali\n")
                return
            elif not ubah_staf.isalpha():
                clear_screen()
                print("Tipe Kamar Harus Berupa Huruf. Kembali\n")
                return
            else:
                data_transaksi.loc[nomor, 'Staf'] = ubah_staf
                data_transaksi.to_csv('data transaksi.csv', index=False)
                clear_screen()
                print("Staf Berhasil Diperbarui\n")
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan\n")
                
        while True:
            pilihan = input("Ingin Perbarui Staf Lagi? (Y/N): ").lower()
            if pilihan == ('Y').lower():
                clear_screen()
                print("Staf Berhasil Diperbarui")
                print("Perbarui Staf Lagi\n")
                break  
            elif pilihan == ('N').lower():
                clear_screen()
                print("Staf Berhasil Diperbarui")
                print("Kembali Ke Menu Utama\n")
                return  
            else:
                print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.\n")

#=========================
#Fitur Menghapus Transaksi 
#=========================
def hapus_transaksi():
    while True:
        print('DATA TRANSAKSI HOTEL')
        try:
            data_transaksi = pd.read_csv('data transaksi.csv')
            data_transaksi.index += 1
            tampilan_tabel(data_transaksi)    
        except FileNotFoundError:
            print("File 'data transaksi.csv' Tidak Ditemukan. Membuat File Baru")

        try:    
            nomor = int(input("Masukkan Nomor Baris Yang Ingin Dihapus (Mulai Dari 1): "))
        except ValueError:
            clear_screen()
            print("Nomor Baris Harus Berupa Angka. Kembali")
            return
        
        if nomor in data_transaksi.index:
            data_transaksi = data_transaksi.drop(nomor)
            data_transaksi.to_csv('data transaksi.csv', index=False)
            clear_screen()
            print("Transaksi Berhasil Dihapus")
        else:
            clear_screen()
            print(f"Baris {nomor} Tidak Ditemukan Dalam Data.")
            return

        while True:
            pilihan = input("Ingin Hapus Transaksi Lagi? (Y/N): ").lower()
            if pilihan == ('Y').lower():
                clear_screen()
                print("Transaksi Berhasil Dihapus")
                print("Hapus Transaksi lagi\n")
                break  
            elif pilihan == ('N').lower():
                clear_screen()
                print("Transaksi Berhasil Dihapus")
                print("Kembali Ke Menu Utama")
                return  
            else:
                print("Input Tidak Valid. Masukkan 'Y' Untuk Ya atau 'N' Untuk Tidak.")        

#=================
#FLogin Staf Hotel 
#=================
def autentikasi():
    clear_screen()
    akun = pd.read_csv('akun admin.csv')
    akun = akun.astype({'Password':'string'})
    for i in range(4):
        if i == 3:
            print("up up coba lagi")
            sys.exit()
        print("╔═════════════════════════════════════════╗")
        print("║       Selamat Datang di Hotel Lexa      ║")
        print("╚═════════════════════════════════════════╝")
        
        print("╔═════════════════════════════════════════╗") 
        username = input("║ Masukkan Username:")
        password = input("║ Masukkan Password:")
        print("╚═════════════════════════════════════════╝")
        
        if ((akun['Username'] == username) & (akun['Password'] == password)).any():
            clear_screen()
            print("Login berhasil!\n")
            menu_utama()
        else:
            print("\n")
            print("Username atau Password Salah!")
            input("Tekan Enter untuk Coba Lagi...")
            clear_screen()

#==========
#Menu Utama 
#==========
def menu_utama():
    while True:
        print("╔════════════════════════════════════╗")
        print("║             Hotel Lexa             ║")
        print("╠════════════════════════════════════╣")
        print("║ ╔════════════════════════════════╗ ║")
        print("║ ║ 1. Kelola Data Hotel           ║ ║")
        print("║ ║ 2. Kelola Fasilitas Hotel      ║ ║")
        print("║ ║ 3. Kelola Pemesanan            ║ ║")
        print("║ ║ 4. Kelola Manajemen Kamar      ║ ║")
        print("║ ║ 5. Kelola Ulasan               ║ ║")
        print("║ ║ 6. Kelola Transaksi            ║ ║")
        print("║ ║ 7. Keluar                      ║ ║")
        print("║ ╚════════════════════════════════╝ ║")
        print("╚════════════════════════════════════╝")

        pilihan = input("Masukkan pilihan (1-7): ")

        if pilihan == "1":
            clear_screen()
            kelola_data_hotel()
        elif pilihan == "2":
            clear_screen()
            kelola_fasilitas()
        elif pilihan == "3":
            clear_screen()
            kelola_pesanan()
        elif pilihan == "4":
            clear_screen()
            kelola_kamar_hotel()
        elif pilihan == "5":
            clear_screen()
            kelola_data_ulasan()
        elif pilihan == "6":
            clear_screen()
            kelola_data_transaksi()
        elif pilihan == "7":
             sys.exit()
        else:
            clear_screen()
            print("Input Tidak Valid Harap Masukkan Angka (1-7)\n")

#==============================
#Menjalankan Fungsi autentikasi 
#==============================
autentikasi()