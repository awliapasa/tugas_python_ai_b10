import numpy as np
import pandas as pd
import os
np.random.seed(42)

arr_nilai = np.array([80, 90, 68, 75, 75, 
                      88, 78, 90, 50, 95])

# rata-rata
rata_rata = np.mean(arr_nilai)
print("Rata-rata nilai:", rata_rata)

# median
median = np.median(arr_nilai)
print("Median nilai: ", median)

# standar deviasi
std_deviasi = np.std(arr_nilai)
print("Standar Deviasi: ", std_deviasi)

# nilai min
nilai_min = np.min(arr_nilai)
print("Nilai minimum: ", nilai_min)

# nilai max
nilai_max = np.max(arr_nilai)
print("Nilai maksimum: ", nilai_max)

# Membuat DataFrame
df = pd.DataFrame({
    "nama": ["Budi", "Arif", "Cinthia", "Aulia", "Rio",
             "Andi", "Yogi", "Lala", "Wildan", "Yu"],
    "nim" : ["A123", "B234", "C456", "A230", "B453",
             "C890", "A120", "B762", "C901", "B434"],
    "nilai" : arr_nilai
})

# Menambahkan kolom status
df["status"] = np.where(df["nilai"] >= 70, "LULUS", "TIDAK LULUS")

# Menampilkan 5 baris pertama
print(df.head())

jumlah_baris = len(df)
jumlah_lulus = (df["status"] == "LULUS").sum()
jumlah_tidak_lulus = (df["status"] == "TIDAK LULUS").sum()

# File I/O 
with open("ringkasan_tugas6.txt", "w") as f:
    f.write("=== RINGKASAN STATISTIK NILAI ===\n")
    f.write(f"Rata-rata nilai: {rata_rata}\n")
    f.write(f"Median nilai: {median}\n")
    f.write(f"Standar Deviasi: {std_deviasi}\n")
    f.write(f"Nilai minimum: {nilai_min}\n")
    f.write(f"Nilai maksimum: {nilai_max}\n")
    f.write("\n")
    f.write("=== RINGKASAN DATAFRAME ===\n")
    f.write(f"Jumlah data: {jumlah_baris}\n")
    f.write(f"Jumlah lulus: {jumlah_lulus}\n")
    f.write(f"Jumlah tidak lulus: {jumlah_tidak_lulus}\n")

# Membuat class GradeBook
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    def average(self) -> float:
        return self.df["nilai"].mean()
    
    def pass_rate(self, threshold: float = 70.0) -> float:
        lulus = (self.df["nilai"] >= threshold).sum()
        total = len(self.df)
        return (lulus/total)*100
    
    def save_summary(self, path: str):
        avg = self.average()
        pass_rate = self.pass_rate()

        with open(path, "a") as f:
            f.write("\n=== RINGKASAN GRADEBOOK ===\n")
            f.write(f"Jumlah data: {len(self.df)}\n")
            f.write(f"Rata-rata nilai: {avg:.2f}\n")
            f.write(f"Persentase lulus: {pass_rate:.2f}%\n")

    def __str__(self) -> str:
        return f"GradeBook(jumlah_data={len(self.df)}, rata-rata={self.average():.2f})"
    
# Demo
if __name__ == "__main__":

    print("=== NUMPY ===")
    print("Rata-rata: ", rata_rata)
    print("Median: ", median)
    print("Standar Deviasi: ", std_deviasi)
    print("Min: ", nilai_min)
    print("Max: ", nilai_max)

    print("\n=== PANDAS ===")
    print(df.head())

    print("\n=== OOP: GRADEBOOK ===")

    gb = GradeBook(df)
    print(gb)
    print("Rata-rata nilai dari GradeBook: ", gb.average())
    print("Persentase Lulus dari GradeBook: ", gb.pass_rate(), "%")

    gb.save_summary("ringkasan_tugas6.txt")