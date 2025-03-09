import requests
import random

# ЗАДАНИЕ 1
def get_weather(city_name, api_key):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
            }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        weather_description = data['weather'][0]['description']
        print(f"Данные о погоде в {city_name}:")
        #print(f"{data}")
        print(f"Температура: {temperature}°C")
        print(f"Влажность: {humidity}%")
        print(f"Давление: {pressure} hPa")
        print(f"Описание: {weather_description}\n")
    else:
        print(f"Ошибка при получении данных: {response.status_code}\n")

api_key = '4e60058a7b1b4c41295ba6ca2434c2b9'
city_name = 'Tokyo'
get_weather(city_name, api_key)

# ЗАДАНИЕ 2

def character_info(character_id):

    url_character = f"https://rickandmortyapi.com/api/character/{character_id}"
    response_character = requests.get(url_character)

    if response_character.status_code == 200:
        data = response_character.json()
        print("Данные о рандомном персонаже:")
        # print(data)
        print(f"Имя: {data['name']}")
        print(f"Статус: {data['status']}")
        print(f"Вид: {data['species']}")
        print(f"Происхождение: {data['origin']['name']}")
        print(f"Локация: {data['location']['name']}\n")

    else:
        print(f"Ошибка при получении данных: {response_character.status_code}")

def episode_info(episodes_id):
    url_episodes = f"https://rickandmortyapi.com/api/episode/{episodes_id}"
    response_episodes = requests.get(url_episodes)
    if response_episodes.status_code == 200:
        data = response_episodes.json()
        print("Данные о рандомном эпизоде:")
        # print(data)
        print(f"Название эпизода: {data['name']}")
        print(f"Дата начала эпизода: {data['air_date']}\n")
    else:
        print(f"Ошибка при получении данных: {response_character.status_code}")

character_id = random.randint(1, 826)
episodes_id = random.randint(1, 51)

character_info(character_id)
episode_info(episodes_id)