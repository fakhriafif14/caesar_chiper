import time
import sys
import string

def enkripsi_caesar(teks, kunci):
    """
    Enkripsi teks menggunakan Caesar Cipher
    
    Args:
        teks (str): Teks yang akan dienkripsi
        kunci (int): Kunci pergeseran (0-25)
    
    Returns:
        str: Teks terenkripsi
    """
    hasil = ""
    
    for char in teks:
        if char.isupper():
            # Enkripsi huruf kapital
            hasil += chr((ord(char) + kunci - 65) % 26 + 65)
        elif char.islower():
            # Enkripsi huruf kecil
            hasil += chr((ord(char) + kunci - 97) % 26 + 97)
        else:
            # Karakter selain huruf tidak dienkripsi
            hasil += char
    
    return hasil


def dekripsi_caesar(teks, kunci):
    """
    Dekripsi teks yang dienkripsi dengan Caesar Cipher
    
    Args:
        teks (str): Teks terenkripsi
        kunci (int): Kunci pergeseran (0-25)
    
    Returns:
        str: Teks terdekripsi
    """
    # Dekripsi adalah enkripsi dengan kunci negatif
    return enkripsi_caesar(teks, -kunci)


def brute_force_caesar(teks_terenkripsi):
    """
    Brute force attack untuk menemukan semua kemungkinan dekripsi
    dengan fokus pada hasil yang bisa dibaca manusia.
    """
    hasil_brute_force = []
    kemungkinan_bisa_dibaca = []
    
    print("=" * 60)
    print("BRUTE FORCE ATTACK - MENCARI KEMUNGKINAN DEKRIPSI")
    print("=" * 60)
    
    # Daftar kata umum dalam Bahasa Indonesia untuk verifikasi
    common_words = ['yang', 'di', 'ke', 'dari', 'pada', 'dalam', 'untuk', 'dengan', 
                   'dan', 'atau', 'ini', 'itu', 'juga', 'ada', 'akan', 'bisa', 
                   'serang', 'pagi', 'siang', 'malam', 'penyerangan']
    
    # Animasi loading
    loading_chars = "⣾⣽⣻⢿⡿⣟⣯⣷"
    
    for kunci in range(26):
        # Tampilkan animasi
        sys.stdout.write(f"\rMencoba kunci {kunci:2d} {loading_chars[kunci % len(loading_chars)]} ")
        sys.stdout.flush()
        time.sleep(0.2)
        
        teks_dekripsi = dekripsi_caesar(teks_terenkripsi, kunci)
        hasil_brute_force.append((kunci, teks_dekripsi))
        
        # Cek apakah hasil dekripsi mengandung kata-kata yang masuk akal
        words = teks_dekripsi.lower().split()
        matches = sum(1 for word in words if word in common_words)
        
        if matches > 0:  # Jika ada kata yang cocok dengan daftar kata umum
            readability_score = (matches / len(words)) * 100
            kemungkinan_bisa_dibaca.append((kunci, teks_dekripsi, readability_score))
    
    # Hapus baris loading
    sys.stdout.write('\r' + ' ' * 50 + '\r')
    sys.stdout.flush()
    
    # Tampilkan semua hasil
    print("\nHasil semua kemungkinan dekripsi:")
    print("-" * 60)
    for kunci, teks_dekripsi in hasil_brute_force:
        print(f"Kunci {kunci:2d}: {teks_dekripsi}")
    
    # Tampilkan hasil yang kemungkinan bisa dibaca
    if kemungkinan_bisa_dibaca:
        print("\n" + "=" * 60)
        print("HASIL YANG BISA DIBACA MANUSIA:")
        print("=" * 60)
        for kunci, teks, score in sorted(kemungkinan_bisa_dibaca, 
                                       key=lambda x: x[2], reverse=True):
            print(f"Kunci {kunci:2d} (match score: {score:.1f}%):")
            print(f"→ {teks}")
            print("-" * 60)
    else:
        print("\nTidak ditemukan hasil yang mudah dibaca.")
    
    return hasil_brute_force


def main():
    print("\n")
    print("█▀▀ ▄▀█ █▀▀ █▀ ▄▀█ █▀█   █▀▀ █ █▀█ █░█ █▀▀ █▀█")
    print("█▄▄ █▀█ ██▄ ▄█ █▀█ █▀▄   █▄▄ █ █▀▀ █▀█ ██▄ █▀▄")
    print("=" * 60)
    
    
    while True:
        print("\nPilih menu:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Brute Force Attack")
        print("4. Keluar")
        
        pilihan = input("\nMasukkan pilihan (1-4): ")
        
        if pilihan == "1":
            teks = input("\nMasukkan teks yang akan dienkripsi: ")
            kunci = int(input("Masukkan kunci (0-25): "))
            
            hasil = enkripsi_caesar(teks, kunci)
            print(f"\nTeks asli    : {teks}")
            print(f"Kunci        : {kunci}")
            print(f"Hasil enkripsi: {hasil}")
            
        elif pilihan == "2":
            teks = input("\nMasukkan teks terenkripsi: ")
            kunci = int(input("Masukkan kunci (0-25): "))
            
            hasil = dekripsi_caesar(teks, kunci)
            print(f"\nTeks terenkripsi: {teks}")
            print(f"Kunci           : {kunci}")
            print(f"Hasil dekripsi  : {hasil}")
            
        elif pilihan == "3":
            teks = input("\nMasukkan teks terenkripsi untuk brute force: ")
            brute_force_caesar(teks)
            
        elif pilihan == "4":
            print("\nTerima kasih telah menggunakan program ini!")
            break
            
        else:
            print("\nPilihan tidak valid!")


# Contoh penggunaan
if __name__ == "__main__":
    # Demo otomatis
    print("\n" + "=" * 60)
    print("DEMO OTOMATIS")
    print("=" * 60)
    
    teks_asli = "Hello World"
    kunci_demo = 3
    
    print(f"\nTeks asli: {teks_asli}")
    print(f"Kunci: {kunci_demo}")
    
    # Enkripsi
    teks_enkripsi = enkripsi_caesar(teks_asli, kunci_demo)
    print(f"Hasil enkripsi: {teks_enkripsi}")
    
    # Dekripsi
    teks_dekripsi = dekripsi_caesar(teks_enkripsi, kunci_demo)
    print(f"Hasil dekripsi: {teks_dekripsi}")
    
    # Brute Force
    print(f"\n\nBrute Force pada '{teks_enkripsi}':")
    brute_force_caesar(teks_enkripsi)
    
    # Jalankan program interaktif
    print("\n" + "=" * 60)
    main()