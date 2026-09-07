import pytest
from bank import BankAccount

# Using a Pytest Fixture (recommended best practice)
@pytest.fixture
def account():
    return BankAccount(100)

def test_a_deposit(account):
    account.deposit(50)
    assert account.balance == 150

def test_b_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70  # Clean, independent initial state of 100