# Capstone Project 1: Perpustakaan
Program ini bertujuan untuk memudahkan pengguna dalam manajemen perpustakaan meliputi tracking daftar buku perpustakaan, daftar pengunjung serta buku yang dipinjam dan dikembalikan.

## Fitur
Fitur yang ada pada program ini adalah:
1. Menampilkan daftar buku (fitur read)
2. Menambah buku (fitur create)
3. Mengedit buku (fitur update)
4. Menghapus buku (fitur delete)
5. Mendaftarkan pengunjung (fitur create)
6. Peminjaman buku (fitur update)
7. Pengembalian buku (fitur update)
8. Exit program

Dictionary 
key: judul buku
value: kode (kolom unik), penulis, jenis, tahun terbit, status

## Cara menjalankan program
library yang diperlukan:
1. tabulate --> menampilkan tabel yang rapi di terminal
2. datetime --> menampilkan waktu
3. rich --> menampilkan tabel dan teks yang menarik dan interaktif
4. pyinputplus --> validasi input yang mudah dan aman

pilihan menu dalam input:
**1. menampilkan daftar buku**

**2. menambahkan buku ke dalam daftar buku perpustakaan**
- untuk membatalkan menu ini, pengguna dapat menginput angka "0" pada judul dan penulis
- pada menu ini, nilai yang perlu diinput adalah:
a. judul buku (tidak boleh kosong)
b. penulis (tidak boleh kosong)
c. jenis buku (fiksi/non-fiksi)
d. status (ada/tidak ada)
e. tahun terbit (integer)
kode buku akan dibuat secara otomatis dengan informasi jenis buku, tahun terbit, dan urutan buku berdasarkan jenis

**3. mengedit buku yang sudah ada dalam daftar buku perpustakaan**
- untuk membatalkan menu ini, pengguna dapat mengosongkan input pada index yang ingin disunting
- pengguna perlu mengisi input index buku yang ingin diedit
- edit buku tidak dapat dijalankan jika nilai yang ingin diubah adalah "kode" karena "kode" merupakan kolom unik
- selain nilai kode, edit buku dapat dijalankan

**4. menghapus buku dalam daftar buku perpustakaan**
- untuk membatalkan menu ini, pengguna dapat mengosongkan input pada index yang ingin dihapus
- pengguna perlu mengisi input index buku yang ingin dihapus

**5. mendaftarkan pengunjung**
- untuk membatalkan menu ini, pengguna dapat mengosongkan input pada nama
- pada menu ini, nilai yang perlu diinput adalah:
a. nama pengunjung
b. umur (integer)
c. pekerjaan (tidak boleh kosong)
tabel akan secara otomatis menampilkan daftar pengunjung & waktu kunjungan

**6. peminjaman buku**
- pada menu ini, pengguna perlu mengisi input nama pengunjung dengan tujuan buku yang dipinjam diketahui peminjamnya oleh pihak perpustakaan. Apabila nama pengunjung belum terdaftar pada daftar pengunjung, maka pengguna akan dialihkan memilih menu 5 di menu utama untuk mendaftar terlebih dahulu
- untuk membatalkan menu ini, pengguna dapat mengosongkan input pada index buku yang ingin dipinjam 
- apabila index buku yang ingin dipinjam valid, maka status buku dalam daftar buku berubah menjadi "tidak ada" dan buku akan terlihat dipinjam oleh peminjam

**6. peminjaman buku**
- pada menu ini, pengguna perlu mengisi input nama pengunjung dengan tujuan peminjam bertanggung jawab dengan buku yang dipinjam. Apabila nama pengunjung belum terdaftar pada daftar pengunjung, maka pengguna akan dialihkan memilih menu 5 di menu utama untuk mendaftar terlebih dahulu
- untuk membatalkan menu ini, pengguna dapat mengosongkan input pada index buku yang ingin dikembalikan
- apabila index buku yang ingin dikembalikan valid, maka status buku dalam daftar buku berubah menjadi "ada" kembali dan buku di daftar pengunjung akan kosong
