import requests

def get_weather(city):
    api_key = 'ddf3e0f3b4aadad90149f0a204d28af9'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def get_news():
    api_key_news = "cabcb87096ba465bb1b35a606eaa6f41"
    url_news = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key_news}"
    response = requests.get(url_news)
    data = response.json().get('articles', []) #Если ключа не будет, возвращаться будет пустой список.
    return data

def get_quotes():
    url = 'https://zenquotes.io/api/random'
    response = requests.get(url)
    data = response.json()
    return data
