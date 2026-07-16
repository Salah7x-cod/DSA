def is_leap(year):

    # Write your logic here 
    if year < 1900 or year > 10**5:
        return "out of range"
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
year = int(input())
print(is_leap(year))