#import library
from tabulate import tabulate
import datetime

#pip install rich (terminal)
#pip install pyinputplus (terminal)

from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

import pyinputplus as pyip

console = Console()
console_table = Console() 
console_tambah = Console()
console_edit = Console()
console_hapus = Console()
console_kunjung = Console()
console_pinjam = Console()
console_kembali = Console()
console_daftar = Console()

buku = {
    "Rich Dad Poor Dad": {"Kode": "N20051", "Penulis": "Robert Kiyosaki", "Jenis": "Non-Fiksi", "Tahun terbit": "2005", "Status": "Ada"},
    "Hujan": {"Kode": "F20121", "Penulis": "Tere Liye", "Jenis": "Fiksi", "Tahun terbit": "2012", "Status": "Ada" },
    "Hello": {"Kode": "F20132", "Penulis": "Tere Liye", "Jenis": "Fiksi", "Tahun terbit": "2013", "Status": "Ada"}
}
daftar = {}
pil_menu = True

#function
def tampilkan_menu():
    panel = Panel("=== LIST MENU ===\n"
                  "1. Menampilkan Daftar Buku\n"
                  "2. Menambah Buku\n"
                  "3. Mengedit Buku\n"
                  "4. Menghapus Buku\n"
                  "5. Daftar Pengunjung\n"
                  "6. Peminjaman Buku\n"
                  "7. Pengembalian Buku\n"
                  "8. Exit Program",
                 title = "\nSelamat datang di Perpustakaan Yumi! \n")
    console.print(panel)

def tampilkan_buku():
    table = Table(title="Koleksi Buku Perupustakaan")
    table.add_column("Index", justify="center", style="bold yellow")
    table.add_column("Nama Buku", style="bold white")
    table.add_column("Kode Buku", style="cyan")
    table.add_column("Penulis", style="green")
    table.add_column("Jenis", style="bright_blue")
    table.add_column("Tahun Terbit", justify="center", style="bright_yellow")
    table.add_column("Status", justify="center", style="bold red")

    for i, (Judul, data) in enumerate(buku.items()):
        table.add_row(
            str(i),
            Judul,
            data["Kode"],
            data["Penulis"],
            data["Jenis"],
            str(data["Tahun terbit"]),
            str(data["Status"])
        )

    console_table.print(table)

def kode_buku(i_jenis):
    if i_jenis == "Fiksi":
        awalan = "F"
    else:
        awalan = "N"
    
    #hitung jumlah buku
    jumlah = 0
    for data in buku.values():
        if data["Kode"].startswith(awalan):
            jumlah += 1
    
    #kode buku baru
    jumlah = (jumlah+1)
    i_kode = awalan + str(i_tahunterbit) + str(jumlah)

    return i_kode

def kode_buku_j(i_jenis):
    if i_jenis == "Fiksi":
        awalan = "F"
    else:
        awalan = "N"
    
    #hitung jumlah buku
    jumlah = 0
    for data in buku.values():
        if data["Kode"].startswith(awalan):
            jumlah += 1

    #kode buku baru
    jumlah = (jumlah+1) 
    for data in buku.values():
        tt = data["Kode"][1:5]
    i_kode = awalan + tt + str(jumlah)

    return i_kode

def kode_buku_t(i_tahunterbit, kode_lama):
    awalan = kode_lama[0:1]
    akhiran = kode_lama[5:]
    i_kode = awalan + str(i_tahunterbit) + akhiran

    return i_kode

def tambah_buku(i_kode, i_judul , i_jenis, i_status, i_tahunterbit):
    buku[i_judul] = {"Kode": i_kode, "Penulis" : i_penulis, "Jenis": i_jenis, "Tahun terbit": i_tahunterbit, "Status": i_status}
    print(f"Buku {i_judul} berhasil ditambahkan!")

def HapusBuku(i_hapus_buku):
    if 0 <= i_hapus_buku < len(buku):
        NamaBuku = list(buku.keys())[i_hapus_buku] #berdasarkan index
        buku.pop(NamaBuku)
        print(f" {NamaBuku} berhasil dihapus!")
    else:
        print("Index tidak valid!")

def daftar_kunjung(nama_orang, umur_orang, job_orang, enter_time):
        if nama_orang not in daftar:
            daftar[nama_orang] = {"Umur": umur_orang, "Pekerjaan" : job_orang, "Waktu kunjungan": enter_time, "Buku Dipinjam":[]}
            print(f"Pengunjung {nama_orang} berhasil ditambahkan!")
        else:
            print(f"Pengunjung {nama_orang} sudah terdaftar")

