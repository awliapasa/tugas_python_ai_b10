# Function
def greet(nama: str) -> str:
    return f"Halo, {nama}!"
# print(greet("Naya"))
print()

def tambah(a: float, b: float = 0.0) -> float:
    return a + b
# print(tambah(10, 10))
print()

def rata_rata(angka: list[float]) -> float:
    if len(angka) == 0:
        return 0.0
    return sum(angka)/len(angka)
# print(rata_rata([5, 5, 2.5, 0]))
# print(rata_rata([]))
print()

# Class
class student:
    def __init__(self, nama: str, nim: str, nilai: list[float]):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)
        
    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold: return "LULUS"
        else: return "TIDAK LULUS"

    def __str__(self) -> str:
        return f"nama={self.nama}, nim={self.nim}, rata={self.rata_nilai()}, status={self.status()}"
    
student1 = student('Budi', 'A123', [80, 90, 68])
print(student1)

print("=== FUNCTIONS === dan == CLASS STUDENT ===")
print(greet("Arifian"))
print(tambah(5, 7))
print(tambah(10))
print(rata_rata([80, 90, 100]))
print(rata_rata([]))

student2 = student('Arif', 'B234', [77, 98, 45])
student2.tambah_nilai(85)
print(student2)
print(student2.rata_nilai())
print(student2.status())

student3 = student('Cinthia', 'C456', [88, 76, 90])
student3.tambah_nilai(75)
print(student3)
print(student3.rata_nilai())    
print(student3.status())    
