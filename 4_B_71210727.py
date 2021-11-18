a = int(input("Masukkan angka: "))

if (a % 2 == 0) and (a % 3 != 0):
    hasil1 = "YA"
    if (a % 5 != 0) or (a % 10 == 0):
        hasil2 = "IYA DONG"
    elif (a % 5 == 0) and (a % 10 != 0):
        hasil2 = "TIDAK"
    print("Bilangan tersebut habis dibagi 2 dan tidak habis dibagi 3? Jawab: ", hasil1)
    print("Apakah Bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: ", hasil2)
else:
    print("Bilangan tersebut tidak habis dibagi 2 dan habis dibagi 3. Program dihentikan ")