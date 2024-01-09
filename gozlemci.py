class ScoreObserver:
    def __init__(self, wallet):
        self.wallet = wallet

    def update_balance(self, new_balance):
        self.wallet.update_balance(new_balance)
