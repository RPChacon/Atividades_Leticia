for x in range(2, 100):
    primo = True
    for y in range(2, x):
        if x % y == 0:
            primo = False
            break
        if primo:
            print(x)
