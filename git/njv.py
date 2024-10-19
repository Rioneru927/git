import os
import random
import string

data = dict()


def random_food():
    foods = ['Pizza', 'Burger', 'Sushi', 'Pasta', 'Salad','kentang','nasi padang','kipas angin']
    return random.choice(foods)

def random_quantity():
    return random.randint(1, 6)

def random_name_order():
    names = ['asep', 'Boby', 'Clara', 'David', 'Emmanuel','lionel','atsal','fatan','ridho','rafi ahmad','denil','monic','vito','shawki ','timoty']
    return random.choice(names)

while True:
    os.system("cls")  
 
    print(f" {'ORDER MAKANAN':_^45}")
    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range(3))  
    nama_pemesan = input("Enter nama pemesan\t: ")
    jumlah_makanan = input("Enter jumlah makanan\t: ")
    makanan = input("Enter makanan apa\t: ")
    
   
    data[keyFinal] = { 'namakey': nama_pemesan, 'jumlahkey': jumlah_makanan, 'makanankey': makanan }
    
    #lionel membuat random code
    data[f"lio-{keyFinal}"] = { 'namakey': random_name_order(), 'jumlahkey': random_quantity(), 'makanankey': random_food() }
    data[f"lil-{keyFinal}"] = { 'namakey': random_name_order(), 'jumlahkey': random_quantity(), 'makanankey': random_food() }
    data[f"lol-{keyFinal}"] = { 'namakey': random_name_order(), 'jumlahkey': random_quantity(), 'makanankey': random_food() }
    data[f"lel-{keyFinal}"] = { 'namakey': random_name_order(), 'jumlahkey': random_quantity(), 'makanankey': random_food() }
    data[f"lal-{keyFinal}"] = { 'namakey': random_name_order(), 'jumlahkey': random_quantity(), 'makanankey': random_food() }
    
    opsi = input(" ada yang mau dipesan lagi  (y/t) : ").lower()
    if opsi == 't':
        break

# Print final data
print("-" * 60)
print(f"Key\t Nama Pemesan\t Jumlah\t\t Makanan")
print("-" * 60)
for key, value in data.items():
    print(f"{key}\t {value['namakey']}\t {value['jumlahkey']}\t\t {value['makanankey']}")


