import requests

response = requests.get('https://randomuser.me/api/?results=100&gender=male')
numbers = response.json()

users = numbers['results']
top_male_population = []

for men in population:
    if user['gender'] == 'male':
        top_male_population.append(men)

for i, men in enumerate(top_male_population):
    print(f"{i+1}. {men['name']['first']} {men['name']['last']}")