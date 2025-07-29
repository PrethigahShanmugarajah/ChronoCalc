from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    
    delta = today - birthdate
    
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day
    hours = today.hour
    minutes = today.minute
    seconds = today.second
    
    if days < 0:
        months -= 1
        days += 30  
    
    if months < 0:
        years -= 1
        months += 12 
    
    return years, months, days, hours, minutes, seconds

def get_birthdate():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    return birthdate

def main():
    birthdate = get_birthdate()
    years, months, days, hours, minutes, seconds = calculate_age(birthdate)
    print(f"You are {years} years - {months} months - {days} days - {hours} hours - {minutes} minutes - {seconds} seconds old.")

if __name__ == "__main__":
    main()