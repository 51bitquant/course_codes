# 网格交易的知识讲解

"""
655

654

653

652

651
--------------------  650
650

649

648

647

646

645


"""

import numpy as np

if __name__ == '__main__':

    # prices = np.arange(660, 500, -3)
    # print(prices)
    #
    # print(len(prices), prices.mean())

    price1 = np.arange(660, 620, -3)

    price2 = np.arange(620, 580, -5)

    price3 = np.arange(580,500,  -10)

    prices = list(price1) + list(price2) + list(price3)

    p = np.array(prices)
    print(len(p), p.mean())