import requests
import json
import gzip
import concurrent.futures
from bs4 import BeautifulSoup

class GrabFoodScraper:
    def __init__(self, location):
        self.base_url = "https://food.grab.com/sg/en/4"
        self.location = location

    def get_restaurant_list(self):
        url = f"{self.base_url}?q={self.location}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            restaurants = []
            for restaurant in soup.find_all('div', class_='restaurant-card'):
                name = restaurant.find('h6', class_='name').text.strip()
                cuisine = restaurant.find('div', class_='cuisines').text.strip()
                rating = restaurant.find('div', class_='rating').text.strip()
                delivery_fee = restaurant.find('div', class_='delivery-fee').text.strip()
                estimated_delivery_time = restaurant.find('div', class_='eta').text.strip()
                restaurants.append({
                    "name": name,
                    "cuisine": cuisine,
                    "rating": rating,
                    "delivery_fee": delivery_fee,
                    "estimated_delivery_time": estimated_delivery_time
                })
            return restaurants
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None

    def scrape_and_save(self):
        restaurant_list = self.get_restaurant_list()
        if restaurant_list:
            with gzip.open(f"{self.location.replace(' ', '_')}_restaurants.gz", 'wt', encoding='utf-8') as f:
                for restaurant in restaurant_list:
                    json.dump(restaurant, f)
                    f.write('\n')
            print("Data extraction and saving completed successfully.")
        else:
            print("No data to save.")

if __name__ == "__main__":
    locations = [
        "PT Singapore - Choa Chu Kang North 6, Singapore, 689577",
        "Chong Boon Dental Surgery - Block 456 Ang Mo Kio Avenue 10, #01-1574, Singapore, 560456"
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        scrapers = [GrabFoodScraper(location) for location in locations]
        executor.map(GrabFoodScraper.scrape_and_save, scrapers)
