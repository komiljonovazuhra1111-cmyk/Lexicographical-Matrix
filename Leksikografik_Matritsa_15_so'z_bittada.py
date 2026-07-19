# 1-bob,1-so'z: Pythonda o‘zgaruvchilarni hosil qilish (8-bet)
soz = "Idrok"
manosi = "Tashqi dunyo voqea, hodisalarini bilish, tushunish qobiliyati"

# Qiymatlarni ekranga chiqarish (print)
print(soz)
print(manosi)




# 1-bob,2-so'z: Python operatorlari va arifmetik amallar (12-bet)
x = 10
y = 3

# Izohli lug'at qoidasiga ko'ra amallarning ketma-ket bajarilishi
print("Qo'shish algoritmi:", x + y)
print("Ko'paytirish algoritmi:", x * y)
print("Qoldiqli bo'lish algoritmi:", x % y)




# 1-bob,3-so'z: Nomli indekslar yordamida satrlarni formatlash
fahm_ijobiy = "farosatli"
fahm_salbiy = "farosatsiz"
andoza = "Bahrombek ishni pishiq qiladigan, {ijobiy} o'g'il edi, ammo akasi {salbiy} bo'lib chiqdi."

print(andoza.format(ijobiy=fahm_ijobiy, salbiy=fahm_salbiy))




#1-bob,4-so'z: Nil sathini o'lchovchi o'zgaruvchi (Variable)
nil_sathi = 12.5  # Boshlang'ich qiymat (tirsak hisobida)
print(f"Nilning joriy sathi: {nil_sathi} tirsak")

# Suv sathi ko'tarilishi (Qiymat o'zgarishi)
nil_sathi = 16.0
print(f"Toshqin paytidagi sath: {nil_sathi} tirsak")

# Suv sathi pasayishi
nil_sathi = 7.2
print(f"Qurg'oqchilik paytidagi sath: {nil_sathi} tirsak")




# 1-bob,5-so'z:Ibn Sino irodasining algoritmi
masala_yechildimi = False
urinishlar_soni = 0

print("Ibn Sino murakkab masalani yechishni boshladi...")

# Maqsadga erishguncha sikl to'xtamaydi (Iroda)
while not masala_yechildimi:
    urinishlar_soni += 1
    print(f"{urinishlar_soni}-kecha: Izlanish davom etmoqda...")
    
    # Ma'lum bir urinishdan keyin yechim topiladi
    if urinishlar_soni == 5:
        masala_yechildimi = True

print("Natija: Iroda va sabr bilan masala yechildi!")




# 1-bob,6-so'z: Saboq — amal va natija (Input -> Process -> Output)
xatolar_soni = 0

amal = input("O'tgan kundagi holatingizni kiriting (yaxshi / xato / o'rganmadim): ")

if amal == "xato":
    xatolar_soni += 1
    print(f"Saboq olindi! Xato tahlil qilindi, tizim yangilandi. Jami saboqlar: {xatolar_soni}")
elif amal == "yaxshi":
    print("Amal to'g'ri bajarildi. Natija mustahkamlandi.")
else:
    print("Ma'lumot yetarli emas — hali xulosa chiqarib bo'lmaydi.")




# 1-bob,7-so'z: Haqiqat — tashqi bosimga qaramay o'zgarmas Constant
haqiqat = True
xavf_darajasi = 10  # "Qilich" — tashqi bosim kuchi

# Mantiqiy tekshiruv: xavf bor VA haqiqat hali ham True bo'lsa
if xavf_darajasi > 0 and haqiqat == True:
    print("Xavf mavjud, ammo ma'lumot o'zgarmadi: Rost so'zlandi.")
elif not haqiqat:
    print("Xato! Tizim yaxlitligi (integrity) buzilgan.")
else:
    print("Xavf yo'q, haqiqat baribir saqlanadi.")



#1-bob,8-so'z:
import datetime

# Hozirgi sana va vaqtni olamiz
hozirgi_vaqt = datetime.datetime.now()

# Uni ekranga chiqaramiz
print("Kashfiyot lahzasi qayd etildi:")
print(hozirgi_vaqt)




# 1-bob,9-so'z: Forobiy: resurslarni aholiga adolatli taqsimlash
resurs = 100        # Umumiy resurs (masalan, non soni)
aholi_soni = 5       # Shahar aholisi

ulush = resurs / aholi_soni

for kishi in range(1, aholi_soni + 1):
    print(f"{kishi}-kishi o'z ulushini oldi: {ulush} birlik")




# 1-bob,10-so'z:(Deb(u)ag,debaglash) ilmiy ehtiyotkorligi (Xatoliklar bilan ishlash)
try:
    # Tizimda hali e'lon qilinmagan (mavjud bo'lmagan) xulosani tekshirish
    print(x)
except NameError:
    # Agar ma'lumot topilmasa, dastur to'xtab qolmaydi, balki ogohlantirish beradi
    print("Xatolik: x o'zgaruvchisi (ma'lumotlar omborida) mavjud emas")




#1-bob,11-so'z:Aristotel.
from abc import ABC, abstractmethod

# Aristotel andozasi (Abstract Class)
class Borliq(ABC):
    @abstractmethod
    def mohiyat(self):
        # Bu yerda detallar yo'q, faqat umumiy talab bor
        pass

