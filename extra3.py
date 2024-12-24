
product_price = float(input("Mahsulot narxini kiriting: "))

sale = float(input("Chegirma foizini kiriting: "))

# Chegirma qiymatini hisoblaymiz
total = product_price * (sale / 100)

# Yakuniy narx
SUM = product_price - total

print(f"Chegirmadan keyin yakuniy narx: {SUM}")
