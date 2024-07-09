import subprocess
import sys

# Fungsi untuk menginstal pustaka
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Daftar pustaka yang dibutuhkan
required_packages = ['numpy', 'matplotlib', 'opencv-python', 'tk']

# Menginstal pustaka yang dibutuhkan
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install(package)

import numpy as np
import matplotlib.pyplot as plt
import cv2
from tkinter import Tk, filedialog

# Menampilkan plot dalam jendela pop-up
plt.ion()

# Fungsi untuk membuka dialog pemilihan file
def browse_file():
    root = Tk()
    root.withdraw()  # Menyembunyikan jendela utama Tkinter
    file_path = filedialog.askopenfilename(title="Pilih Gambar", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    return file_path

# Meminta pengguna untuk memilih gambar
image_path = browse_file()
if not image_path:
    print("Tidak ada gambar yang dipilih. Program dihentikan.")
    exit()

# Meminta pengguna untuk memasukkan jumlah cluster
k = input("Masukkan jumlah cluster (K): ")
try:
    k = int(k)
    if k <= 0:
        raise ValueError("Jumlah cluster harus lebih besar dari 0.")
except ValueError as e:
    print(f"Input tidak valid: {e}. Program dihentikan.")
    exit()

# Membaca gambar
image = cv2.imread(image_path)

# Mengubah warna gambar dari BGR ke RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Membentuk ulang gambar menjadi susunan piksel 2D dengan 3 nilai warna (RGB)
pixel_vals = image.reshape((-1, 3))

# Mengkonversikan ke tipe float
pixel_vals = np.float32(pixel_vals)

# Menentukan kriteria agar algoritme berhenti berjalan: 100 iterasi atau epsilon (akurasi yang dibutuhkan) mencapai 85%
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)

# Melakukan k-means clustering dengan jumlah cluster yang ditetapkan oleh pengguna dan pusat acak pada awalnya dipilih
retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Mengonversi data pusat cluster menjadi nilai 8-bit
centers = np.uint8(centers)

# Menggunakan label untuk membentuk ulang data menjadi dimensi gambar asli
segmented_data = centers[labels.flatten()]
segmented_image = segmented_data.reshape((image.shape))

# Menampilkan gambar asli dan gambar tersegmentasi berdampingan
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(segmented_image)
plt.title('Segmented Image')

plt.show()

# Menjaga plot tetap terbuka
plt.ioff()
plt.show()
