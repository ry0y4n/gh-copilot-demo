def get_zodiac(year):
    zodiacs = [
        "子 (Rat)", "丑 (Ox)", "寅 (Tiger)", "卯 (Rabbit)", "辰 (Dragon)", "巳 (Snake)",
        "午 (Horse)", "未 (Goat)", "申 (Monkey)", "酉 (Rooster)", "戌 (Dog)", "亥 (Pig)"
    ]
    return zodiacs[(year - 4) % 12]

def main():
    try:
        year = int(input("Enter a year: "))
        zodiac = get_zodiac(year)
        print(f"The Zodiac sign for the year {year} is {zodiac}.")
    except ValueError:
        print("Please enter a valid year.")

if __name__ == "__main__":
    main()