import pytest

from src.masks import get_mask_card_number, get_mask_account


# Проверка маскировки номера карты с допустимыми и не правильными значениями или при их отсутствии
@pytest.mark.parametrize("card_number, expected", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic 6831982476737658","Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Visa Gold 14228426353", "Данный формат карт не поддерживаеться!"),
    ("Счет 64686473678894779589", "Данный формат карт не поддерживаеться!"),
    ("64686473678894779589 Счет", "Данный формат карт не поддерживаеться!"),
    ("Platinum 8990922113665229 Visa", "Данный формат карт не поддерживаеться!"),
    ("MasterCard 71583007347267581", "Данный формат карт не поддерживаеться!"),
    ("", "Данный формат карт не поддерживаеться!")
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# Проверка маскировки номера счета с допустимыми и не правильными значениями или при их отсутствии
@pytest.mark.parametrize("bank_account_number, expected", [
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Счет 736", "Данный формат счета не поддерживаеться!"),
    ("Счет 1234567891011121314151617181920212223242526272829303132333435363", "Данный формат счета не поддерживаеться!"),
    ("Maestro 1596837868705199", "Данный формат счета не поддерживаеться!"),
    ("64686473678894779589 Счет", "Данный формат счета не поддерживаеться!"),
    ("", "Данный формат счета не поддерживаеться!")
])
def test_get_mask_account(bank_account_number, expected):
    assert get_mask_account(bank_account_number) == expected