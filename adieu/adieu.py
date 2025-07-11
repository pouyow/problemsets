def formating(names):
    if len(names) == 0:
        return ""
    elif len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return " and ".join(names)
    else:
        return ", ".join(names[:-1]) + ", and " + names[-1]

names = []
try:
    while True:
        name = input("Name")
        names.append(name)
except EOFError:
    pass

formatted_names = formating(names)
print(f"Adieu, adieu, to {formatted_names}")
