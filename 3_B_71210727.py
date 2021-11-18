bil1 = float(input("Masukan bilangan pertama: "))
bil2 = float(input("Masukan bilangan kedua: "))
kal = input("Masukan kalimat: ")

if "kali" in kal:
    print("Hasil perkalian", bil1, "dengan", bil2, "adalah", bil1*bil2)
elif "kurang" in kal:
    print("Hasil pengurangan", bil1, "dengan", bil2, "adalah", bil1-bil2)
elif "bagi" in kal:
    print("Hasil pembagian", bil1, "dengan", bil2, "adalah", bil1/bil2)
elif "tambah" in kal:
    print("Hasil penjumlahan", bil1, "dengan", bil2, "adalah", bil1+bil2)
else:
    print("Data yang anda masukan salah")