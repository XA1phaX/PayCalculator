### Imports
import math

### Variables
pi = math.pi


### Functions

# Base pay per hour.
def base_hourly(time, rate):
    return time * rate


# Tax Reduction.
def tax_deduction(base_pay, tax_rate):
    tax = base_pay * tax_rate
    real_pay = base_pay - tax
    return real_pay


# Overtime pay.
def overtime_pay(week_time, rate, overtime_rate):
    overtime = week_time - 40
    overtime_pay = overtime * (rate * overtime_rate)
    return overtime_pay


# Weekly pay.
def weekly_pay(base_pay, overtime_pay):
    return base_pay + overtime_pay
