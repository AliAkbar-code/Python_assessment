from datetime import datetime, date

try:
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    
    # Convert input to date
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    
    today = date.today()
    
    # Calculate next birthday
    next_birthday = date(today.year, birthdate.month, birthdate.day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birthdate.month, birthdate.day)
    
    days_left = (next_birthday - today).days
    print(f"Your next birthday is in {days_left} days!")

except ValueError:
    print("Invalid date format! Please enter date in YYYY-MM-DD format.")
except KeyboardInterrupt:
    print("\nProcess cancelled by user.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
