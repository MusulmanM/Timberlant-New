
# 🌲 Timberland Backend v1

Ushbu loyiha Django asosida yozilgan backend tizimidir. Quyidagi bosqichlar orqali loyihani lokal kompyuteringizda ishga tushirishingiz mumkin.

---

## 📥 1. Loyihani yuklab olish

```bash
git clone https://github.com/fintechhub-darsliklar/timberland-backend-v1.git
cd timberland-backend-v1
```

---

## 🐍 2. Virtual Environment (venv) yaratish

Agar sizda `python` mavjud bo‘lsa:

```bash
python -m venv venv
```

Agar sizda `python3` bo‘lsa:

```bash
python3 -m venv venv
```

---

## ▶️ 3. Virtual Environment ni aktivatsiya qilish

### 🔹 Git Bash (Windows)

```bash
source venv/Scripts/activate
```

### 🔹 Linux / MacOS

```bash
source venv/bin/activate
```

---

## 📦 4. Kerakli kutubxonalarni o‘rnatish

```bash
pip install -r requirements.txt
```

---

## ⚙️ 4.1 Environment fayl yaratish

```bash
cp .env.example .env
```

So‘ng `.env` fayl ichini o‘zingizga moslab to‘ldiring.

---

## 🗄 5. Ma'lumotlar bazasini yaratish

```bash
python manage.py migrate
```

---

## 👤 6. Superuser yaratish

```bash
python manage.py createsuperuser
```

---

## 🚀 7. Loyihani ishga tushirish

```bash
python manage.py runserver
```

Brauzer orqali quyidagi manzilga kiring:

```
http://127.0.0.1:8000/
```

---

## 🛠 Texnologiyalar

* Python
* Django
* PostgreSQL (agar ishlatilsa)
* Virtual Environment

---