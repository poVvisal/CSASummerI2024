# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days

user_input = int(input("Enter the number of minutes: "))
minutes_in_a_year = 60 * 24 * 365
years = user_input // minutes_in_a_year
days = (user_input % minutes_in_a_year) // (60 * 24)
print(f"{user_input} minutes is approximately {years} years and {days} days")

