import pandas as pd

# Nama file input dan output
input_file = "wa_guyup_rukun_sak_lawase.csv"
output_file = "wa_guyup_rukun_sak_lawase_msg.csv"

# Mengambil fitur Message saja
data = pd.read_csv(input_file)
data = data['Message']

# Menyimpan CSV
data.to_csv(output_file, index=False)
print(f"File telah disaring dan disimpan di {output_file}")