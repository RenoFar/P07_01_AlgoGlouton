#! /usr/bin/env python3
# coding: utf-8


first_stock = [['share-1', 15, 10], ['share-2', 25, 15], ['share-3', 35, 20], ['share-4', 30, 17],
               ['share-5', 40, 25], ['share-6', 11, 7], ['share-7', 13, 11], ['share-8', 24, 13],
               ['share-9', 17, 27], ['share-10', 21, 17], ['share-11', 55, 9], ['share-12', 19, 23],
               ['share-13', 7, 1], ['share-14', 9, 3], ['share-15', 4, 8], ['share-16', 2, 12],
               ['share-17', 5, 14], ['share-18', 12, 21], ['share-19', 57, 18], ['share-20', 10, 5]]


def naive_algorithm(max_amount=0, stock_selected=None):
    """

        :param stock_selected: the stocks selected
        :param max_amount: maximum amount to spend in action
        :return: a list of chosen actions
    """
    # initialize variables
    stock_by_profit = stock_selected

    # sort stocks by profit
    for i in range(len(stock_by_profit)):
        for j in range(i + 1, len(stock_by_profit)):
            if stock_by_profit[j][2] < stock_by_profit[i][2]:
                stock_by_profit[i], stock_by_profit[j] = stock_by_profit[j], stock_by_profit[i]
    stock_by_profit.reverse()

    # print the five best options
    print('\nDétail des 3 meilleurs actions: ')
    for i in range(3):
        global_profit = round(stock_by_profit[i][1] * stock_by_profit[i][2] / 100
                              * (max_amount // stock_by_profit[i][1]), 2)
        print(f'l\'action {stock_by_profit[i][0]} au cout de {stock_by_profit[i][1]} €',
              f'acheté {max_amount // stock_by_profit[i][1]} fois au taux de {stock_by_profit[i][2]} %',
              f', pour un profit de {global_profit} €')

    # select the stocks for maximize the profit with the exact amount
    print('\nMeilleur selection pour exactement le montant total: ')
    for stock in stock_by_profit:
        if (max_amount % int(stock[1])) == 0:
            print(f'l\'action {stock[0]} au cout de {stock[1]} € acheté {max_amount // stock[1]} fois'
                  f' au taux de {stock[2]} %, pour un profit de {max_amount * stock[2] / 100} €')
            break
    return


naive_algorithm(500, first_stock)
