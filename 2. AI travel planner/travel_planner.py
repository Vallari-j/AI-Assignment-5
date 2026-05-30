import json


with open("tourist_places.json") as f:
    places = json.load(f)

with open("food_recommendations.json") as f:
    foods = json.load(f)

with open("travel_costs.json") as f:
    costs = json.load(f)


def create_plan(city, days, interest):

    if city not in places:
        return "City not available."

    attractions = places[city].get(interest, [])

    itinerary = {}

    attraction_index = 0

    for day in range(1, days + 1):

        day_places = []

        for _ in range(2):

            if attraction_index < len(attractions):
                day_places.append(
                    attractions[attraction_index]
                )
                attraction_index += 1

        itinerary[f"Day {day}"] = day_places

    return itinerary


def estimate_cost(city, days):

    c = costs[city]

    total = (
        c["hotel_per_day"] +
        c["food_per_day"] +
        c["transport_per_day"]
    ) * days

    return total


def recommend_food(city):

    return foods.get(city, [])


city = input("Enter city: ")
days = int(input("Enter days: "))
interest = input(
    "Interest (Historical/Nature): "
)

plan = create_plan(city, days, interest)

print("\nPERSONALIZED TRAVEL PLAN\n")

for day, places in plan.items():
    print(day)

    for p in places:
        print("  -", p)

print("\nRecommended Foods:")

for food in recommend_food(city):
    print("-", food)

print(
    "\nEstimated Cost: ₹",
    estimate_cost(city, days)
)
