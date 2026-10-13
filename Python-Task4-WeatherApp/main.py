import requests


def get_weather():
    print("\n" + "=" * 40)
    print("       PYTHON WEATHER APP")
    print("=" * 40)

    city = input("Enter city name: ").strip()

    if not city:
        print("Error: Please enter a city name.")
        return

    url = "https://wttr.in/" + requests.utils.quote(city) + "?format=j1"

    print("\nFetching weather information...")

    try:
        response = requests.get(
            url,
            timeout=15,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()
        data = response.json()

        current = data["current_condition"][0]
        location = data["nearest_area"][0]

        city_name = location["areaName"][0]["value"]
        country = location["country"][0]["value"]
        temperature = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        humidity = current["humidity"]
        description = current["weatherDesc"][0]["value"]
        wind_speed = current["windspeedKmph"]

        print("\n" + "-" * 40)
        print("          CURRENT WEATHER")
        print("-" * 40)
        print(f"City          : {city_name}, {country}")
        print(f"Temperature   : {temperature} °C")
        print(f"Feels Like    : {feels_like} °C")
        print(f"Condition     : {description}")
        print(f"Humidity      : {humidity}%")
        print(f"Wind Speed    : {wind_speed} km/h")
        print("-" * 40)

    except requests.exceptions.RequestException:
        print("Unable to fetch weather data.")
        print("Check your internet connection and try again.")
    except (KeyError, IndexError, ValueError):
        print("Weather data could not be processed.")
        print("Please try another city.")


def main():
    while True:
        get_weather()

        choice = input(
            "\nCheck another city? (yes/no): "
        ).strip().lower()

        if choice not in ("yes", "y"):
            print("\nThank you for using Python Weather App!")
            break


if __name__ == "__main__":
    main()