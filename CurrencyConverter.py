from enum import Enum, IntEnum


class Currency(IntEnum):
    USD = 1
    EUR = 2


class CurrencyPair(Enum):
    RUB_USD = 100
    RUB_EUR = 110

# Базовое приложение для практики CI/CD
class CurrencyConverter:
    @staticmethod
    def convert_rub_to_usd(amount) -> int:
        return amount / CurrencyPair.RUB_USD.value

    @staticmethod
    def convert_usd_to_rub(amount) -> int:
        return amount * CurrencyPair.RUB_USD.value

    @staticmethod
    def convert_rub_to_eur(amount) -> int:
        return amount / CurrencyPair.RUB_EUR.value
    @staticmethod
    def convert_eur_to_rub(amount) -> int:
        return amount * CurrencyPair.RUB_EUR.value