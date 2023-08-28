q = {}
while True:
 try:
    s = input()
    if s in q:
        q[s] += 1
    else:
        q[s] = 1

 except EOFError:
    for i in sorted(q.keys()):
        print(q[i], i.upper())
    break
