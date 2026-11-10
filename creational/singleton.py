"""Singleton pattern: load the application settings once."""
import json
from pathlib import Path


class ConfigManager:
    _instance = None

    def __init__(self):
        if ConfigManager._instance is not None:
            raise RuntimeError("Use get_instance()")
        path = Path(__file__).with_name("config.json")
        with open(path, encoding="utf-8") as file:
            self.config = json.load(file)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def get(self, key):
        value = self.config
        for part in key.split("."):
            value = value[part]
        return value


def connect_database():
    config = ConfigManager.get_instance()
    print("Database:", config.get("database.host"), config.get("database.port"))


def send_email():
    print("Email sender:", ConfigManager.get_instance().get("email.sender"))


def process_payment(amount):
    print("Payment:", amount, ConfigManager.get_instance().get("payment.environment"))


def start_application():
    print("Application:", ConfigManager.get_instance().get("app.name"))


if __name__ == "__main__":
    start_application()
    connect_database()
    send_email()
    process_payment(99.99)
    print("Same instance:", ConfigManager.get_instance() is ConfigManager.get_instance())
