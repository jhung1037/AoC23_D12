import AoC23_D12.algo as algo

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
        sum += algo.check(d[0],d[1])
    print(sum)