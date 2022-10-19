people = [
    {"name": "owen", "country": "kenya"},
    {"name": "samuel", "country": "uganda"},
    {"name": "melody", "country": "tanzania"}
]

def f(person):
    return person["name"]

people.sort(key=f)

print(people)