q = [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
]
while True:
    ss = input("enter: ")
    try:
        m,d,y = ss.split("/")
        if int(m) <= 12 and int(d) <= 31:
         print(f"{y}-{int(m):02}-{int(d):02}")
         break
    except:
        try:
            mm,dd,yy = ss.split(" ")
            for i in range(len(q)):
               if mm == q[i]:
                mm = i + 1
            d = dd.replace(",", "")
            if int(d) <= 31:
              print(f"{yy}-{(mm):02}-{int(d):02}")
              break
        except:
                pass