# Abstraksiyani amalda qo'llash (Implementation)
class Inson(Borliq):
    def mohiyat(self):
        return "Natija: Insonning botini - aql va nutqdir."

class Daraxt(Borliq):
    def mohiyat(self):
        return "Natija: Daraxtning botini - o'sish va meva berishdir."

# Sinab ko'ramiz:
odam = Inson()
print(odam.mohiyat())





# 1-bob,12-so'z: Ona sinf (Base Class) - Ustoz (Ibn Sino) maktabi va uning merosi
class TibQonunlari:
    def __init__(self, kitob_nomi, asosiy_ilm):
        self.kitob_nomi = kitob_nomi
        self.asosiy_ilm = asosiy_ilm

    def davolash(self):
        return f"Fundamental tibbiyot asosi: {self.asosiy_ilm}."

# Voris sinf (Derived Class) - Ustoz yo'lini davom ettiruvchi Shogird
class Shogird(TibQonunlari):
    def __init__(self, kitob_nomi, asosiy_ilm, shogird_ismi):
        # Ustoz qoldirgan asar va ilm xususiyatlarini meros qilib olish
        super().__init__(kitob_nomi, asosiy_ilm)
        self.shogird_ismi = shogird_ismi
        self.yangi_tajriba = "Amaliy jarrohlik va yangi dori-darmonlar"

    # Ustoz metodini zamon talabiga qarab boyitish (Method Overriding)
    def davolash(self):
        ustoz_merosi = super().davolash()
        return f"{ustoz_merosi} Shogird {self.shogird_ismi} tomondan qo'shilgan hissa: {self.yangi_tajriba}."

# Tizimni real hayotda sinab ko'rish (Obyekt yaratish)
shogird_olim = Shogird("Tib qonunlari", "Puls diagnostikasi va anatomiya", "Abuhayr Jobir")

print(f"Meros qolgan asar: {shogird_olim.kitob_nomi}")
print(f"Ilmiy vorislik natijasi: {shogird_olim.davolash()}")




# 13-soz:Ixlos (Integrity) tekshiruvi: Ma'lumotning o'zgarishi yoki buzilmasligi
def ixlos_tekshiruvi(asl_niyat, joriy_amal):
    # Agar amal niyatga mos bo'lsa (Integrity saqlansa)
    if hash(asl_niyat) == hash(joriy_amal):
        return "Ixlos mustahkam: Tizim (yoki inson) o'zligini yo'qotmadi."
    else:
        return "Diqqat: Ixlos buzildi! Tizimda begona 'aralashma' (corruption) bor."

# Boshlang'ich qiymatlarni o'zgaruvchi konteynerlariga yuklash
niyat = "Xalqqa xizmat qilish va toza kod yozish"
amal = "Xalqqa xizmat qilish va toza kod yozish"

# Natijani ekranga chiqarish
print(ixlos_tekshiruvi(niyat, amal))





#14-so'z:Formatlash.
import json

# Satrlarni formatlash (f-string) — muloqot odobi va protokolining asosi
def muloqot_tizimi(sender, message):
    # 1. Protocol (Adab): Muloqot formati (JSON - zamonaviy til)
    payload = {
        "kimdan": sender,
        "xabar": message,
        "status": "Uchrashuv o'rnatildi"
    }
    
    # 2. Handshake (Salomlashish): Ikki tomonning bir-birini tanishi
    muloqot_log = json.dumps(payload, ensure_ascii=False)
    
    # 3. Transmission (Uzatish) va 28-bet: Satrlarni formatlash orqali muloqotni qurish
    # f-string matn ichiga o'zgaruvchilarni "aralashmasiz" joylashtirish san'atidir
    if "samimiyat" in message.lower() or "vatan" in message.lower():
        # Esenin uslubidagi formatlangan silliq muloqot
        return f"Esenin uslubida muloqot: {muloqot_log}"
    else:
        # Oddiy, quruq formatlangan texnik muloqot
        return f"Texnik muloqot: {muloqot_log}"

# Amaliyotda qo'llash
print(muloqot_tizimi("Sergey Esenin", "Vatanim va samimiyatim bilan salom!"))





# 15-so'z:Tizimlarni o'zaro muvofiqlashtirish va integratsiya qilish algoritmi
def tizim_integratsiyasi(lingvistik_data, texnik_kod, iqtisodiy_ulush):
    # f-string yordamida ayrim qismlarni qo'shib, bitta butunlik (Ekotizim) hosil qilish
    ekotizim = f"Integrated System: [{lingvistik_data}] + [{texnik_kod}] -> Matrix Active."
    
    # Integratsiya muvaffaqiyatini (Data Compatibility) tekshirish
    if ekotizim and iqtisodiy_ulush > 0:
        return f"Integratsiya muvaffaqiyatli: {ekotizim} | Status: 200 OK (Muvofiqlashdi)."
    else:
        return "Xatolik: Elementlar mos kelmadi (Integration Failed)."

# 1-bobning yakuniy jamoaviy matritsasini integratsiyaga yuklash
til_qatlam = "O'zbek tili Izohli lug'ati (1-bob)"
kod_qatlam = "Python Source Code (GitHub Repository)"
ulush = 100 # Jamoaviy ittifoq resursi

print(tizim_integratsiyasi(til_qatlam, kod_qatlam, ulush))













