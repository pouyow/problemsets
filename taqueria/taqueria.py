nar = [{
"Baja Taco": 4.00,
"Burrito": 7.50,
"Bowl": 8.50,
"Nachos": 11.00,
"Quesadilla": 8.50,
"Super Burrito": 8.50,
"Super Quesadilla": 9.50,
"Taco": 3.00,
"Tortilla Salad": 8.00
}]
while True:
    try:
        inp = input("Item: ").title()
        for i in nar:
           k = i[inp]
           s += k
           s = round(s, 2)
           print("{:.2f}".format(s))
    except(KeyError):
        pass
    except(EOFError):
        exit()