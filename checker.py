async def checker(stoimost, s):
    k = 0
    try:
            stoim =  int(stoimost)
    except ValueError:
            k += 1
    try:
        a = list(stoimost)
    except IndexError:
        a[0] = 1 
    try: 
        if a[0] == '-':
            k += 1
    except IndexError:
        k += 1
    if k > 0:
        stoim = -1
        s = 'Стоимость введена некоректно введите ее заново'
    return stoim, s