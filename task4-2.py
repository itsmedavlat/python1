son1 = int (input("Birinchi son kiriting : "))
son2 = int (input("Ikkinchi son kiriting : "))

teng = son1 == son2

# boolen ishlatamiz => teng bolsa TRUE , teng bomasa False beramiz. 
natija = ["teng emas", "teng"][teng]
print(f"Sonlar {natija}")
