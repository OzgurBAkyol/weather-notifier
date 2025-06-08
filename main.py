from weather import get_weather_forecast as get_weather 
from message_builder import build_message
from mailer import send_email

def run_weather_notification():
    print("📡 Hava durumu tahmini alınıyor...")
    weather_data = get_weather()

    if not weather_data:
        print("❌ Hava Tahmini alınamadı. E-posta bu nedenle gönderilemedi.")
        return

    print("🧠 Mesaj oluşturuluyor...")
    message = build_message(weather_data)

    print("📬 E-posta gönderiliyor...")
    send_email("Günlük Hava Durumu Tahmini Bu Şekilde : ", message)
    print("✅ İşlem tamamlandı.")

if __name__ == "__main__":
    run_weather_notification()
