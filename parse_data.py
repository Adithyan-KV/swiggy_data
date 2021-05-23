import json


def main():
    # open text file
    with open('swiggy_data.txt') as file:
        # load json data
        order_data = json.load(file)

        # total number of orders
        num_orders = len(order_data)

        # iterate through data for each order
        for index, order in enumerate(order_data):
            print(index)


if __name__ == '__main__':
    main()
