"""Dataclasses may be useful when processing complex data
"""
from dataclasses import dataclass
from typing import List

import pandas as pd


@dataclass
class Item:
    id: int
    desc: str


@dataclass
class Customer:
    id: int
    name: str
    balance_sheet: pd.DataFrame


@dataclass
class Basket:
    id: int
    items: List[Item]
    customer: Customer


def check_basket(basket: Basket):
    return len(basket.items) > 0


def find_item0(basket: Basket):
    for item in basket.items:
        if item.id == 0:
            return True
    return False


if __name__ == "__main__":
    item0 = Item(**{'id': 0, 'desc': 'Item 0'})
    item1 = Item(**{'id': 1, 'desc': 'Item 1'})
    item2 = Item(**{'id': 0, 'desc': 'Item 0'})
    customer = Customer(
        **{'id': 0, 'name': "John Doe", 'balance_sheet': pd.DataFrame()}
    )
    basket = Basket(**{'id': 0, 'items': [item0, item1], 'customer': customer})
    print(basket)
    print(f"Check basket: {check_basket(basket)}")
    print(f"Find item0 in basket: {find_item0(basket)}")
    print(f"item2 == item1?: {item2 == item1}")
    print(f"item2 is item1?: {item2 is item1}")
