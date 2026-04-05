import json
def sum_products() -> float:#peredat' file
    with open("input.json", 'r', encoding = 'utf-8')as f:
        data = json.load(f)
    tot = 0.0
    for item in data:
        tot += item['score'] * item['weight']
    return round(tot, 3)


print(sum_products())
