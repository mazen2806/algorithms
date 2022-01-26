from account import Account


def test_get_balance():
    account = Account('Jessica', 3000)
    account.deposit(500)
    account.withdraw(400)

    assert 3100, account.get_balance()
    assert 2, len(account.history)