def tampilkan_pengujung():
    tabel = [[i, nama, dataa["Umur"], dataa["Pekerjaan"], dataa["Waktu kunjungan"], dataa["Buku Dipinjam"]] for i, (nama, dataa) in enumerate(daftar.items())]
    print(tabulate(tabel, headers=["Index", "Nama", "Umur", "Pekerjaan", "Waktu kunjungan", "Buku Dipinjam"], tablefmt="grid"))

def EditBuku(edit_field, edit_value):
    data_buku[edit_field] = edit_value
    print(f"Data {edit_field} berhasil diubah!")
    return edit_value

def Pinjam_Buku(pinjam_buku, NamaBuku_pinjam):
    if 0 <= pinjam_buku < len(buku):
        buku[NamaBuku_pinjam]["Status"] = "Tidak Ada"
        print(f"Buku {NamaBuku_pinjam} berhasil dipinjam")
        tampilkan_buku()
        daftar[nama_pinjam]["Buku Dipinjam"].append(NamaBuku_pinjam)
        tampilkan_pengujung()

def Kembali_Buku(kembali_buku, NamaBuku_kembali):
    if 0 <= kembali_buku < len(buku):
        buku[NamaBuku_kembali]["Status"] = "Ada"
        print(f"Buku {NamaBuku_kembali} berhasil dikembalikan")
        tampilkan_buku()
        daftar[nama_pinjam]["Buku Dipinjam"].remove(NamaBuku_kembali)
        tampilkan_pengujung()

