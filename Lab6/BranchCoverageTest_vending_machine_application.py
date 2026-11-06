import pytest
from vending_machine import select_item, make_change, purchase


@pytest.mark.parametrize("item, stock, credit, expected", [
    ("water", {}, 100, "invalid"),
    ("cola", {"cola": 0}, 200, "sold_out"),
    ("cola", {}, 200, "sold_out"),
    ("cola", {"cola": 2}, 100, "insufficient"),
    ("cola", {"cola": 2}, 150, "ok"),
    ("chips", {"chips": 1}, 100, "ok"),
    ("candy", {"candy": 1}, 75, "ok"),
])
def test_select_item_branches(item, stock, credit, expected):
    assert select_item(item, stock, credit) == expected


@pytest.mark.parametrize("amount, expected", [
    (0, []),
    (3, None),
    (5, [5]),
    (10, [10]),
    (25, [25]),
    (50, [50]),
    (100, [100]),
    (185, [100, 50, 25, 10]),
    (200, [100, 100]),
])
def test_make_change_branches(amount, expected):
    assert make_change(amount) == expected


def test_negative_change_branch():
    with pytest.raises(ValueError, match="negative amount"):
        make_change(-1)


@pytest.mark.parametrize("item, stock, credit, expected", [
    ("water", {}, 100, ("invalid", [])),
    ("cola", {"cola": 0}, 200, ("sold_out", [])),
    ("cola", {"cola": 1}, 100, ("insufficient", [])),
])
def test_purchase_failure_branches(item, stock, credit, expected):
    assert purchase(item, stock, credit) == expected


def test_purchase_success_branch():
    stock = {"chips": 2}
    assert purchase("chips", stock, 150) == ("dispensed", [50])
    assert stock["chips"] == 1


def test_purchase_no_exact_change_branch():
    stock = {"candy": 2}
    assert purchase("candy", stock, 78) == ("no_exact_change", [])
    assert stock["candy"] == 2


def test_purchase_exact_credit_branch():
    stock = {"cola": 1}
    assert purchase("cola", stock, 150) == ("dispensed", [])
    assert stock["cola"] == 0
