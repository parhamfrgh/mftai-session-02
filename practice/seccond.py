def convert(s: str) -> list:
    return [int(x) if x.isnumeric() else x for x in s.split(",")]

print(convert("alireza,alavi,23,tehran"))
