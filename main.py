#import modul dan library yang akan digunakan
import cashier
import uuid
import datetime as dt

#Membuat objek transaksi dan tanggal
hari_ini = dt.date.today()
trnsct_123 = cashier.Transaction()

def random_trnsct_id(string_length=10):
    #Membuat ID transaksi di setiap transaksi dengan menggunakan modul UUID dengan panjang maksimum 10 karakter dan angka
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-","")
    return random[0:string_length]

id_transaction = random_trnsct_id()

#Membuat tampilan menu utama
def main_menu():
    '''create menu for user and use every method in object trnsct_123 
    '''
    print()
    print("=" * 14, "MAIN MENU CASHIER", "=" * 14)
    print(" " * 13, "WELCOME TO JV STORE\n")
    print(" "*3, "=" * 3 ,f"Your transaction id is {id_transaction}", "=" * 3," "*3, "\n")
    print(f"                 {hari_ini}")
    print("=" * 7, "Please enter one of the option", "=" * 8)
    print("1. Add new item")
    print("2. Update item name")
    print("3. Update item quantity")
    print("4. Update item price")
    print("5. Delete item")
    print("6. Reset transaction")
    print("7. Check order")
    print("8. Check total price")
    print("9. Exit")
    
    while True:
        # input pilihan
        try:
            pilihan = input("Choose menu: ")

            # pilihan menu
            if pilihan == '1':
                trnsct_123.add_item()
                main_menu()
            elif pilihan == '2':
                trnsct_123.update_item_name()
                main_menu()
            elif pilihan == '3':
                trnsct_123.update_item_qty()
                main_menu()
            elif pilihan == '4':
                trnsct_123.update_item_price()
                main_menu()
            elif pilihan == '5':
                trnsct_123.delete_item()
                main_menu()
            elif pilihan == '6':
                trnsct_123.reset_item()
                main_menu()
            elif pilihan == '7':
                trnsct_123.check_order()
                main_menu()
            elif pilihan == '8':
                trnsct_123.total_price()
                main_menu()
            elif pilihan == '9':
                print("Program exit")
                exit()
            else:
                raise ValueError
        except ValueError:
            print("Input according to menu")

main_menu()
