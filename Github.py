import pandas as pd
import json

# Baca file JSON
with open("AISYAH NURUL ILMI PRIANTO_V3925018_TIB (2).JSON", "r", encoding="utf-8") as file:
    data = json.load(file)

# Tampilkan tabel untuk setiap bagian
print("\n=== DATA MASYARAKAT ===")
df_masyarakat = pd.DataFrame(data["Masyarakat"])
print(df_masyarakat.to_string(index=False))

print("\n=== DATA INSTANSI PEMERINTAH ===")
df_instansi = pd.DataFrame(data["Instansi_Pemerintah"])
print(df_instansi.to_string(index=False))

print("\n=== DATA MEDIA TERPERCAYA ===")
df_media = pd.DataFrame(data["Media_Terpercaya"])
print(df_media.to_string(index=False))

print("\n=== DATA BIG DATA PUBLIK ===")
df_bigdata = pd.DataFrame(data["BIG Data Publik"])
print(df_bigdata.to_string(index=False))
