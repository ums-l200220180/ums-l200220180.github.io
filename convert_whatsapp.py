import csv
import re

# Nama file input dan output
input_file = "wa_guyup_rukun_sak_lawase.txt"
output_file = "wa_guyup_rukun_sak_lawase.csv"

# Pola regex untuk pesan WhatsApp
pattern = r"(\d{1,2}/\d{1,2}/\d{2,4}), (\d{2}:\d{2}) - (.+?): (.+)"
system_pattern = r"(\d{1,2}/\d{1,2}/\d{2,4}), (\d{2}:\d{2}) - (.+)"

# Membaca file teks
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Menulis ke file CSV
with open(output_file, "w", encoding="utf-8", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Date", "Time", "Sender/Info", "Message"])  # Header CSV

    for line in lines:
        line = line.strip()  # Menghapus spasi putih di awal/akhir
        if match := re.match(pattern, line):  # Jika cocok dengan pesan biasa
            date, time, sender, message = match.groups()
            writer.writerow([date, time, sender, message])
        elif match := re.match(system_pattern, line):  # Jika cocok dengan pesan sistem
            date, time, info = match.groups()
            writer.writerow([date, time, info, ""])
        else:  # Jika baris tidak cocok, kemungkinan kelanjutan pesan sebelumnya
            if line:  # Hanya jika baris tidak kosong
                writer.writerow(["", "", "", line])

print(f"File telah dikonversi ke {output_file}")