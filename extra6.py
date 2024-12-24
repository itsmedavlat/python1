# Foydalanuvchidan telefon raqamini kiritishni so'rash
telefon_raqami = input("Telefon raqamingizni kiriting: ")

# Telefon raqamni oxirgi 4ta raqamini olamiz slicing qilib
oxirgi_tort = telefon_raqami[-4:]

print(f"Telefon raqamizni oxirgi 4ta raqami: {oxirgi_tort}")
