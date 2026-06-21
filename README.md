# Portfolio/Resume API

Shaxsiy portfolio va rezyume (CV) sayti uchun Django REST Framework asosida qurilgan backend API.

---

## Loyiha tuzilmasi

```
project/
├── ronaldo/                 # Asosiy ilova
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
└── config/                  # Loyiha sozlamalari
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

## Texnologiyalar

- **Python**
- **Django** — web framework
- **Django REST Framework** — API yaratish uchun
- **drf-yasg** — Swagger/OpenAPI dokumentatsiya
- **python-dotenv** — muhit o'zgaruvchilarini boshqarish

---

## O'rnatish

```bash
# 1. Reponi klonlash
git clone https://github.com/username/portfolio-api.git
cd portfolio-api

# 2. Virtual muhit yaratish
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 3. Kutubxonalarni o'rnatish
pip install -r requirements.txt

# 4. .env faylini yaratish
cp .env.example .env
# .env faylga SECRET_KEY qiymatini kiriting

# 5. Migratsiyalarni bajarish
python manage.py migrate

# 6. Serverni ishga tushirish
python manage.py runserver
```

---

## API Endpointlari

| Method | URL | Tavsif |
|--------|-----|--------|
| GET | `/api/about/` | Shaxsiy ma'lumotlar (About) |
| GET | `/api/resume/` | Ta'lim/rezyume tarixi |
| GET | `/api/malaka/` | Malaka oshirish kurslari |
| GET | `/api/tajriba/` | Ish tajribasi va ko'nikmalar foizi |
| GET | `/api/m_tajriba/` | Qo'shimcha ko'nikmalar (mini tajriba) |
| GET | `/api/sovrinlar/` | Sovrinlar va yutuqlar |
| GET | `/api/service/` | Taklif qilinadigan xizmatlar |
| GET | `/api/projects/` | Bajarilgan loyihalar |
| GET | `/api/blog/` | Blog postlari |
| POST | `/api/contact/` | Aloqa formasi orqali xabar yuborish |

---

## Modellar haqida qisqacha

- **About** — shaxsiy ma'lumotlar (ism, tug'ilgan sana, manzil, email, telefon, bajarilgan loyihalar soni)
- **Resume** — ta'lim/ish tarixi (yil, sarlavha, o'qish markazi)
- **Malaka** — malaka oshirish kurslari
- **Tajriba** — ko'nikmalar va ularning foiz darajasi
- **M_tajriba** — qo'shimcha ko'nikmalar ro'yxati
- **Sovrinlar** — yutuqlar va sovrinlar
- **Service** — taklif qilinadigan xizmatlar
- **Projects** — bajarilgan loyihalar (rasm, dizayn turi bilan)
- **Blog** — blog postlari
- **Contact** — aloqa ma'lumotlari va yuborilgan xabarlar

---

## Muhit o'zgaruvchilari

`.env` fayl yaratib quyidagini sozlang:

```env
SECRET_KEY=
```

---

## Litsenziya

MIT License