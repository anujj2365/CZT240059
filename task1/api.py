import requests

def fetch_recipe():
    api_url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        if "meals" in data and data["meals"]:
            meal = data["meals"][0]
            print(f"Meal: {meal['strMeal']}")
            print(f"Category: {meal['strCategory']}")
            print(f"Instructions: {meal['strInstructions']}")
            print(f"Ingredients:")
            for i in range(1, 21):
                ingredient = meal[f"strIngredient{i}"]
                measure = meal[f"strMeasure{i}"]
                if ingredient and ingredient.strip():
                    print(f"  - {ingredient}: {measure}")
        else:
            print("No meal data found.")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

fetch_recipe()
