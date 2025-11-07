import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r'c:\KELAS XI\ARTIFICIAL INTELLEGENCE - PAK ARIFIN\data\nilai_siswa.csv'
data = pd.read_csv(file_path)

print("Informasi Dataset:")
data.info()
print("\n")

print("5 Data Pertama:")
print(data.head())
print("\n")

print("Statistik Deskriptif:")
print(data.describe())
print("\n")

print("Statistik Nilai:")
print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])
print("\n")

print("Nilai Matematika:")
matematika = data[data['Mapel'] == 'Matematika']
print(matematika)
print("\n")

print("Nilai Bahasa Inggris:")
b_inggris = data[data['Mapel'] == 'Bahasa Inggris']
print(b_inggris)
print("\n")

print("Nilai Bahasa Indonesia:")
b_indonesia = data[data['Mapel'] == 'Bahasa Indonesia']
print(b_indonesia)
print("\n")

print("Nilai Produktif:")
produktif = data[data['Mapel'] == 'Produktif']
print(produktif)
print("\n")

print("Nilai Fisika:")
fisika = data[data['Mapel'] == 'Fisika']
print(fisika)
print("\n")

print("Nilai Maksimum dan Minimum per Mata Pelajaran:")
nilai_extrem = data.groupby('Mapel')['Nilai'].agg(['max','min'])
print(nilai_extrem)
print("\n")

print("Membuat Grafik Batang Rata-Rata Nilai...")
rata = data.groupby('Mapel')['Nilai'].mean()
plt.figure(figsize=(10, 6))
rata.plot(kind='bar', color=['skyblue', 'lightgreen', 'coral', 'gold', 'violet'])
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

print("Membuat Diagram Boxplot Sebaran Nilai...")
plt.figure(figsize=(10, 6))
sns.boxplot(x='Mapel', y='Nilai', data=data, palette='Set2')
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("Analisis selesai!")