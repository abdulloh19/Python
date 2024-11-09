11-dars

1-vazfa
son = int(input("Juft son kiriting "))
if son%2 != 0:
    print("Bu son juft emas")
else:
    print("Raxmat")

2-vazifa
yosh = int(input("Yoshingizni kiriting = "))
if yosh < 4:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000

print(f"Siz uchun kirish narhi {narh} so'm")

3-vazifa
son = float(input("Birinchi sonni kiriting = "))
son2 = float(input("Ikkinchi sonni kiriting = "))
if son==son2:
    print(f"{son} = {son2}")
elif son > son2:
    print(f"{son} > {son2}")
elif son < son2:
    print(f"{son} < {son2}")

4-vazifa
mahsulotlar = ["anor", "uzum", "limon", "shaftoli", "olxo'ri", "banan", "olma", "tarvuz", "qovun", "baqlajon"]
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1} mahsulot qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(F"Do'konimizda {mahsulot} bor")
        else:
            print(f"Afsuski do'konimizda {mahsulot} yo'q")

else:
    print("Savat bo'sh")

5-vazifa
mahsulotlar = ["un", "piyola", "shaftoli", "choynak", "kapkir", "loviya", "chinni"]
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

6-vazifa
users = ["anvar", "sanjar", "abdulloh", "zubayr", "zayd"]
login = input("Yangi login tanlang: ")

if login in users:
    print(f"{login} afsuski bu login band, iltimos boshqa login tanlang.")
else:
    print(f"Xush kelibsiz {login}")

7-vazifa
son = int(input("Istalgan sonni kiriting: "))
for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
--------------------------------------------------------------------
12-dars
1-vazifa
son = float(input("Juft son kiriting: "))
if son%2!=0:
    print("Bu son juft emas.")
else:
    print("Rahmat!")

2-vazifa
yosh = int((input("Yoshingiz nechida? ")))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000

print(f"Chipta {narh} so'm")

3-vazifa
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")

4-vazifa
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else: 
    print("Savatingiz bo'sh")  

5-vazifa
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

savat = []
for n in range(5):
    savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
for mahsulot  in mavjud_emas:
  print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

6-vazifa
users = ['alisher1983','aziza','yasina' 'umar']

login = input("Yangi login tanlang:" )

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")