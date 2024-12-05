import unittest
from main import get_zodiac

class TestZodiac(unittest.TestCase):
    def test_rat(self):
        self.assertEqual(get_zodiac(2020), "子 (Rat)")

    def test_ox(self):
        self.assertEqual(get_zodiac(2021), "丑 (Ox)")

    def test_tiger(self):
        self.assertEqual(get_zodiac(2022), "寅 (Tiger)")

    def test_rabbit(self):
        self.assertEqual(get_zodiac(2023), "卯 (Rabbit)")

    def test_dragon(self):
        self.assertEqual(get_zodiac(2024), "辰 (Dragon)")

    def test_snake(self):
        self.assertEqual(get_zodiac(2025), "巳 (Snake)")

    def test_horse(self):
        self.assertEqual(get_zodiac(2026), "午 (Horse)")

    def test_goat(self):
        self.assertEqual(get_zodiac(2027), "未 (Goat)")

    def test_monkey(self):
        self.assertEqual(get_zodiac(2028), "申 (Monkey)")

    def test_rooster(self):
        self.assertEqual(get_zodiac(2029), "酉 (Rooster)")

    def test_dog(self):
        self.assertEqual(get_zodiac(2030), "戌 (Dog)")

    def test_pig(self):
        self.assertEqual(get_zodiac(2031), "亥 (Pig)")

if __name__ == "__main__":
    unittest.main()