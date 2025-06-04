import schedule
import time
from weather import get_weather
from message_builder import build_message
from mailer import send_email


def job():
    print("⏰ Zamanlı görev başlatıldı...")
    weather_data = get_weather()
    if weather_data:
        message = build_message(weather_data)
        send_email("Günlük Hava Durumu Raporu", message)
    else:
        print("❌ Hava durumu alınamadı, e-posta gönderilmeyecek.")


# Örneğin her sabah 07:30'da çalıştır
schedule.every().day.at("07:30").do(job)

# Test amaçlı her 1 dakikada bir çalıştırmak istersen:
# schedule.every(1).minutes.do(job)

print("📅 Zamanlayıcı başlatıldı. Bekleniyor...")

while True:
    schedule.run_pending()
    time.sleep(1)
