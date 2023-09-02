def convert(keys: str, values: str) -> list:
    return [f"{k}:{v}" for k, v in zip(keys.split(","), values.split(","))]

print(convert("name,family,age,location", "alireza,alavi,23,tehran"))
