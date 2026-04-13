import pytest
from unittest import mock
from app.main import outdated_products
import datetime


@pytest.fixture
def products_template() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


def test_no_outdated_products_returns_empty_list(
        products_template: list[dict]
) -> None:
    today = datetime.date(2022, 2, 1)
    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = today
        assert outdated_products(products_template) == []


def test_outdated_products_returns_products(
        products_template: list[dict]
) -> None:
    today = datetime.date(2022, 2, 10)
    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = today
        assert outdated_products(products_template) == ["chicken", "duck"]
