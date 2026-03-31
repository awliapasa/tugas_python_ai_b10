# 1. List - akses dan manipulasi
myList = ["Hi", 3.14, "Donut", "China", 42, True]
print(myList[:1]) # Menampilkan elemen pertama dengan slicing
print(myList[5:]) # Menampilkan elemen terakhir dengan slicing

print(myList)
myList.append("This is the new element")
print(myList)

print()

print(myList)
myList.insert(0, "inserted element")
print(myList)

print()

print(myList)
myList.extend([34, "Extended", False])
print(myList) 

print()

print(myList)
myList.pop(1)
print(myList)

print()

print(myList)
myList.remove(False)
print(myList)

print()

# 2. Tuple - immutability & unpacking
myTuple = (1, 2, 3, 4, 5, 6, 7, 8)
print(len(myTuple)) 
print(myTuple[2])
(a, b, c, d, e, f, g, h) = myTuple
print(a)
print(e)
print(g)

print()

# 3. Set - keunikan & operasi himpunan
A = {1, 2, 3, 4, 5}
B = {2, 3, 6, 7, 8}

print(A.union(B))               # Gabungan
print(A.intersection(B))        # Irisan/yang sama
print(A.difference(B))          # Ada di A, tapi tidak di B
print(A.symmetric_difference(B)) # tidak di keduanya, tapi ada di salah satu set aja

print()

# 4. Dictionary
student = {
    "nama" : "Aulia Fasya",
    "nim" : "2023105499",
    "angkatan" : "2023",
    "kota" : "Jakarta"
}

# tambah key baru
student["jurusan"] = "Informatika"
print(student)

# ubah nilai key
student.update({"kota" : "Jakarta Timur"})
print(student)

# hapus key
student.pop("jurusan")
print(student)

print(student.keys())   # Menampilkan semua key
print(student.values()) # Menampilkan semua value
print(student.items())  # Menampilkan items

for key, value in student.items():
    print(key, ":", value)

# 5. Nested Structures
daftar_buku = [
    {
        "judul" : "Laut Bercerita",
        "penulis" : "Leila S. Chudori"      ,
        "tahun"   : 2017
    },
    {
        "judul" : "Hujan",
        "penulis" : "Tere Liye",
        "tahun" : 2016
    },
    {
        "judul" : "Shatter Me",
        "penulis" : "Tahereh Mafi",
        "tahun" : 2011
    },
    {
        "judul" : "Ignite Me",
        "penulis" : "Tahereh Mafi",
        "tahun" : 2013
    },
    {
        "judul" : "Restore Me",
        "penulis" : "Tahereh Mafi",
        "tahun" : 2014
    }
]

for buku in daftar_buku:
    print(buku["judul"])

list_buku_2015_ke_atas = []
for buku in daftar_buku:
    if int(buku["tahun"]) >= 2015:
        list_buku_2015_ke_atas.append(buku["judul"])
        
print(list_buku_2015_ke_atas)

print()

# 6. Comprehension & utilitas
# - List comprehension
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 
                   12, 23, 14, 15, 16, 17, 18, 19, 20]

list_genap = [x for x in list_of_numbers if x % 2 == 0]
print(list_genap)

list_kuadrat = [x**2 for x in list_of_numbers]
print(list_kuadrat)

print()

# - Dictionary comprehension
num = {
    angka: "genap" if angka % 2 == 0 else "ganjil" for angka in range(1, 11)
}
print(num)

print()

# - Set comprehension
# huruf unik (lowercase) dari sebuah kalimat.
kalimat = "Selamat Idul Fitri"
huruf_unik = {kecil for kecil in kalimat if kecil.islower()}
print(huruf_unik)

print()

# 7. Keanggotaan & pencarian sederhana
buah = ["anggur", "duku", "kelengkeng", "jambu"]

if "kelengkeng" in buah:
    print("Buah kelengkeng masih ada!")

print("Index posisi kelengkeng: ", buah.index("kelengkeng"))
