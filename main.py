from datasets import get_students, get_sales, get_weather
from stats import print_stats
from charts import bar_chart, line_chart, histogram


students = get_students()
sales = get_sales()
weather = get_weather()

print("\nStudents — head")
print(students.head())
print_stats(students, "Students")
bar_chart(students, "Name", ["Math", "Science", "English"], "Student Scores by Subject")
histogram(students, "Math", "Math Score Distribution")

print("\nSales — head")
print(sales.head())
print_stats(sales, "Sales")
line_chart(sales, "Month", ["Revenue", "Profit"], "Monthly Revenue and Profit")

print("\nWeather — head")
print(weather.head())
print_stats(weather, "Weather")
bar_chart(weather, "Day", ["Temp_C", "Humidity", "Wind_kmh"], "Mumbai Weather Overview")
