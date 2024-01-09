# project-UAS
## PROJECT UAS
| Variable | Isi |
| -------- | --------------------- |
| **Nama** | LUTPIAH AINUS SHIDDIK |
| **NIM** | 312310474 |
| **Kelas** | TI.23.A.5 |
| **Mata Kuliah** | Bahasa Pemrograman |


Buatlah program kasir di sebuah kantin, dengan kondisi berikut:
• List opsi pilihan makanan/minuman dan aksi, bisa menggunakan
format dictionary
• Program harus meminta input pilihan makanan dari pengguna.
• Program harus menghitung total harga makanan yang dipesan.
• Program harus menampilkan struk pembelian.

Program Python tersebut merupakan program kasir sederhana yang dapat digunakan untuk mencatat transaksi pembelian makanan dan minuman di kantin. Program ini memiliki beberapa fitur, yaitu:

Menampilkan daftar menu makanan dan minuman beserta harganya
Menerima input dari pengguna untuk memilih menu yang ingin dibeli
Menghitung total harga pembelian
Menampilkan struk pembelian

Fungsi tampilkan_menu()

Fungsi ini digunakan untuk menampilkan daftar menu makanan dan minuman beserta harganya. Fungsi ini menggunakan perulangan for untuk menampilkan setiap item dalam dictionary menu.

```phython
def tampilkan_menu():
  print("Menu Makanan/Minuman:")
  for item, harga in menu.items():
    print(f"{item}: Rp {harga}")
```
Fungsi hitung_total()

Fungsi ini digunakan untuk menghitung total harga pembelian. Fungsi ini menggunakan perulangan for untuk menjumlahkan harga setiap item yang dipesan.

```phython
def hitung_total(pesanan):
  total = 0
  for item in pesanan:
    total += menu.get(item, 0)
  return total
```
Fungsi main()

Fungsi ini merupakan fungsi utama program. Fungsi ini memulai transaksi dengan menampilkan pesan selamat datang dan daftar menu. Kemudian, fungsi ini menerima input dari pengguna untuk memilih menu yang ingin dibeli. Jika pengguna memilih untuk mengakhiri transaksi, fungsi ini akan keluar dari perulangan. Setelah itu, fungsi ini menghitung total harga pembelian dan menampilkan struk pembelian.
```phython
def main():
  pesanan = []

  # Mulai Transaksi
  print("Selamat datang di Kantin selalu lapar")
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

if name == "__main__":
  main()
```
TERIMAKASIH 
