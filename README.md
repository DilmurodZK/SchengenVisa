# 📌 SchengenVisa Bot

## 📖 Loyihaning qisqacha tavsifi
**SchengenVisa Bot** — foydalanuvchi nomidan Shengen vizasi uchun ariza topshirish imkoniyati ochiq yoki yo‘qligini tekshiruvchi avtomatlashtirilgan dastur.  

Botning ishlash prinsipi:  
- 🔹 **Selenium** orqali viza ariza topshirish saytiga kiradi  
- 🔹 Kerakli sahifalarga avtomatik o‘tadi  
- 🔹 Foydalanuvchi ma’lumotlarini kiritadi yoki mavjud variantlardan tanlaydi  
- 🔹 Ko‘rsatilgan parametrlar asosida **ariza topshirish imkoniyati mavjud yoki yo‘qligini** qaytaradi  
- 🔹 Ishga tushirishdan oldin **so‘rov yuborish intervali** sozlanadi (masalan, 5 daqiqa)  

---

## ⚙️ Texnologiyalar
- **Python 3.x**  
- **Selenium** (brauzer avtomatlashtirish)  
- **WebDriver** (ChromeDriver / GeckoDriver)  
- **Telegram Bot API** (agar natija foydalanuvchiga bot orqali yuborilsa)  

---

## 🚀 O‘rnatish (Installation)

1. Repozitoriyani klonlash:
   ```bash
   git clone https://github.com/DilmurodZK/SchengenVisa.git
   cd SchengenVisa
   
2. Virtual environment yaratish va faollashtirish:
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Kerakli kutubxonalarni o‘rnatish:
   pip install -r requirements.txt

4. ChromeDriver yoki GeckoDriver o‘rnatilgan bo‘lishi kerak

5. config.py faylida interval va boshqa sozlamalarni belgilash:
   seconds = 300  # soniyada, intervalni kattaroq yozish tavsiya qilinadi (bir necha soat)

6. Botni ishga tushirish:
   python main.py

📊 Asosiy imkoniyatlar

✅ Ariza topshirish imkoniyatini avtomatik tekshirish
✅ Foydalanuvchi ma’lumotlarini avtomatik kiritish
✅ So‘rov yuborish intervalini sozlash
✅ (Ixtiyoriy) Natijani Telegram orqali yuborish

📂 Loyiha tuzilmasi
SchengenVisa/
│── main.py          # Botning ishga tushirish fayli
│── config.py        # Sozlamalar (interval va boshqa)
│── modules/         # Selenium orqali ishlovchi modullar
│── requirements.txt # Kutubxonalar ro‘yxati
│── README.md

⚠️ Eslatma
Bu loyiha o‘quv va shaxsiy foydalanish uchun yaratilgan. Rasmiy saytlardan foydalanishda ehtiyot bo‘ling va saytning qoidalariga amal qiling.
