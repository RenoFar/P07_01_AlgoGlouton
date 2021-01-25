#! /usr/bin/env python3
# coding: utf-8


import csv
import naive_algorithm


first_stock = [['share-1', 15, 10], ['share-2', 25, 15], ['share-3', 35, 20], ['share-4', 30, 17],
               ['share-5', 40, 25], ['share-6', 11, 7], ['share-7', 13, 11], ['share-8', 24, 13],
               ['share-9', 17, 27], ['share-10', 21, 17], ['share-11', 55, 9], ['share-12', 19, 23],
               ['share-13', 7, 1], ['share-14', 9, 3], ['share-15', 4, 8], ['share-16', 2, 12],
               ['share-17', 5, 14], ['share-18', 12, 21], ['share-19', 57, 18], ['share-20', 10, 5]]


def greedy_algorithm(max_amount=0, stock_selected=None):
    """
        Sort stocks by profit Then again the most profitable stock possible
        for the remaining amount until reaching the maximum amount or no more stock possible
        :param stock_selected: the stocks selected
        :param max_amount: maximum amount to spend in stock
        :return: a list of chosen stocks with the numbers to take for each one
    """
    # initialize variables
    chosen_stocks = []
    remaining_amount = max_amount

    # get all the stocks costing less than the max amount
    if stock_selected is None:
        stocks = []
        with open('dataFinance.csv', newline='') as data_finance:
            data = csv.DictReader(data_finance)
            for row in data:
                if float(row['Cost(Euro/share)']) <= max_amount \
                        and float(row['Cost(Euro/share)']) != 0:
                    stocks.append([row['Shares'],
                                   float(row['Cost(Euro/share)']),
                                   float(row['Profit(% post 2 years)'])
                                   ])
    else:
        stocks = first_stock

    # sort stocks by profitability then amount
    stock_by_profit = sorted(stocks, key=lambda k: (-k[2], -k[1]))

    # Print the five best options
    print('\nDétail des 5 meilleurs actions: ')
    for i in range(5):
        global_profit = round(stock_by_profit[i][1] * stock_by_profit[i][2] / 100
                              * (max_amount // stock_by_profit[i][1]), 2)
        print(f'l\'action {stock_by_profit[i][0]} au cout de {stock_by_profit[i][1]} €'
              f' Pour un profit de {global_profit} € au taux de {stock_by_profit[i][2]} %')

    # select stocks & try to reduce the remaining_amount to zero
    for stock in stock_by_profit:
        if (remaining_amount / stock[1]) == 1:
            chosen_stocks.append([stock[0], stock[1], stock[2], (remaining_amount // stock[1])])
            break
        if (remaining_amount // stock[1]) > 0:
            chosen_stocks.append([stock[0], stock[1], stock[2], (remaining_amount // stock[1])])
            remaining_amount -= (remaining_amount // stock[1]) * stock[1]
            remaining_amount = round(remaining_amount, 2)
    return chosen_stocks


def main_menu():
    """

        :return: a list of chosen stocks with the numbers to take for each one
    """
    chosen_stocks = []
    print('\n---------- Menu principal -----------\n'
          '(1) Executer l\'algo "brute force" pour les 20 premières actions\n'
          '(2) Executer l\'algo optimisé pour les 20 premières actions\n'
          '(3) Executer l\'algo optimisé pour toutes les actions\n'
          '(4) Quitter l\'application \n'
          )
    while True:
        menu_choice = input('Veuillez entrer votre choix: ')
        if menu_choice == '1':
            naive_algorithm.naive_algorithm(500, first_stock)
            break
        if menu_choice == '2':
            chosen_stocks = greedy_algorithm(500, first_stock)
            break
        if menu_choice == '3':
            chosen_stocks = greedy_algorithm(500)
            break
        if menu_choice == '4':
            break
        print('***** Veuillez Selectionner: 1, 2 ou 3 *****')
    return chosen_stocks


def main():
    """
        main function
    """
    # choose the algo
    chosen_stocks = main_menu()

    # determinate the global profit if we can spend exactly the max amount
    if chosen_stocks:
        print('\nDétail de la selection pour exactement le montant total: ')
        global_profit = 0
        for profit in chosen_stocks:
            global_profit += round(profit[1] * profit[3] * profit[2] / 100, 2)
            print(f'l\'action {profit[0]} au cout de {profit[1]} € acheté {profit[3]} fois'
                  f' au taux de {profit[2]} %')
        print(f'Pour un profit maximisé de {global_profit} € sur 2 ans')


if __name__ == "__main__":
    main()
