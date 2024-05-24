import requests

def get_weather(api_key, city):
    base_url = "http://api.weatherstack.com/current"
    params = {
        'access_key': api_key,
        'query': city,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad responses

        weather_data = response.json()
        current_data = weather_data['current']
        weather_description = current_data['weather_descriptions'][0]
        temperature = current_data['temperature']

        print(f"Weather in {city}: {weather_description}")
        print(f"Temperature: {temperature}°C")
    
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    api_key = 'cb56a8e1487240cfd7bc5fd7a34fd69d'  # Replace with your Weatherstack API key
    city = input("Enter city: ")

    get_weather(api_key, city)