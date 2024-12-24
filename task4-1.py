
son1 = float( input("Birinchi sonni kiriting: ") )
son2 = float( input("Ikkinchi sonni kiriting:") )

# Tengmaslik va kattalikni aniqlaymiz
tengmas = son1 != son2
katta = son1 > son2
# boolen ishlatamiz - teng bulsa - True aski bulsa False
natija_tengmas = ["teng", "teng emas"][tengmas]
natija_katta = ["kichik yoki teng", "katta"][katta]

print(f" Sonlar biri biriga {natija_tengmas} " )
print(f" Birinchi son ikkinchi sondan {natija_katta} ")
