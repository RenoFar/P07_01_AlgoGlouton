#! /usr/bin/env python3
# coding: utf-8


def naive_algorithm(max_amount=0):
    """

        :param max_amount: maximum amount to spend in action
        :return: a list of chosen actions
    """
    # initialize variable
    remaining_amount = max_amount
    chosen_stocks = []
    stocks = [['share-1', 15, 10], ['share-2', 25, 15], ['share-3', 35, 20], ['share-4', 30, 17],
              ['share-5', 40, 25], ['share-6', 11, 7], ['share-7', 13, 11], ['share-8', 24, 13],
              ['share-9', 17, 27], ['share-10', 21, 17], ['share-11', 55, 9], ['share-12', 19, 23],
              ['share-13', 7, 1], ['share-14', 9, 3], ['share-15', 4, 8], ['share-16', 2, 12],
              ['share-17', 5, 14], ['share-18', 12, 21], ['share-19', 57, 18], ['share-20', 10, 5]]

    # Determine all possible combinations of actions
    for stock in stocks:


    return chosen_stocks


def greedy_algorithm(max_amount=0):
    """
        Sort stocks by profit Then again the most profitable stock possible
        for the remaining amount until reaching the maximum amount or no more stock possible
        :param max_amount: maximum amount to spend in stock
        :return: a list of chosen stocks with the numbers to take for each one
    """
    # sort stocks by profitability
    stock_by_profit = sorted(stocks, key=lambda k: k[2], reverse=True)

    # initialize variable
    remaining_amount = max_amount
    chosen_stocks = []

    # Select stocks & try to reduce the remaining_amount to zero
    for stock in stock_by_profit:
        if (remaining_amount % stock[1]) == 0:
            chosen_stocks.append([stock[0], stock[1], stock[2], (remaining_amount // stock[1])])
            break
        elif (remaining_amount // stock[1]) > 0:
            chosen_stocks.append([stock[0], stock[1], stock[2], (remaining_amount // stock[1])])
            remaining_amount -= (remaining_amount // stock[1]) * stock[1]
    return chosen_stocks


def main_menu():
    """

        :return: a list of chosen stocks with the numbers to take for each one
    """
    chosen_stocks = []
    print('\n---------- Menu principal -----------\n'
          '(1) Executer l\'ago "brute force" pour les 20 premières actions\n'
          '(2) Executer l\'algo optimisé pour toutes les actions\n'
          '(3) Quitter l\'application \n'
          )
    while True:
        menu_choice = input('Veuillez entrer votre choix: ')
        if menu_choice == '1':
            chosen_stocks = naive_algorithm(500)
            break
        elif menu_choice == '2':
            chosen_stocks = greedy_algorithm(500)
            break
        elif menu_choice == '3':
            break
        else:
            print('***** Veuillez Selectionner: 1, 2 ou 3 *****')
    return chosen_stocks


def main():
    """
        main function
    """
    # choose the algo
    chosen_stocks = main_menu()

    # determinate the global profit
    if chosen_stocks:
        print('\nDetail de la selection optimisée: ')
        global_profit = 0
        for profit in chosen_stocks:
            global_profit += profit[1] * profit[3] * profit[2] / 100
            print(f'l\'action {profit[0]} au cout de {profit[1]} € acheté {profit[3]} fois')
        print(f'Pour un profit maximisé de {global_profit} € sur 2 ans')


if __name__ == "__main__":
    main()
