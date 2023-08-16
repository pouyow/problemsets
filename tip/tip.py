def dollars_to_float(d):
    ss = d.replace("$" , "")
    ass = float (ss)
    return (ass)

def percent_to_float(p):
    ss = p.replace("%" , "")
    ass = float (ss)
    sss = ass / 100
    return (sss)

def main():
   dollars = dollars_to_float(input("How much was the meal? "))
   percent = percent_to_float(input("What percentage would you like to tip? "))
   tip = dollars * percent
   print(f"Leave ${tip:.2f}")

main()