while pil_menu:
    tampilkan_menu()
    menu = input("Masukkan angka menu yang ingin dijalankan: ")

    if menu == "1":
        tampilkan_buku()

    elif menu == "2":
        p_tambah = Panel("=== Menambahkan Buku ===")
        console_tambah.print(p_tambah)
        jenis = True
        status = True

        print("Jika ingin membatalkan tambah buku, input dengan angka 0 pada judul dan penulis")
        i_judul = pyip.inputStr("Masukkan judul buku: ", blank = False).title()
        i_penulis = pyip.inputStr("Masukkan nama penulis: ", blank = False).title()

        if i_judul == "0" and i_penulis == "0":
            print("Tambah buku dibatalkan.")
            continue
        
        print("Pilih jenis buku: ")
        i_jenis = pyip.inputMenu(['Fiksi', 'Non-Fiksi'], numbered = True)
        print("Pilih status buku: ")
        i_status = pyip.inputMenu(["Ada", "Tidak Ada"], numbered = True)
        i_tahunterbit = pyip.inputInt("Masukkan tahun terbit: ")

        kode_buku(i_jenis)
        i_kode = kode_buku(i_jenis)
        tambah_buku(i_kode, i_judul , i_jenis, i_status, i_tahunterbit)
        tampilkan_buku()

    elif menu == "3":
        p_edit = Panel("=== Menyunting Buku ===")
        console_edit.print(p_edit)
        edit = True

        tampilkan_buku()

        while edit == True:
            print("Jika ingin membatalkan penyuntingan buku, kosongkan input ")
            edit_buku = input("Masukkan index yang ingin disunting: ")

            if edit_buku == "":
                print("Penyuntingan buku dibatalkan.")
                edit = False
                break

            if not edit_buku.isdigit():
                print("Index harus berupa angka!")
                continue

            edit_buku = int(edit_buku)
            if not 0 <= edit_buku < len(buku):
                print("Index tidak valid")
                continue
            else:
                NamaBuku = list(buku.keys())[edit_buku] #index judul buku
                data_buku = buku[NamaBuku]

            print("Berikut adalah nilai yang dapat diubah")
            print("Judul\n"
                    "Penulis\n"
                    "Jenis\n"
                    "Tahun terbit\n"
                    "Status\n") #untuk nambahin judul
            
            edit_field = input("Masukkan nilai yang ingin diubah: ").capitalize()
            if edit_field == "Kode":
                print("Kode tidak dapat diubah")
                continue   

            elif edit_field == "Tahun terbit":
                edit_value = pyip.inputInt("Masukkan nilai yang ingin diubah: ")
                EditBuku(edit_field, edit_value)
                i_tahunterbit = edit_value
                kode_lama = data_buku["Kode"]
                data_buku["Kode"] = kode_buku_t(i_tahunterbit, kode_lama)
                tampilkan_buku()
                break

            elif edit_field == "Jenis":
                edit_value = pyip.inputMenu(['Fiksi', 'Non-Fiksi'], numbered = True)
                EditBuku(edit_field, edit_value)
                i_jenis = edit_value
                data_buku["Kode"] = kode_buku_j(i_jenis)
                tampilkan_buku()
                break

            elif edit_field == "Status":
                edit_value = pyip.inputMenu(["Ada", "Tidak Ada"], numbered = True)
                EditBuku(edit_field, edit_value)
                tampilkan_buku()
                break

            elif edit_field == "Penulis":
                edit_value = input(f"Masukkan nilai baru untuk {edit_field}: ").title()
                EditBuku(edit_field, edit_value)
                tampilkan_buku()
                break      

            elif edit_field == "Judul" :
                edit_value = input(f"Masukkan nilai baru untuk {edit_field}: ").title()
                buku[edit_value] = buku.pop(NamaBuku) #menambahkan data baru di index yang dihapus
                print(f"Data {edit_field} berhasil diubah!")
                tampilkan_buku()
                break
            else:
                print("Index tidak valid!")
                continue

    elif menu =="4":
        p_hapus = Panel("=== Menghapus Buku ===")
        console_hapus.print(p_hapus)

        clearbuku = True
        while clearbuku == True:

            tampilkan_buku()
            print("Jika ingin membatalkan hapus buku, kosongkan input ")
            hapus_buku = input("Masukkan index yang ingin dihapus: ")

            if hapus_buku == "":
                print("Hapus buku dibatalkan.")
                clearbuku = False
                break
            
            hapus_buku= int(hapus_buku)
            if 0 <= hapus_buku < len(buku):
                i_hapus_buku = hapus_buku
                HapusBuku(i_hapus_buku)
                tampilkan_buku()
                break
            else:
                print("Index tidak valid!")
                continue

    elif menu == "5" :         
        p_kunjung = Panel("=== Daftar Pengunjung ===")
        console_kunjung.print(p_kunjung)
        tampilkan_pengujung()

        pengunjung = True
        umur = True

        print("Jika ingin membatalkan pendaftaran pengunjung, kosongkan input pada nama ")
        nama_orang = input("Masukkan nama pengunjung: ").title()
        if nama_orang == "":
            print("Pendaftaran pengunjung dibatalkan!")
            continue

        umur_orang = pyip.inputInt("Masukkan umur pengunjung: ")
        job_orang = pyip.inputStr("Masukkan pekerjaan pengunjung: ", blank = False).title()
        enter_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        daftar_kunjung(nama_orang, umur_orang, job_orang, enter_time)
        tampilkan_pengujung()

    elif menu == "6" :
        p_pinjam = Panel("=== Peminjaman Buku ===")
        console_pinjam.print(p_pinjam)
        
        PinjamBuku = True

        while PinjamBuku == True:
            nama_pinjam = input("Masukkan nama pengunjung: ").title()
            if nama_pinjam not in daftar:
                print("Pengunjung belum terdaftar. Silakan daftar di menu 5")
                break
            
            tampilkan_buku()
            print("Jika ingin membatalkan peminjaman buku, kosongkan input pada index buku ")
            pinjam_buku = input("Masukkan index buku yang ingin dipinjam: ")

            if pinjam_buku == "":
                print("Pinjam buku dibatalkan.")
                PinjamBuku = False
                break

            if not pinjam_buku.isdigit():
                print("Index tidak valid.")
                continue

            pinjam_buku = int(pinjam_buku)
            if not 0 <= pinjam_buku < len(buku):
                print("Index tidak valid.")
                continue

            NamaBuku_pinjam = list(buku.keys())[pinjam_buku] #index judul buku

            if buku[NamaBuku_pinjam]["Status"] == "Tidak Ada":
                print(f"Buku {NamaBuku_pinjam} sedang tidak tersedia")
                continue

            Pinjam_Buku(pinjam_buku, NamaBuku_pinjam)  
            break

    elif menu == "7" :
        p_kembali = Panel("=== Pengembalian Buku ===")
        console_kembali.print(p_kembali)

        KembaliBuku = True

        while KembaliBuku == True:

            nama_kembali = input("Masukkan nama pengunjung: ").title()
            if nama_kembali not in daftar:
                print("Pengunjung belum terdaftar. Silakan daftar di menu 5")
                break

            tampilkan_buku()
            print("Jika ingin membatalkan peminjaman buku, kosongkan input pada index buku")
            kembali_buku = input("Masukkan index buku yang ingin dikembalikan: ")

            if kembali_buku == "":
                print("Pengembalian buku dibatalkan.")
                PinjamBuku = False
                break

            if not kembali_buku.isdigit():
                print("Index tidak valid.")
                continue

            kembali_buku = int(kembali_buku)
            if not 0 <= kembali_buku < len(buku):
                print("Index tidak valid.")
                continue

            NamaBuku_kembali = list(buku.keys())[kembali_buku] #index judul buku

            if buku[NamaBuku_kembali]["Status"] == "Ada":
                print("Index tidak valid")
                continue

            Kembali_Buku(kembali_buku, NamaBuku_kembali)
            break

    elif menu == "8":
        print("Program selesai. Terima kasih sudah datang ke Perpustakaan Yumi!")
        pil_menu = False

    else:
        print("Menu tidak valid, coba lagi.")
        


 

