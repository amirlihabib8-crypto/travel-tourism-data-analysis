import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv("Travel And Tourism.csv")

print("=== 1. ÜMUMİ MƏLUMAT VƏ STRUKTUR ===")
print(df.info())
print("\n" + "=" * 40 + "\n")

print("=== 2. YAŞ VƏ CİNSİYYƏT PAYLANMASI ===")
print("Cinsiyyət faizləri:")
print(df["Gender"].value_counts(normalize=True) * 100)
print("\nYaş statistikası:")
print(df["Customer_Age"].describe())
print("\n" + "=" * 40 + "\n")

print("=== 3. İSTİQAMƏTLƏR (ŞƏHƏR VƏ ÖLKƏ) ===")
print("Top 5 Destination Country:")
print(df["Destination_Country"].value_counts().head(5))
print("\nTop 5 Destination City:")
print(df["Destination_City"].value_counts().head(5))
print("\n" + "=" * 40 + "\n")

print("=== 4. SƏYAHƏT MÜDDƏTİ VƏ QRUP TƏRKİBİ ===")
print("Orta gecələmə sayı (Number_of_Nights):", df["Number_of_Nights"].mean())
print("Orta böyük sayı (Number_of_Adults):", df["Number_of_Adults"].mean())
print("Orta uşaq sayı (Number_of_Children):", df["Number_of_Children"].mean())
print("\n" + "=" * 40 + "\n")

print("=== 5. MALİYYƏ VƏ XƏRC ANALİZİ ===")
print(df["Total_Trip_Cost"].describe())
print("\n" + "=" * 40 + "\n")

print("=== 6. OTEL VƏ MÜŞTƏRİ REYTİNQLƏRİ ===")
print("Hotel Rating Paylanması:")
print(df["Hotel_Rating"].value_counts().head(5))
print("\nCustomer Rating Paylanması:")
print(df["Customer_Rating"].value_counts().head(5))



print(
    "\n[INFO] Bütün konsol məlumatları çıxarıldı. İndi qrafik ekrana gətirilir..."
)

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 5))

# İlk 5 otelin reytinqini qrafikə çıxaraq
top_hotels = df.head(5)
plt.bar(top_hotels["Hotel_Name"], top_hotels["Hotel_Rating"], color="teal")

plt.title("İlk 5 Otelin Reytinqi", fontsize=14, fontweight="bold")
plt.xlabel("Otel Adı", fontsize=12)
plt.ylabel("Reytinq", fontsize=12)
plt.xticks(rotation=30, ha="right")
plt.tight_layout()



plt.show()