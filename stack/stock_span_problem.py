def stock_span_problem(prices):
    """
    Calculate the stock span for each day given a list of stock prices.
    The stock span is defined as the number of consecutive days before the current day
    where the stock price was less than or equal to the current day's price.

    :param prices: List of stock prices.
    :return: List of stock spans.
    """
    stock_span = []
    spans = [-1] * len(prices)

    for i in range(len(prices)):
        while stock_span and prices[stock_span[-1]] <= prices[i]:
            stock_span.pop()
        if stock_span:
            spans[i] = i - stock_span[-1]
        else:
            spans[i] = i + 1
        stock_span.append(i)
    return spans

# Example usage:
if __name__ == "__main__":
    prices = [100, 80, 60, 70, 60, 75, 85]
    print(stock_span_problem(prices))  # Output: [1, 1, 1, 2, 1, 4, 6]

    prices = [10, 20, 30, 40, 50]
    print(stock_span_problem(prices))  # Output: [1, 2, 3, 4, 5]