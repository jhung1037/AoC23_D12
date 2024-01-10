import test

def readf():
    data = []
    with open("Map.txt") as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.split(' '))
    return data

if __name__ == '__main__':
    data = readf()
    sum=0
    for d in data:
        sum += test.check(d[0],d[1])
    print(sum)