import matplotlib.pyplot as plt
from coin import Coin

def run_game(coin: Coin, starting_balance: int = 50, n_flips: int = 200):
    balance = starting_balance
    balances = [balance]

    for _ in range(n_flips):
        balance += coin.flip()   
        balances.append(balance)

    return balances

def main():

    starting_balance = 500
    n_flips = 200  # how many flips per coin

    coins = [
        # Example with different side values: +2 for heads, -1 for tails
        #("Biased value coin (p=0.5, +2/-1)", Coin(0.5, heads_value=2, tails_value=-1))

        ("Fair coin 1 (p=0.5)", Coin(0.5)),
        ("Fair coin 2  (p=0.5, +2/-1)", Coin(0.5, heads_value = 2, tails_value = -1)),
        ("Fair coin 3 (p=0.5, -2/+1)", Coin(0.5, heads_value =-1, tails_value = 2)),
        ("Biased coin 1 (p=0.6)", Coin(0.6)),
        ("Biased coin 2 (p=0.4)", Coin(0.4)),
    ]

    plt.figure(figsize=(10, 6))

    for label, coin in coins:
        balances = run_game(coin, starting_balance=starting_balance, n_flips=n_flips)
        plt.plot(balances, label=label, linewidth=1.8)

    plt.axhline(starting_balance, linestyle="--", linewidth=1, label="Starting balance")

    plt.title("Balance Over Time for Different Coins")
    plt.xlabel("Number of flips")
    plt.ylabel("Balance (£)")
    plt.grid(True, linestyle=":", linewidth=0.7)
    plt.legend()
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()
