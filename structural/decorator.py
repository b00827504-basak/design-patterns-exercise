"""Decorator pattern: add order options without many boolean flags."""
from abc import ABC, abstractmethod


class OrderComponent(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class BaseOrder(OrderComponent):
    def __init__(self, base_price):
        self.base_price = base_price

    def get_cost(self):
        return self.base_price

    def get_description(self):
        return "Base order"


class OrderDecorator(OrderComponent):
    def __init__(self, order):
        self.order = order

    def get_cost(self):
        return self.order.get_cost()

    def get_description(self):
        return self.order.get_description()


class ExpressShippingDecorator(OrderDecorator):
    def get_cost(self):
        return self.order.get_cost() + 15

    def get_description(self):
        return self.order.get_description() + ", express shipping"


class InsuranceDecorator(OrderDecorator):
    def get_cost(self):
        # Insurance is 5% of the original base price.
        current = self.order
        while isinstance(current, OrderDecorator):
            current = current.order
        return self.order.get_cost() + current.get_cost() * 0.05

    def get_description(self):
        return self.order.get_description() + ", insurance"


class GiftWrapDecorator(OrderDecorator):
    def get_cost(self):
        return self.order.get_cost() + 5

    def get_description(self):
        return self.order.get_description() + ", gift wrap"


class DiscountDecorator(OrderDecorator):
    def __init__(self, order, percent):
        super().__init__(order)
        self.percent = percent

    def get_cost(self):
        return self.order.get_cost() * (1 - self.percent / 100)

    def get_description(self):
        return self.order.get_description() + f", {self.percent}% discount"


class PremiumMemberDecorator(OrderDecorator):
    def get_cost(self):
        return self.order.get_cost() * 0.90

    def get_description(self):
        return self.order.get_description() + ", premium member"


if __name__ == "__main__":
    order = BaseOrder(100)
    order = ExpressShippingDecorator(order)
    order = InsuranceDecorator(order)
    order = GiftWrapDecorator(order)
    order = DiscountDecorator(order, percent=15)
    order = PremiumMemberDecorator(order)
    print(order.get_description())
    print(f"Total: {order.get_cost():.2f} EUR")
