#Import library yang dipakai dalam cashier.py
from tabulate import tabulate
from validation import validate_add, validate_update_name, validate_update_price, validate_update_qty


class Transaction:
    #Membuat kelas dan method untuk transaksi yang termasuk nama item, quantity, dan harga
    data = {}

    def __init__(self):
        self.items = {}

    def add_item(self):
        #Berfungsi untuk menambahkan item baru ke transaksi dan menggunakan validate_add untuk memvalidasi item yang ditambahkan sesuai kriteria
        name, quantity, item_price = validate_add()      
        self.items[name] = {"quantity": quantity, "item_price": item_price, "total_item_price": quantity * item_price}

    def delete_item(self):
        #Berfungsi untuk menghapus item berdasarkan nama item yang telah dimasukkan dan menggunakan try except untuk memvalidasi jika item yang dimasukkan tidak ada.
        name = input("Enter name item you want delete: ")
        try:
            del self.items[name]
            print("delete success!")
        except KeyError:
            print(f"There is item no {name} in the bucket")
        
    def reset_item(self):
        #Berfungsi untuk menghapus semua data item dan menggunakan try except untuk memvalidasi tidak ada data
        try:
            if(len(self.items) != 0):
                print("Clearing all item")
                self.items.clear()
                print("All item success deleted!")
            else:    
                raise ValueError
        except ValueError:
            print("There is no item to be deleted")

    def update_item_name(self):
        #Berfungsi untuk memperbarui nama item berdasarkan item yang telah ada di transaksi dan menggunakan validate_update_name untuk menyesuaikan sesuai kriteria dan mencegah ambiguitas item. Menggunakan try except untuk memvalidasi jika item tersebut tidak ada didalam transaksi.
        if(len(self.items) != 0):
            try:
                old_name, new_name = validate_update_name()
                if old_name in self.items:
                    self.items[new_name] = self.items.pop(old_name)
                else: 
                    raise ValueError
            except ValueError:
                print(f"There is no item name {old_name} the transaction")
        else:
            print("Please add item first")
    
    def update_item_qty(self):
        #Berfungsi untuk memperbarui quantity(jumlah) item yang telah ada di dalam transaksi dan menggunakan validate_update_qty untuk mencegah item yang ambigu dan menggunakan try except untuk memvalidasi apakah item tersebut ada di dalam transaksi. Jika benar akan dijumlahkan di total belanja.
        if(len(self.items) != 0):
            try:
                name, quantity = validate_update_qty()
                if name in self.items:
                    self.items[name]['quantity'] = quantity
                    self.items[name]['total_item_price'] = quantity * self.items[name]['item_price']
                else:
                    raise ValueError
            except ValueError:
                print("No item on the transaction")
        else:
            print("Please add item first")

    def update_item_price(self):
        #Berfungsi untuk memperbarui price(harga) item yang telah ada di dalam transaksi dan menggunakan validate_update_price untuk mencegah item yang ambigu dan menggunakan try except untuk memvalidasi apakah item tersebut ada di dalam transaksi. Jika benar akan dijumlahkan di total belanja. 
        if(len(self.items) != 0):
            try:
                name, price = validate_update_price()
                if name in self.items:
                    self.items[name]['item_price'] = price
                    self.items[name]['total_item_price'] = price * self.items[name]['quantity']
                else:
                    raise ValueError
            except ValueError:
                print("No item on the transaction")
        else:
            print("please add item first")

    def total_price(self):
        #Berfungsi untuk menghitung total harga semua item dan akan memperoleh diskon jika total harga sesuai dengan ketentuan dari diskon.
        total_price = 0
        discount = 0
        if(len(self.items) != 0):
            for keys, _ in self.items.items():
                total_price += int(self.items[keys]["total_item_price"])
            
            if total_price > 200_000 and total_price <= 300_000:
                discount = int(0.05 * total_price)
            elif total_price > 300_000 and total_price <= 500_000:
                discount = int(0.08 * total_price)
            elif total_price > 500_000:
                discount = int(0.1 * total_price)
            else:
                pass
            self.check_order()
            print(f"Your price before discount {total_price}, you got discount {discount} and total price is {total_price - discount}")
        else:
            print('No item to calculate the price')

    
    def check_order(self):
        #Membuat tabel yang menunjukan semua item yang telah dimasukkan dan akan mengeluarkan tabel kosong jika datanya kosong. Menggunakan module tabulate agar tampilannya lebih rapi
        item_to_attribute = {}
        list_item = []

        for keys_1, keys_2 in self.items.items():
            item_to_attribute['product name'] = keys_1
            item_to_attribute['quantity'] = keys_2['quantity']
            item_to_attribute['item_price'] = keys_2['item_price']
            item_to_attribute['total_item_price'] = keys_2['total_item_price']

            #need to append a copy, otherwise it just adding references to the same dictionary over and over again
            list_item.append(item_to_attribute.copy())

        if(len(list_item) != 0):
            print('=' * 10,"List of items in this transaction",'=' * 10)
            print(tabulate(list_item,headers="keys", tablefmt="simple_grid"))
        else:
            print("There is no items in the bucket")