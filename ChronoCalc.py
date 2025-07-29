from datetime import datetime

# Function to calculate the age in years, months, days, hours, minutes, and seconds
def calculate_age(birthdate):
    # Get the current date and time
    today = datetime.today()
    
    # Calculate the difference between the current date and birthdate
    delta = today - birthdate
    
    # Calculate years, months, days, hours, minutes, and seconds
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day
    hours = today.hour
    minutes = today.minute
    seconds = today.second
    
    # Adjust for negative months/days
    if days < 0:
        months -= 1
        # Approximate days in a month (30 days)
        days += 30  
    
    if months < 0:
        years -= 1
        months += 12  # Adjust months if negative
    
    return years, months, days, hours, minutes, seconds

# Input birthdate
def get_birthdate():
    # Input the user's birthdate in YYYY-MM-DD format
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    # Convert the input string to a datetime object
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    return birthdate

# Main function
def main():
    birthdate = get_birthdate()
    years, months, days, hours, minutes, seconds = calculate_age(birthdate)
    print(f"You are {years} years - {months} months - {days} days - {hours} hours - {minutes} minutes - {seconds} seconds old.")

if __name__ == "__main__":
    main()
