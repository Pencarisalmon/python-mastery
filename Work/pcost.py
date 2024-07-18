
def portfolio_cost(filename):
    with open(filename, 'r') as f:
        datas = []
        for line in f:
            data = line.split()
            try:
                data[1] = int(data[1])
                data[2] = float(data[2][:-2])
                datas.append(data)

            except ValueError as e:
                print(f'Couldn\'t parse: {repr(line)}')
                print('Reason:', e)

    total_cost = 0
    for data in datas:
        total_cost += data[1]*data[2]

    return total_cost


if __name__ == '__main__':
    print(portfolio_cost('Data/portfolio3.dat'))
