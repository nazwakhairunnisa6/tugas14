import os

# Membuat folder
folder_name = "nazwa"
os.makedirs(folder_name, exist_ok=True)

# Membuat dan menulis isi file
file_path = os.path.join(folder_name, "nazwa.txt")
with open(file_path, 'w') as file:
    file.write("Nama: Nazwa khairunnisa hakiki\n")
    file.write("Usia: 20\n")
    file.write("Alamat: Sukabumi\n")
    
# Membaca dan menampilkan isi 
with open(file_path, 'r') as file:
    data = file.read()
    print(data)
