
# 🔐 Caesar Cipher Encryption Program

## 🧩 Deskripsi Singkat

Program ini mengimplementasikan algoritma **Caesar Cipher**, salah satu metode enkripsi klasik yang bekerja dengan **menggeser setiap huruf** pada teks sejumlah nilai kunci tertentu.
Program memiliki tiga mode utama:

1. **Enkripsi** – menyandikan teks menggunakan kunci.
2. **Dekripsi** – mengembalikan teks ke bentuk asli menggunakan kunci yang sama.
3. **Brute Force** – mencoba semua kemungkinan kunci (0–25) untuk menebak pesan terenkripsi.

---

## ⚙️ Fitur Utama

* Enkripsi teks menggunakan pergeseran alfabet.
* Dekripsi teks dengan kunci tertentu.
* Brute force untuk memecahkan pesan tanpa mengetahui kunci.
* Menampilkan hasil enkripsi, dekripsi, dan hasil percobaan brute force.

---

## 🧮 Hasil Program

### 🔸 Mode Enkripsi

Menampilkan teks yang telah dienkripsi dengan kunci tertentu.

```
Masukkan teks  : HELLO
Masukkan kunci : 3
Hasil Enkripsi : KHOOR
```

### 🔸 Mode Dekripsi

Mengembalikan teks terenkripsi ke bentuk asli.

```
Masukkan teks  : KHOOR
Masukkan kunci : 3
Hasil Dekripsi : HELLO
```

### 🔸 Mode Brute Force

Mencoba seluruh kemungkinan kunci dari 0–25.

```
Kunci 0 : KHOOR  
Kunci 1 : JGNNQ  
Kunci 2 : IFMMP  
Kunci 3 : HELLO  ← Hasil yang benar
...
Kunci 25 : LIPPS
```

---

## 🧩 Flowchart Program

```
     ┌────────────────────────┐
     │     Mulai Program      │
     └──────────┬─────────────┘
                │
     ┌──────────▼──────────┐
     │  Tampilkan Menu     │
     │1.Enkripsi 2.Dekripsi│
     │3.Brute Force 4.Keluar│
     └──────────┬──────────┘
                │
        ┌───────▼────────┐
        │  Input Pilihan  │
        └───────┬────────┘
                │
   ┌────────────┼────────────┐
   │             │            │
1.Enkripsi   2.Dekripsi   3.Brute Force
   │             │            │
   ▼             ▼            ▼
Enkripsi→Output  Dekripsi→Output  Tampilkan semua kunci
   │             │            │
   └─────────────┴────────────┘
                │
         ┌──────▼──────┐
         │   Keluar    │
         └─────────────┘
```

---

## 💻 Pseudocode Singkat

### 🔸 Enkripsi

```
FUNCTION enkripsi_caesar(teks, kunci)
    hasil ← ""
    FOR setiap huruf IN teks DO
        IF huruf besar → geser dari 'A'
        IF huruf kecil → geser dari 'a'
        selain itu → tetap
    END FOR
    RETURN hasil
END FUNCTION
```

### 🔸 Dekripsi

```
FUNCTION dekripsi_caesar(teks, kunci)
    RETURN enkripsi_caesar(teks, -kunci)
END FUNCTION
```

### 🔸 Brute Force

```
FUNCTION brute_force(teks)
    FOR kunci FROM 0 TO 25
        PRINT kunci, dekripsi_caesar(teks, kunci)
    END FOR
END FUNCTION
```

---

## 🧠 Penjelasan Singkat Caesar Cipher

**Caesar Cipher** adalah algoritma kriptografi klasik yang digunakan untuk **menyandikan teks dengan cara menggeser huruf dalam alfabet** sebanyak nilai kunci tertentu.

### 🔐 Cara Kerja

* Setiap huruf digeser maju sejumlah langkah sesuai **kunci (key)**.
* Jika kunci = 3:
  A → D, B → E, C → F, … hingga Z kembali ke A (menggunakan **mod 26**).

### ⚙️ Proses

1. **Enkripsi:** Geser huruf ke kanan sebanyak kunci.
2. **Dekripsi:** Geser huruf ke kiri sebanyak kunci (atau gunakan kunci negatif).
3. **Brute Force:** Coba semua 26 kemungkinan kunci untuk menemukan teks asli.

### 🧮 Contoh

Teks: `HELLO`
Kunci: `3`
Enkripsi → `KHOOR`
Dekripsi → `HELLO`

### 💡 Karakteristik

* Jenis cipher: **Substitusi sederhana**
* Ruang kunci: **26 kombinasi (huruf A–Z)**
* Kompleksitas:

  * Enkripsi/Dekripsi: **O(n)**
  * Brute Force: **O(26n)** = **O(n)**
* **Kelemahan:** Mudah dipecahkan karena ruang kunci kecil.

---

## 📌 Kesimpulan

Caesar Cipher merupakan dasar dari algoritma kriptografi modern.
Meskipun sederhana dan mudah dipecahkan, metode ini efektif untuk **pengenalan konsep enkripsi dan dekripsi**, serta menunjukkan bagaimana data dapat diamankan menggunakan operasi matematis sederhana.

---
