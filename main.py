# Dictionary berisi opsi pilihan makanan/minuman dan harganya
menu = {
    "Nasi Goreng telur": 12000,
    "Mie nyemek": 10000,
    "Ayam Goreng": 58000,
    "Es Teh manis": 5000,
    "Es Jeruk": 5000,
    "Teh Pucuk": 3000
}

def tampilkan_menu():
    print("Menu Makanan/Minuman:")
    for item, harga in menu.items():
        print(f"{item}: Rp {harga}")

def hitung_total(pesanan):
    total = 0
    for item in pesanan:
        total += menu.get(item, 0)
    return total

def main():
    pesanan = []
# Mulai Transaksi
    print("Selamat datang di Kantin selalu kenyang")
    tampilkan_menu()

    while True:
        pilihan = input("\nMasukkan nama makanan/minuman yang ingin dipesan (ketik 's' untuk mengakhiri): ")
        
        if pilihan.lower() == 's':
            break
        elif pilihan in menu:
            pesanan.append(pilihan)
        else:
            print("Maaf, pilihan tidak valid. Silakan pilih lagi.")

    total_harga = hitung_total(pesanan)

    # Tampilkan struk pembelian
    print("\n--- Struk Pembelian ---")
    for item in pesanan:
        print(f"{item}: Rp {menu[item]}")

    print("-----------------------")
    print(f"Total Harga: Rp {total_harga}")
    print("Terima kasih atas pembelian Anda!")

if __name__ == "__main__":
    main()