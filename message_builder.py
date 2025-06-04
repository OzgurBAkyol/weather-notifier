def build_message(weather_data):
    if not weather_data:
        return "Hava durumu bilgisi alınamadı."

    city = weather_data.get("city", "Bilinmeyen Konum")

    lines = [f"📍 {city} için günün hava durumu özeti:", ""]

    def format_period(name, data):
        if not data:
            return f"{name}: Bilgi yok"

        icon = {"Sabah": "🌅", "Öğle": "🌞", "Akşam": "🌙"}.get(name, "⏰")
        desc = data['desc']
        temp = data['avg_temp']
        feels = data['feels_like']
        t_min = data['temp_min']
        t_max = data['temp_max']
        humidity = data['humidity']
        wind = data['wind']
        vis = data['visibility']

        return (
            f"{icon} {name}:\n"
            f"➡️ Hava: {desc}\n"
            f"🌡️ Sıcaklık: {temp}°C (Hissedilen: {feels}°C)\n"
            f"📊 Min: {t_min}°C / Max: {t_max}°C\n"
            f"💧 Nem: %{humidity}\n"
            f"💨 Rüzgar: {wind} m/s\n"
            f"👁️ Görüş mesafesi: {vis} km\n"
        )

    # Sabah / Öğle / Akşam blokları
    lines.append(format_period("Sabah", weather_data.get("morning")))
    lines.append(format_period("Öğle", weather_data.get("afternoon")))
    lines.append(format_period("Akşam", weather_data.get("evening")))
    lines.append("")

    # Günlük maksimum sıcaklığa göre detaylı giyinme önerisi
    temps = [
        data["temp_max"]
        for key in ["morning", "afternoon", "evening"]
        if weather_data.get(key)
        for data in [weather_data[key]]
    ]
    temp_max = max(temps) if temps else 0

    if temp_max < 5:
        lines.append(
            "🧣 Hava oldukça soğuk. Dışarı çıkarken atkı, bere ve kalın mont şart.\n"
            "Uzun süre dışarıda kalacaksan eldiven almayı unutma.\n"
            "Soğuk algınlığına karşı dikkatli ol, özellikle sabah saatlerinde açık alanlardan kaçın."
        )
    elif temp_max < 15:
        lines.append(
            "🧥 Bugün serin bir gün. İnce bir mont ya da ceket seni rahat ettirir.\n"
            "Sabah saatleri daha soğuk olabilir, katmanlı giyinmek akıllıca olur.\n"
            "Rüzgar varsa boynunu koruyacak bir şey almayı unutma."
        )
    else:
        lines.append(
            "👕 Hava genel olarak sıcak. Tişört, gömlek ve hafif kıyafetler yeterli olacaktır.\n"
            "Açık renkli giysiler, şapka ve güneş gözlüğü tercih edebilirsin.\n"
            "Bol su içmeyi ihmal etme, dışarıda uzun kalacaksan güneşe dikkat et!"
        )

    return "\n".join(lines)
