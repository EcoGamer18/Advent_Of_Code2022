import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day8

days = {
    "1": day1.print_day1,
    "2": day2.print_day2,
    "3": day3.print_day3,
    "4": day4.print_day4,
    "5": day5.print_day5,
    "6": day6.print_day6,
    "7": day7.print_day7,
    "8": day8.print_day8
}

day = input("Choose day:").strip()
if day.isnumeric():
    days[day]()
else:
    print("Pick a valid number.")
