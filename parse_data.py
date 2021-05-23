import json


def main():
    # open text file
    with open('swiggy_data.txt') as file:
        # load json data
        order_data = json.load(file)

        print_all_orders(order_data)


def print_all_orders(order_data):
    # iterate through data for each order
    for index, order in enumerate(order_data):

        order_id = order['order_id']

        # date and time of order
        date_time = order['order_time']
        print(date_time)

        # list containing all items in order
        item_list = order['order_items']

        for item in item_list:
            item_name = item['name']
            quantity = item['quantity']
            print(f'{item_name} x {quantity}')
        print('')


if __name__ == '__main__':
    main()
