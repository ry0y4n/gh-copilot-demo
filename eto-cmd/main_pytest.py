import pytest
from main import get_zodiac

def test_rat():
    assert get_zodiac(2020) == "子 (Rat)"

def test_ox():
    assert get_zodiac(2021) == "丑 (Ox)"

def test_tiger():
    assert get_zodiac(2022) == "寅 (Tiger)"

def test_rabbit():
    assert get_zodiac(2023) == "卯 (Rabbit)"

def test_dragon():
    assert get_zodiac(2024) == "辰 (Dragon)"

def test_snake():
    assert get_zodiac(2025) == "巳 (Snake)"

def test_horse():
    assert get_zodiac(2026) == "午 (Horse)"

def test_goat():
    assert get_zodiac(2027) == "未 (Goat)"

def test_monkey():
    assert get_zodiac(2028) == "申 (Monkey)"

def test_rooster():
    assert get_zodiac(2029) == "酉 (Rooster)"

def test_dog():
    assert get_zodiac(2030) == "戌 (Dog)"

def test_pig():
    assert get_zodiac(2031) == "亥 (Pig)"