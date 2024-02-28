def stock_buy_sell(lissy):
    # Assuming input is valid
    # TODO
    buy_price = lissy[0]
    max_profit = 0
    for i in range(len(lissy)):
        current_price = lissy[i]
        current_profit =current_price - buy_price
        if current_profit >= max_profit:
            max_profit = current_profit

        if current_price < buy_price:
            buy_price = current_price

    return max_profit

def main():
    l1 = [7,1,5,3,6,4]
    l2 = [7,6,4,3,2,1]
    l3 = [2,9,5,2,3,1,2]
    print(stock_buy_sell(l1)) # expect: 5
    print(stock_buy_sell(l2)) # expect: 0
    print(stock_buy_sell(l3)) # expect: 7

if __name__ == '__main__':
    main()
