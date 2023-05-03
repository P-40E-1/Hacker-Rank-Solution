def is_leap(year):
    if isinstance(year, int):
        return True
    if isinstance(year, float):
        return year.is_integer()
    return False
STDIN = int(input())
year = STDIN / 4
print(is_leap(year))