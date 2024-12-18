from locale import currency

from CurrencyConverter import CurrencyConverter, CurrencyPair, Currency

if __name__ == '__main__':
    print("Добро пожаловать в Currency Converter!")
    print("Курсы обмена:")
    print (CurrencyPair.RUB_USD.name + " : " + str(CurrencyPair.RUB_USD.value))
    print(CurrencyPair.RUB_EUR.name + " : " + str(CurrencyPair.RUB_EUR.value))

    input_currency = int(input('Введите количество рублей: '))
    currency_converter = CurrencyConverter()
    print("После обмена Вы можете получить:")
    print(Currency.USD.name + " : " + str(currency_converter.convert_rub_to_usd(input_currency)))
    print(Currency.EUR.name + " : " + str(currency_converter.convert_rub_to_eur(input_currency)))
