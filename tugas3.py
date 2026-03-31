# 1. Deklarasi Variabel dan Tipe Data

# - Tipe Data String
name = "Aulia"
print(name)

# - Tipe Data Integer
age = 20
print(age)

# - Tipe Data Float
height = 1.59
print(height)

# - Tipe Data Boolean
lives_in_jakarta = True
print(lives_in_jakarta)

# - Tipe Data List
fav_fruits = ["grape", "pear", "melon"]
print(fav_fruits)

# 2. Manipulasi String
first_name = "Aulia"
last_name = "Fasya"
full_name = first_name + " " + last_name
print(full_name)
print(len(full_name))
print(full_name.upper())
print(full_name.lower())

# 3. Operasi Matematika Sederhana
print(805 + 100)
print(805 - 100)
print(200 * 2)
print(100 / 50)
print(20 // 3)
print(20 % 3)

# 4. List dan Akses Elemen
indonesia_cities = ["Jakarta", "Yogyakarta", "Bandung"]
print(indonesia_cities[2])

indonesia_cities.append("Ambon")
print(indonesia_cities)

indonesia_cities.remove("Yogyakarta")
print(indonesia_cities)

indonesia_cities.pop(0)
print(indonesia_cities)

# 5. Penggunaan Input dari User
user_name = input("Masukkan nama Anda: ")
user_age = input("Masukkan umur Anda: ")
print("Halo, nama saya " + user_name 
      + " dan umur saya " + user_age + " tahun.")
