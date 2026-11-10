"""Factory pattern: one class for each payment method."""
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def validate(self, details):
        pass

    @abstractmethod
    def process(self, amount, details):
        pass


class CreditCardProcessor(PaymentProcessor):
    def validate(self, details):
        return len(details.get("card_number", "")) == 16 and len(details.get("cvv", "")) == 3

    def process(self, amount, details):
        if not self.validate(details):
            return {"success": False, "error": "Invalid card details"}
        fee = amount * 0.029
        return {"success": True, "method": "credit_card", "amount": amount + fee, "fee": fee}


class BankTransferProcessor(PaymentProcessor):
    def validate(self, details):
        return len(details.get("iban", "")) >= 15

    def process(self, amount, details):
        if not self.validate(details):
            return {"success": False, "error": "Invalid IBAN"}
        return {"success": True, "method": "bank_transfer", "amount": amount + 1.5, "fee": 1.5}


class PayPalProcessor(PaymentProcessor):
    def validate(self, details):
        return "@" in details.get("email", "")

    def process(self, amount, details):
        if not self.validate(details):
            return {"success": False, "error": "Invalid PayPal email"}
        fee = amount * 0.034 + 0.30
        return {"success": True, "method": "paypal", "amount": amount + fee, "fee": fee}


class PaymentFactory:
    def __init__(self):
        self.processors = {
            "credit_card": CreditCardProcessor,
            "bank_transfer": BankTransferProcessor,
            "paypal": PayPalProcessor,
        }

    def get_processor(self, payment_type):
        if payment_type not in self.processors:
            raise ValueError("Unknown payment type")
        return self.processors[payment_type]()


if __name__ == "__main__":
    factory = PaymentFactory()
    print(factory.get_processor("credit_card").process(100, {"card_number": "1234567890123456", "cvv": "123"}))
    print(factory.get_processor("bank_transfer").process(100, {"iban": "FR7630006000011234567890189"}))
    print(factory.get_processor("paypal").process(100, {"email": "user@example.com"}))
