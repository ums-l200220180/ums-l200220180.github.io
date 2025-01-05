import csv
import re
import math

# Nama file input dan output
input_file = "wa_guyup_rukun_sak_lawase_msg.csv"
output_file = "wa_guyup_rukun_sak_lawase_clean.csv"

# Pola regex untuk huruf, angka, dan tanda baca-tulis umum
clean_pattern = r"[^\w\s.,!?;:'\"()\-\/@]"

def clean_text(text):
    """
    Membersihkan teks dari karakter yang tidak diinginkan.
    """
    return re.sub(clean_pattern, "", text)

def is_valid_row(row):
    """
    Mengecek apakah baris valid (tidak ada NaN dan tidak mengandung 'media omitted').
    """
    for cell in row:
        if cell is None or cell == "" or (isinstance(cell, float) and math.isnan(cell)):
            return False
        if "media omitted" in cell.lower():
            return False
    return True

# Membaca file CSV asli dan membersihkan datanya
with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Menyalin header
    headers = next(reader)
    writer.writerow(headers)

    # Membersihkan setiap baris data
    for row in reader:
        if is_valid_row(row):  # Hanya memproses baris valid
            cleaned_row = [clean_text(cell) for cell in row]
            writer.writerow(cleaned_row)

print(f"File telah dibersihkan dan disimpan di {output_file}")

