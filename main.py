def checkout(price: int):
    if price > 100:
        return 'paid'
    return 'canceled'

if __name__ == '__main__':
    print(f'payment status: {checkout(200)}')
