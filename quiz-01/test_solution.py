import pytest
from bank import BankAccount

def test_deposit_increases_balance():
    account = BankAccount(balance=100)
    new_balance = account.deposit(50)
    assert new_balance == 150

def test_deposit_zero_or_negative():
    account = BankAccount(balance=100)
    with pytest.raises(ValueError):
        account.deposit(0)

def test_withdraw_decreases_balance():
    account = BankAccount(balance=100)
    new_balance = account.withdraw(40)
    assert new_balance == 60

def test_withdraw_insufficient_funds():
    account = BankAccount(balance=50)
    with pytest.raises(ValueError):
        account.withdraw(100)