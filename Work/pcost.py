

with open('Data/portfolio.dat', 'r') as f:
    datas = []
    for line in f:
        data = line.split(' ')
        data[1] = int(data[1])
        data[2] = float(data[2][:-2])
        datas.append(datas)

total_cost = 0
for data in datas:
    total_cost += data[1]*data[2]

print(total_cost)
