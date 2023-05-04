# Python-Project-Pacmann---Super-Cashier
Project ini dibuat oleh Jusvita sebagai syarat kelulusan program TTS 3 Pacmann

# Background project
Andi merupakan pemilik supermarket besar yang berencana untuk menginovasi bisnisnya. Andi berkeinginan membuat sistem kasir self-service di supermarketnya agar para customer dapat melakukan transaksi jarak jauh tanpa harus datang ke supermarket. Dengan adanya sistem kasir ini akan sangat membantu untuk melakukan transaksi pembelian, update barang dan aktivitas transaksi lainnya di sistem kasir tersebut.

# Objective and Requirements
**Objective**

Membuat sistem kasir self service di supermarket Andi untuk mempermudah transaksi pembelian jarak jauh melalui website/aplikasi yang telah disediakan.

**Requirements**

Adapun beberapa fitur yang digunakan dalam sistem kasir ini yaitu:
1. Menginput dan membuat ID transaksi otomatis.
2. Menginput nama item, jumlah item dan harga setiap item yang ingin dibeli.
3. Melakukan update(perbarui) item jika terdapat kekeliruan dalam menginput data.
4. Melakukan penghapusan item jika tidak jadi membeli item tersebut
5. Melakukan pembatalan(reset all) daftar belanja
6. Melakukan pengecekan daftar belanja
7. Melakukan pembayaran atas transaksi belanja.

# Flowchart

![image](https://user-images.githubusercontent.com/131349719/235947274-3e83a147-4792-4bf0-937a-35d8654ad375.png)

# Penjelasan Kode Program

# Penjelasan Alur Program

# Test Case
Berikut merupakan menu utama yang akan keluar di terminal
![1 welcome menu](https://user-images.githubusercontent.com/131349719/236109727-fd8b9dfe-a0e9-4097-b2e3-905b561bf78e.png)

**Test Case 1**

Customer ingin menambahkan item baru menggunakan method add_item(). Item yang ditambahkan adalah sebagai berikut:

• Nama item: Potato, Qty: 5, Harga: 20000

• Nama item: Susu, Qty: 12, Harga: 15000

• Nama item: Mie, Qty: 24, Harga: 3000

• Nama item: Saos, Qty: 1, Harga: 35000

![2 add item](https://user-images.githubusercontent.com/131349719/236110196-88a3f3ba-2172-4bd7-8aee-1ea0d9ab0d23.png)
Daftar belanja setelah ditambahkan
![3 Check order](https://user-images.githubusercontent.com/131349719/236110215-573f835c-ed98-4d1e-bb41-d3d2f37c0ee5.png)

**Test Case 2**

Ternyata Customer salah menginput nama item (Mie - Mie Goreng) jumlah item  potato dan harga susu yang ingin dibeli, maka Customer dapat menggunakan method update_item_name() update__item_qty() dan update_item_price() untuk memperbarui transaksi tersebut.

Untuk update_item_name()
![4 update item name](https://user-images.githubusercontent.com/131349719/236111456-667cd696-695d-497f-b345-be7c30342954.png)
Untuk update_item_qty()
![6 update item qty](https://user-images.githubusercontent.com/131349719/236111502-f447ccd6-b10a-4cc1-892f-7ada9e26b35a.png)
Untuk update_item_price()
![8 update item price](https://user-images.githubusercontent.com/131349719/236111567-4ff8fa47-a2a4-4c4d-870c-05322de42e6f.png)
Maka setelah diperbarui menjadi
![9 check update item price](https://user-images.githubusercontent.com/131349719/236111612-ec068c02-1797-4fc0-98c3-f481f12dfa7f.png)

**Test Case 3**

Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer dapat menggunakan method delete_item() untuk menghapus item yang dipilih. Item yang ingin dihapus adalah Saos.
![10 delete item](https://user-images.githubusercontent.com/131349719/236111808-c1f98169-fe24-418a-807d-95e54bc1e92a.png)
![11 check delete item](https://user-images.githubusercontent.com/131349719/236111830-f1fcb792-ff67-4695-89ba-8cc788ced582.png)

**Test Case 4**

Ternyata setelah dipikir-pikir, Customer salah memasukkan item yang ingin dibelanjakan. Daripada menghapusnya satu-satu, maka Customer cukup menggunakan method reset_transaction() untuk menghapus semua item yang sudah ditambahkan. Daftar belanja setelah diperbarui:
![13 reset item all](https://user-images.githubusercontent.com/131349719/236111921-231becae-6fda-47f2-ac31-5ead119388de.png)

**Test Case 5**

Setelah Customer selesai berbelanja, maka sistem akan menghitung total belanja yang harus dibayarkan menggunakan method total_payment(). Sebelum mengeluarkan output total akan menampilkan daftar belanja. Daftar belanja ketika melakukan pembayaran:
![12 check total price](https://user-images.githubusercontent.com/131349719/236112022-75cb21a3-c447-453e-9d37-617235a06c5a.png)

# Conclusion
