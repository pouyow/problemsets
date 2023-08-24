d = {"Apple" : "130" ,
"Avocado" : "50" ,
"Banana" : "110" ,
"Cantaloupe" : "50" ,
"Grapefruit" : "60" ,
"Grapes" : "90" ,
"Honeydew Melon" : "50" ,
"Kiwifruit" : "90" ,
"Lemon" : "15" ,
"Lime" : "20" ,
"Nectarine" : "60" ,
"Orange" : "80" ,
"Peach" : "60" ,
"Pear" : "100" ,
"PineApple" : "50" ,
"Plums" : "70",
"Strawberries" : "50" ,
"SweetCherries" : "100" ,
"Tangerine" : "50" ,
"Watermelon" : "80"}
k = input("enter: ")
for s in d:
    if k in s.lower():
     print(s , d[s])
    break