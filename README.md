# RyuChain# 🔗 ChainProof

ChainProof adalah aplikasi blockchain sederhana berbasis Python dan Flask yang digunakan untuk melakukan verifikasi keaslian dokumen digital menggunakan teknologi Blockchain, SHA-256 Hashing, RSA Digital Signature, dan Proof of Work (PoW).

Sistem ini memungkinkan pengguna untuk:
- Mengunggah dokumen
- Menghasilkan hash dokumen
- Menyimpan hash ke blockchain
- Melakukan verifikasi dokumen
- Melihat Blockchain Explorer
- Mengamankan autentikasi pengguna menggunakan BCrypt


# Fitur Utama

# Upload Dokumen
Pengguna dapat mengunggah dokumen digital ke sistem. Dokumen akan di-hash menggunakan SHA-256 dan disimpan ke blockchain.


# Verifikasi Dokumen
Publik dapat memverifikasi apakah dokumen telah terdaftar pada blockchain atau belum.


# Blockchain Explorer
Menampilkan seluruh block yang tersimpan pada blockchain beserta:
- Block Hash
- Previous Hash
- Document Hash
- Timestamp
- Signature


# Digital Signature RSA
Setiap hash dokumen ditandatangani menggunakan RSA Digital Signature untuk menjaga autentikasi data.


# Proof of Work (PoW)
Blockchain menggunakan algoritma Proof of Work untuk proses validasi block.


# Login dan Register
Sistem memiliki autentikasi user menggunakan BCrypt password hashing.


# Teknologi yang Digunakan

| Teknologi | Fungsi |
|---|---|
| Python | Bahasa pemrograman utama |
| Flask | Web Framework |
| SHA-256 | Hashing dokumen |
| RSA | Digital Signature |
| BCrypt | Password Hashing |
| JSON | Penyimpanan blockchain |
| Bootstrap 5 | User Interface |


# Algoritma Kriptografi

1. SHA-256
Digunakan untuk menghasilkan hash unik dari dokumen.

2. RSA Digital Signature
Digunakan untuk menandatangani hash dokumen menggunakan private key.

3. Proof of Work (PoW)
Digunakan untuk memvalidasi block sebelum masuk ke blockchain.

4. BCrypt
Digunakan untuk mengamankan password pengguna.


# Struktur Folder
chainproof/
│
├── app.py
├── blockchain/
├── crypto/
├── routes/
├── services/
├── templates/
├── static/
├── uploads/
├── keys/
├── database/
└── utils/


# Instalasi

1. Clone Repository

git clone https://github.com/alimasumajja/RyuChain.git

2. Masuk ke Folder Project

cd chainproof

3. Install Dependency

pip install -r requirements.txt

4. Jalankan Aplikasi
python app.py

5. Akses Browser

http://127.0.0.1:5000


# Alur Sistem


User Upload Dokumen
↓
SHA-256 Membuat Hash
↓
RSA Membuat Digital Signature
↓
Block Dibuat
↓
Proof of Work Mining
↓
Block Disimpan ke Blockchain
↓
Dokumen Dapat Diverifikasi


# Sistem Keamanan

Sistem menggunakan beberapa lapisan keamanan:

- SHA-256 untuk integritas dokumen
- RSA Digital Signature untuk autentikasi
- Proof of Work untuk validasi blockchain
- BCrypt untuk keamanan password user


# Keterbatasan Sistem

Beberapa keterbatasan sistem saat ini:

- Masih menggunakan penyimpanan JSON
- Belum menggunakan Merkle Tree
- Belum Multi-chain
- Dokumen masih tersimpan lokal
- Signature masih menggunakan server-side signing


# Pengembangan Selanjutnya

Pengembangan yang direncanakan:

- Implementasi User-Based Digital Signature
- Migrasi database ke SQLite/PostgreSQL
- Implementasi Merkle Tree
- Implementasi Multi-Chain
- Penyimpanan cloud storage


# Developer

Proyek ini dikembangkan untuk kebutuhan pembelajaran dan implementasi mata kuliah Kriptografi dan Blockchain.

# License

This project is licensed for educational purposes.
