import requests

def get_weather(city="Guntur"):
    try:
        url = f"https://wttr.in/{city}?format=%l:+%c+%t,+%h+humidity,+%p+precipitation"
        response = requests.get(url, timeout=5)
        if response.status_code == 200 and response.text.strip():
            return response.text.strip()
        else:
            return f"Sorry, I couldn't fetch the weather for {city} right now."
    except Exception as e:
        return f"Error getting weather information for {city}."