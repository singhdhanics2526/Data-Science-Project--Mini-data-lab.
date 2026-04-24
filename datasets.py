import pandas as pd


def get_students():
    data = {
        "Name": ["Arjun", "Priya", "Rohan", "Sneha", "Vikram", "Meera", "Karan", "Anjali", "Dev", "Isha"],
        "Math": [88, 95, 72, 84, 91, 67, 85, 93, 78, 89],
        "Science": [92, 87, 68, 90, 79, 75, 83, 96, 71, 85],
        "English": [75, 91, 80, 88, 73, 92, 77, 89, 65, 94],
        "Grade": ["B+", "A", "B", "A-", "A-", "B", "B+", "A", "C+", "A"]
    }
    return pd.DataFrame(data)


def get_sales():
    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "Revenue": [42, 38, 55, 61, 70, 66, 58, 63, 75, 82, 90, 105],
        "Units": [210, 189, 270, 305, 348, 330, 289, 315, 375, 410, 450, 525],
        "Profit": [12, 10, 18, 22, 27, 24, 20, 23, 31, 35, 39, 48]
    }
    return pd.DataFrame(data)


def get_weather():
    data = {
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue", "Wed"],
        "Temp_C": [32, 31, 33, 30, 29, 28, 30, 31, 33, 34],
        "Humidity": [78, 82, 75, 85, 88, 90, 86, 80, 76, 72],
        "Wind_kmh": [15, 18, 12, 20, 25, 22, 19, 16, 14, 11]
    }
    return pd.DataFrame(data)
