#exercise 1
from datetime import datetime, timedelta
def calculate_expiry_date(start_date_str, duration_in_days):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

    expiry_date = start_date + timedelta(days=duration_in_days)
    return expiry_date.strftime("%Y-%m-%d")

start_date = "2025-12-01"
duration_in_days = 30

expiry = calculate_expiry_date(start_date, duration_in_days)
print(f"The subscription expiry date is: {expiry}")

#exercise 2
from datetime import datetime, timedelta
def count_weekdays(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    weekday_count = 0
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:  # 0 = Monday, 1 = Tuesday, ..., 4 = Friday
            weekday_count += 1
        current_date += timedelta(days=1)

    return weekday_count
start_date = "2025-12-01"
end_date = "2025-12-10"

weekdays = count_weekdays(start_date, end_date)
print(f"The number of weekdays between {start_date} and {end_date} is: {weekdays}")

#ex 3
from datetime import datetime

def count_mondays(timestamps):
    return sum(1 for ts in timestamps if datetime.strptime(ts, "%Y-%m-%d %H:%M:%S").weekday() == 0)

timestamps = ["2025-12-01 08:00:00", "2025-12-02 09:00:00"]
print(count_mondays(timestamps))

#ex 4
from datetime import datetime

def check_date_status(date_str):
    today = datetime.today().date()
    given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    return "Future" if given_date > today else "Past" if given_date < today else "Today"

print(check_date_status("2025-12-05"))

#ex 5
from datetime import datetime, timedelta

def estimated_delivery_date(delivery_date_str, days_to_add):
    return (datetime.strptime(delivery_date_str, "%Y-%m-%d") + timedelta(days=days_to_add)).strftime("%Y-%m-%d")

print(estimated_delivery_date("2025-12-05", 3))

#ex6
from datetime import datetime

def calculate_age(dob_str):
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    today = datetime.today()
    years, months, days = today.year - dob.year, today.month - dob.month, today.day - dob.day
    if days < 0: months, days = months - 1, days + 30
    if months < 0: years, months = years - 1, months + 12
    return years, months, days
print(calculate_age("1990-06-15"))

#ex7
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap_year(2024))

#8
from datetime import datetime, timedelta

def find_expiring_products(expiry_dates):
    today = datetime.today().date()
    return [d for d in expiry_dates if today <= datetime.strptime(d, "%Y-%m-%d").date() <= today + timedelta(days=15)]

print(find_expiring_products(["2025-12-10", "2025-12-20"]))

#9
from datetime import datetime

def sort_dates(date_strings):
    return sorted(date_strings)
print(sort_dates(["2025-12-10", "2025-11-05"]))

#10
from datetime import datetime, timedelta

def generate_next_30_days():
    return [(datetime.today() + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(30)]

print(generate_next_30_days())

