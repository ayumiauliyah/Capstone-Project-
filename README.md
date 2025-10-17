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
> contoh output
<img width="671" height="130" alt="Screenshot 2025-10-17 at 22 38 19" src="https://github.com/user-attachments/assets/0e01f86a-36cc-4a11-9589-a93fd24075eb" />

**2. menambahkan buku ke dalam daftar buku perpustakaan**
- untuk membatalkan menu ini, pengguna dapat menginput angka "0" pada judul dan penulis
- pada menu ini, nilai yang perlu diinput adalah:
a. judul buku (tidak boleh kosong)
b. penulis (tidak boleh kosong)
c. jenis buku (fiksi/non-fiksi)
d. status (ada/tidak ada)
e. tahun terbit (integer)
kode buku akan dibuat secara otomatis dengan informasi jenis buku, tahun terbit, dan urutan buku berdasarkan jenis
> contoh output
<img width="671" height="139" alt="Screenshot 2025-10-17 at 22 39 11" src="https://github.com/user-attachments/assets/f999a1a6-04fb-4df9-98aa-c6bcdf7c9cf4" />

**3. mengedit buku yang sudah ada dalam daftar buku perpustakaan**
- untuk membatalkan menu ini, pengguna dapat mengosongkan input pada index yang ingin disunting
- pengguna perlu mengisi input index buku yang ingin diedit
- edit buku tidak dapat dijalankan jika nilai yang ingin diubah adalah "kode" karena "kode" merupakan kolom unik
- selain nilai kode, edit buku dapat dijalankan
> contoh output
<img width="676" height="171" alt="Screenshot 2025-10-17 at 22 41 43" src="https://github.com/user-attachments/assets/aca76bfb-9580-46c2-8746-0f9ccc76a4f1" />

**4. menghapus buku dalam daftar buku perpustakaan**
- untuk membatalkan menu ini, pengguna dapat mengosongkan input pada index yang ingin dihapus
- pengguna perlu mengisi input index buku yang ingin dihapus
> contoh output
<img width="683" height="317" alt="Screenshot 2025-10-17 at 22 42 13" src="https://github.com/user-attachments/assets/d02bc90c-4216-4d97-bb87-f79a4fe11115" />

**5. mendaftarkan pengunjung**
- untuk membatalkan menu ini, pengguna dapat mengosongkan input pada nama
- pada menu ini, nilai yang perlu diinput adalah:
a. nama pengunjung
b. umur (integer)
c. pekerjaan (tidak boleh kosong)
tabel akan secara otomatis menampilkan daftar pengunjung & waktu kunjungan
> contoh output
<img width="599" height="145" alt="Screenshot 2025-10-17 at 22 42 50" src="https://github.com/user-attachments/assets/2d32e8a4-1aa3-4c53-9faf-7ff202d0201f" />

**6. peminjaman buku**
- pada menu ini, pengguna perlu mengisi input nama pengunjung dengan tujuan buku yang dipinjam diketahui peminjamnya oleh pihak perpustakaan. Apabila nama pengunjung belum terdaftar pada daftar pengunjung, maka pengguna akan dialihkan memilih menu 5 di menu utama untuk mendaftar terlebih dahulu
- untuk membatalkan menu ini, pengguna dapat mengosongkan input pada index buku yang ingin dipinjam 
- apabila index buku yang ingin dipinjam valid, maka status buku dalam daftar buku berubah menjadi "tidak ada" dan buku akan terlihat dipinjam oleh peminjam
> contoh output
<img width="707" height="208" alt="Screenshot 2025-10-17 at 22 43 16" src="https://github.com/user-attachments/assets/fe68b7da-8b5e-4a4e-890c-a27bfcbb7f7f" />

**7. pengembalian buku**
- pada menu ini, pengguna perlu mengisi input nama pengunjung dengan tujuan peminjam bertanggung jawab dengan buku yang dipinjam. Apabila nama pengunjung belum terdaftar pada daftar pengunjung, maka pengguna akan dialihkan memilih menu 5 di menu utama untuk mendaftar terlebih dahulu
- untuk membatalkan menu ini, pengguna dapat mengosongkan input pada index buku yang ingin dikembalikan
- apabila index buku yang ingin dikembalikan valid, maka status buku dalam daftar buku berubah menjadi "ada" kembali dan buku di daftar pengunjung akan kosong
> contoh output
<img width="671" height="194" alt="Screenshot 2025-10-17 at 22 44 10" src="https://github.com/user-attachments/assets/573f24fd-732f-4b4f-9f59-5b1edc68e8e1" />

**8. exit program**
Apabila pengguna memilih menu ini, maka program akan dihentikan.
> contoh output
<img width="464" height="183" alt="Screenshot 2025-10-17 at 22 45 15" src="https://github.com/user-attachments/assets/2f9d4294-d7b8-42c1-ad01-56f01345054c" />

Apabila pengguna memilih menu selain menu diatas, maka menu tidak valid.



