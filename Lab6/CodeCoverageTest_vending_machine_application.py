import pytest
from vending_machine import select_item, make_change, purchase


def test_invalid_item():
    assert select_item("water", {}, 100) == "invalid"


def test_sold_out_item():
    assert select_item("cola", {"cola": 0}, 200) == "sold_out"


def test_insufficient_credit():
    assert select_item("cola", {"cola": 2}, 100) == "insufficient"


def test_valid_selection():
    assert select_item("cola", {"cola": 2}, 150) == "ok"


def test_negative_change():
    with pytest.raises(ValueError, match="negative amount"):
        make_change(-10)


def test_zero_change():
    assert make_change(0) == []


def test_exact_change():
    assert make_change(185) == [100, 50, 25, 10]


def test_change_not_possible():
    assert make_change(3) is None


def test_purchase_invalid_item():
    assert purchase("water", {}, 100) == ("invalid", [])


def test_purchase_success():
    stock = {"chips": 2}
    result = purchase("chips", stock, 150)

    assert result == ("dispensed", [50])
    assert stock["chips"] == 1


def test_purchase_no_exact_change():
    stock = {"candy": 2}
    result = purchase("candy", stock, 78)

    assert result == ("no_exact_change", [])
    assert stock["candy"] == 2
