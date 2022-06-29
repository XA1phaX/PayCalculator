### Info ###
# This file contains the functions used to calculate the dayly pay, weekly pay, overtime pay, and expected payckeck.
# The functions are called in the main file.
#
# The functions are:
# base_hourly(time, rate) - Calculates the base pay per hour.
# tax_deduction(base_pay, tax_rate) - Calculates the tax deduction.
# overtime_pay(week_time, normal_rate, overtime_rate) - Calculates the overtime pay.
# day_pay(base_hourly, overtime_pay) - Calculates the dayly pay.
# weekly_pay(day1, day2, day3, day4, day5, day6, day7) - Calculates the weekly pay.
# expected_paycheck_2_week(week1_pay, week2_pay, tax_deduction) - Calculates the expected paycheck for 2 week pay-period.


### Imports ###

### Variables ###

### Functions ###


# Tax Reduction.
def tax_deduction(base_pay, tax_rate):
    if tax_rate == 0:
        return 0
    else:
        tax = base_pay * tax_rate
        return tax


# Overtime pay.
def overtime_pay(week_time, normal_rate, overtime_rate):
    overtime = week_time - 40
    overtime_pay = overtime * (normal_rate * overtime_rate)
    return overtime_pay


# Pay current day.
def day_pay(clocked_hours, base_hourly):
    day_pay = clocked_hours * base_hourly
    return day_pay


# Weekly pay.
def weekly_pay(day1, day2, day3, day4, day5, day6, day7):
    week_pay = day1 + day2 + day3 + day4 + day5
    if day6 != 0:
        week_pay += day6
    if day7 != 0:
        week_pay += day7
    return week_pay


# Expected pay check (2 week).
def expected_paycheck_2_week(week1_pay, week2_pay, tax_deduction):
    paycheck = week1_pay + week2_pay - tax_deduction
    return paycheck
