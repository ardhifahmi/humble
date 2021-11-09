"""
Semua sintaksi basah pemogramman
1. Sikuensial : Langkah berurutan
2. Percabangan : Langkah melompat jika kondisi terpenuhi
3. Perulangan : Mengulang langkah yang sama berkali-kali sampai kondisi terpenuhi
"""
print ('ibu berkata, "pergi ke toko"')
print ('budi menjawab, "apa yang saya harus lakukan di toko"')
print ('ibu menjawab, "beli satu botol susu, dan jika ada telur beli 6"')
print ("maka budi berangkat ke toko")
print ("dan mulai berbelanja")


# Percabangan

jumlah_botol_susu = 173
jumlah_telur = 1587

print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah butir telur {jumlah_telur} butir")

if jumlah_botol_susu >1 :
    print("Budi mengecek harga dan uangnya cukup")
    if jumlah_telur >6:
        print("Budi membeli 1 botol susu dan membeli 6 butir telur")
    else:
        print("Budi membeli 1 botol susu")
else:
    print("budi tidak membeli 6 butir telur")

print("Budi pulang ke rumah")
print("menyampaikan hasilnya kepada ibu")
