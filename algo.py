def check(map,hint):

    hint = hint.split(',')
    pin = []
    for num in hint:
        pin.append('#'*int(num))
    expect = '.'.join(pin)

    ans = [expect]

    l = len(map)
    for ptr in range(l):

        rm_lis = []

        for index,possiblility in enumerate(ans):

            if len(possiblility)>l:
                rm_lis.append(possiblility)
                continue

            try: 
                match (possiblility[ptr],map[ptr]):
                    case ('#','.'):
                        if ptr != l-1:
                            ans[index] = possiblility[:ptr] + '.' + possiblility[ptr:]
                        else:
                            rm_lis.append(possiblility)
                    case ('#','?'):
                        if ptr>=1:
                            if possiblility[ptr-1] != '#':
                                ans.append(possiblility[:ptr] + '.' + possiblility[ptr:])
                        else:
                            ans.append(possiblility[:ptr] + '.' + possiblility[ptr:])
                    case ('.','#'):
                        rm_lis.append(possiblility)
                    case _:
                        continue
            except IndexError:
                ans[index] = possiblility[:ptr] + '.' + possiblility[ptr:]
        
        for rm in rm_lis:
            ans.remove(rm)


    # print(len(ans),":",ans)
    return len(ans)


# check('?#?#?#?#?#?#?#?', '1,3,1,6')