import json
import numpy as np
import matplotlib.pyplot as plt


def main():
    # open text file
    with open('swiggy_data.txt') as file:
        # load json data
        order_data = json.load(file)

        # print_all_orders(order_data)

        # getting number of orders
        num_orders = len(order_data)

        # getting price details
        net_price, gross_price, price_list = get_total_price(order_data)

        # getting basic price statistics
        average_order_value = np.mean(price_list)
        median_order_value = np.median(price_list)
        std_order_value = np.std(price_list)

        plot_price_distribution(price_list)

        print(average_order_value, median_order_value, std_order_value)


def get_total_price(order_data):
    total_gross_price = 0
    total_net_price = 0
    net_price_list = []

    # iterating over all orders and adding up prices
    for order in order_data:

        # pre discounts
        restaurant_bill = float(order['order_restaurant_bill'])
        delivery_charges = float(
            order['order_delivery_charge'])
        gross_price = restaurant_bill + delivery_charges

        # post discounts
        net_price = order['order_total']

        # update prices
        total_gross_price += gross_price
        total_net_price += net_price
        net_price_list.append(net_price)

    return total_net_price, total_gross_price, net_price_list


def plot_price_distribution(price_list):
    num_bins = 100
    n, bins, patches = plt.hist(price_list, num_bins)
    plt.title('Distribution of order value')
    plt.xlabel('Order value (₹)')
    plt.ylabel('Number of orders')
    plt.show()


def print_all_orders(order_data):
    # iterate through data for each order
    for index, order in enumerate(order_data):

        order_id = order['order_id']

        # date and time of order
        date_time = order['order_time']
        print(date_time)

        # Name of restaurant
        restaurant = order['restaurant_name']
        print(f'Restaurant:{restaurant}')

        # list containing all items in order
        item_list = order['order_items']

        # individual items and their quantities
        for item in item_list:
            item_name = item['name']
            quantity = item['quantity']
            print(f'{item_name} x {quantity}')

        # getting final price of item
        price = order['net_total']
        print(f'₹{price}')
        print('')


if __name__ == '__main__':
    main()
