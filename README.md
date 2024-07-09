# TUGAS UAS

## Deskripsi
Program ini merupakan implementasi segmentasi gambar menggunakan algoritma k-means clustering. Pengguna dapat memilih gambar dari komputernya, menentukan jumlah cluster (K), dan melihat hasil segmentasi gambar tersebut.

## Persyaratan
Pastikan Anda telah menginstal Python di sistem Anda. Program ini memerlukan beberapa pustaka Python yang dapat diinstal secara otomatis jika belum ada di sistem Anda.

Pustaka yang dibutuhkan:
- numpy
- matplotlib
- opencv-python
- tk

## Cara Menjalankan Program

1. **Unduh dan Buka Program**
    - Unduh file `TUGAS UAS.py` dari repository ini.
    - Buka terminal atau command prompt dan navigasikan ke direktori tempat file `TUGAS UAS.py` berada.

2. **Jalankan Program**
    - Jalankan perintah berikut untuk menjalankan program:
      ```bash
      python TUGAS UAS.py
      ```

3. **Pilih Gambar**
    - Setelah program dijalankan, sebuah dialog pemilihan file akan muncul. Pilih gambar dengan format `.jpg`, `.jpeg`, atau `.png` yang ingin Anda segmentasikan.

4. **Masukkan Jumlah Cluster**
    - Program akan meminta Anda untuk memasukkan jumlah cluster (K). Masukkan nilai numerik yang lebih besar dari 0.

5. **Lihat Hasil**
    - Program akan menampilkan gambar asli dan gambar yang telah tersegmentasi berdampingan dalam jendela pop-up.

## Struktur Kode
- **Pemasangan Pustaka Otomatis**: Program akan memeriksa dan menginstal pustaka yang diperlukan jika belum terpasang.
- **Pemilihan File Gambar**: Menggunakan Tkinter untuk membuka dialog pemilihan file.
- **Pengaturan K-Means**: Menggunakan OpenCV untuk melakukan k-means clustering pada gambar yang dipilih.
- **Tampilan Hasil**: Menggunakan Matplotlib untuk menampilkan gambar asli dan hasil segmentasi.

## Contoh Gambar 

<img src="https://github.com/ferdycuy/ReportUasCitra/assets/115714443/79ec4dc4-e414-4c32-a01e-911d787cb1db" alt="Hasil Segmentasi1" width="600"/>

<img src="https://github.com/ferdycuy/ReportUasCitra/assets/115714443/519010c6-515c-43ce-9aee-622d7db5332f" alt="Hasil Segmentasi2" width="600"/>

<img src="https://github.com/ferdycuy/ReportUasCitra/assets/115714443/35983ed8-e57a-4312-9447-cd1982ce2658" alt="Hasil Segmentasi3" width="600"/>




