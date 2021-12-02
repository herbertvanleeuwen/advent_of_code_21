if __name__ == "__main__":
    with open("data/input_day2.txt") as f:
        orders = [(order.split()[0], int(order.split()[1].strip())) for order in f.readlines()]

    position = {'horizontal': 0,
                'vertical': 0,
                'aim': 0}
    for order in orders:
        if order[0] == 'forward':
            position['horizontal'] += order[1]
            position['vertical'] += position['aim'] * order[1]
        elif order[0] == 'down':
            # position['vertical'] += order[1]
            position['aim'] += order[1]
        elif order[0] == 'up':
            # position['vertical'] -= order[1]
            position['aim'] -= order[1]

    print(position)
    print(position['horizontal'] * position['vertical'])
