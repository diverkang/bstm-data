
import json, sys

REQUIRED_KEYS_CITY = ["ko","durationHint","costIndex"]
def walk(db):
    problems = []
    for cont, countries in db.items():
        if cont.startswith("_"):
            continue
        if not isinstance(countries, dict):
            problems.append(f"[{cont}] is not an object")
            continue
        for country, cities in countries.items():
            if country.startswith("_"):
                continue
            if not isinstance(cities, dict):
                problems.append(f"[{cont}/{country}] is not an object")
                continue
            for city, payload in cities.items():
                if city.startswith("_"):
                    continue
                if not isinstance(payload, dict):
                    problems.append(f"[{cont}/{country}/{city}] not an object")
                    continue
                for k in REQUIRED_KEYS_CITY:
                    if k not in payload:
                        problems.append(f"Missing key {k}: {cont}/{country}/{city}")
    return problems

def main(fp):
    with open(fp, "r", encoding="utf-8") as f:
        db = json.load(f)
    probs = walk(db)
    if probs:
        print("❌ Problems found:")
        for p in probs: print("-", p)
        sys.exit(1)
    print("✅ Looks good:", fp)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validator.py <data_pack.json>")
        sys.exit(2)
    main(sys.argv[1])
