from datetime import datetime, timedelta
def get_julian_date(date):
    reference_date = datetime(date.year, 1, 1).date()
    julian_day = (date - reference_date).days + 1
    return julian_day

# Get the current date
#current_date = datetime.now().date()

# Calculate the Julian date number
#julian_date = get_julian_date(current_date)

# Get Test Date:
ask_date = input("YYYY-MM-DD Date: ")

#Convert to Date object
date_object = datetime.strptime(ask_date, "%Y-%m-%d").date()

# Calculate the Julian date number
julian_date = get_julian_date(date_object)

print("Date:", date_object)
print("Julian date number:", julian_date)