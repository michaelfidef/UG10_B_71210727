RSI = int(input("Masukkan besar RSI: "))
MACD = input("Masukkan kondisi MACD: ")

if (RSI >= 70) and (MACD == "golden-cross"):
    print("RSI lebih dari sama dengan 70 dan MACD Golden-cross, Tunggu MACD sampai Death-cross")
elif (RSI <= 30) and  (MACD == "death-cross"):
    print("RSI kurang dari sama dengan 30 dan MACD Death-cross, Tunggu MACD sampai Golden-cross")
elif (RSI >= 70) and (MACD == "death-cross"):
    print("RSI lebih dari sama dengan 70 dan MACD Death-cross, saatnya jual")
elif (RSI <= 30) and (MACD == "golden-cross"):
    print("RSI kurang dari sama dengan 30 dan MACD Golden-cross, saatnya beli")
elif (RSI >= 70) and (MACD == "golden-cross"):
    print("Tunggu MACD sampai death-cross")
else:
    print("RSI berada di area 30 - 70, Bukan saatnya membeli maupun menjual")

