# 🌤️ Weather Notifier

Günlük hava durumu tahminini sabah saat 07:00'de otomatik olarak e-posta ile gönderen Python tabanlı bir bildirim sistemidir.

## 🚀 Özellikler

-  **Her sabah 07:00'de otomatik mail gönderimi** (cron ile zamanlanmış)
-  **Sabah / Öğle / Akşam hava durumu tahmini**
-  Ortalama sıcaklık, hissedilen sıcaklık, nem, rüzgar, görüş mesafesi
-  Giyinme ve plan yapma tavsiyeleri
-  Tamamen terminalden çalışabilir
-  `.env` dosyası ile gizli API & mail bilgileri

---

## 🛠️ Kullanılan Teknolojiler

- Python 3.x
- [OpenWeatherMap API](https://openweathermap.org/api)
- `requests`, `dotenv`, `smtplib`
- macOS/Linux için `cron` zamanlayıcı

---

## 📦 Kurulum

```bash
# 1. Repo'yu klonla
git clone https://github.com/OzgurBAkyol/weather-notifier.git
cd weather-notifier

# 2. Sanal ortam oluştur ve etkinleştir
python3 -m venv notifier
source notifier/bin/activate

# 3. Gerekli paketleri yükle
pip install -r requirements.txt
