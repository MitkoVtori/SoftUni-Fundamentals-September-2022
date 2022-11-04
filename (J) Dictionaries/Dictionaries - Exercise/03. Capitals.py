countries = input().split(', ')
cities = input().split(', ')
country_capitals = dict(zip(countries, cities))
for country, city in country_capitals.items():
    print(f"{country} -> {city}")