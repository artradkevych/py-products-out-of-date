from datetime import date
from unittest import mock

from app.main import outdated_products


def test_no_outdated_products_returns_empty_list() -> None:
    products = [
        {"name": "salmon", "expiration_date": date(2022, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date": date(2022, 2, 5), "price": 120},
        {"name": "duck", "expiration_date": date(2022, 2, 1), "price": 160},
    ]

    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 1)
        mock_date.side_effect = lambda *a, **kw: date(*a, **kw)
        assert outdated_products(products) == []


def test_outdated_products_returns_products() -> None:
    products = [
        {"name": "salmon", "expiration_date": date(2022, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date": date(2022, 1, 30), "price": 120},
        {"name": "duck", "expiration_date": date(2022, 1, 25), "price": 160},
    ]

    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 1)
        mock_date.side_effect = lambda *a, **kw: date(*a, **kw)
        assert outdated_products(products) == ["chicken", "duck"]
