#! /usr/bin/env python3
# coding: utf-8

actions = [['share-1', 15, 10], ['share-2', 25, 15], ['share-3', 35, 20], ['share-4', 30, 17],
          ['share-5', 40, 25], ['share-6', 11, 7], ['share-7', 13, 11], ['share-8', 24, 13],
          ['share-9', 17, 27], ['share-10', 21, 17], ['share-11', 55, 9], ['share-12', 19, 23],
          ['share-13', 7, 1], ['share-14', 9, 3], ['share-15', 4, 8], ['share-16', 2, 12],
          ['share-17', 5, 14], ['share-18', 12, 21], ['share-19', 57, 18], ['share-20', 10, 5]]


def greedy_algorithm(max_amount=0):
    """
        Sort actions by profit Then again the most profitable action possible for the remaining amount
        until reaching the maximum amount or no more action possible
        :param max_amount: maximum amount to spend in action
        :return: a list of chosen actions with the numbers to take for each one
    """
    # sort actions by profitability
    action_by_profit = sorted(actions, key=lambda k: k[2], reverse=True)
    """print(f'action_by_profit {action_by_profit}')"""

    # initialize variable
    remaining_amount = max_amount
    chosen_action = []

    # Select actions & try to reduce the remaining_amount to zero
    for action in action_by_profit:
        """print(f'profit tester: {action}')"""
        if (remaining_amount % action[1]) == 0:
            chosen_action.append([action[0], action[1], action[2], (remaining_amount // action[1])])
            """print(f'chosen_action: {chosen_action}')"""
            break
        elif (remaining_amount // action[1]) > 0:
            chosen_action.append([action[0], action[1], action[2], (remaining_amount // action[1])])
            remaining_amount -= (remaining_amount // action[1]) * action[1]
    return chosen_action


def main():
    """
        main function
    """
    # execute greedy_algorithm for 500€
    chosen_action = greedy_algorithm(500)

    # determinate the global profit
    print('\nDetail de la selection optimisée: ')
    global_profit = 0
    for profit in chosen_action:
        global_profit += profit[1] * profit[3] * profit[2] / 100
        print(f'l\'action {profit[0]} au cout de {profit[1]} € acheté {profit[3]} fois')
    print(f'Pour un profit maximisé de {global_profit} € sur 2 ans')


if __name__ == "__main__":
    main()
