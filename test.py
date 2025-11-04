persons = [
    {"name": "Eva", "cognom": "Vilaregut", "sexe": "Dona", "edat": 19, "altura": 162},
    {"name": "Joan", "cognom": "Sales", "sexe": "Home", "edat": 25, "altura": 173},
    {"name": "Laura", "cognom": "Casademunt", "sexe": "Dona", "edat": 41, "altura": 182},
    {"name": "Raquel", "cognom": "Viñales", "sexe": "Dona", "edat": 12, "altura": 123},
    {"name": "Esther", "cognom": "Parra", "sexe": "Dona", "edat": 33, "altura": 178},
    {"name": "Miquel", "cognom": "Amorós", "sexe": "Home", "edat": 56, "altura": 166},

]

# Objetivo final -> encontrar a la persona más alta de la lista

result = persons[0]
for person in persons[1:]:
    if person["altura"] > result["altura"]:
        result = person

assert result["name"] == "Laura"