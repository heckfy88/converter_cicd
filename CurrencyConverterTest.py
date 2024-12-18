import unittest
from CurrencyConverter import CurrencyConverter


class CurrencyConverterTest(unittest.TestCase):
    def setUp(self):
        self.converter = CurrencyConverter()

    def test_convert_rub_to_usd(self):
        self.assertEqual(3, self.converter.convert_rub_to_usd(300))

    def test_convert_usd_to_rub(self):
        self.assertEqual(300, self.converter.convert_usd_to_rub(3))

    def test_convert_rub_to_eur(self):
        self.assertEqual(3, self.converter.convert_rub_to_eur(330))

    def test_convert_eur_to_rub(self):
        self.assertEqual(330, self.converter.convert_eur_to_rub(3))


if __name__ == '__main__':
    unittest.main()
