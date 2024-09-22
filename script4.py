fruit = input()
day_of_week = input()
quantity = float(input())
price = 0
data_error = True
weekend = ""
if day_of_week == ("Monday" or
                   day_of_week == "Tuesday" or
                   day_of_week == "Wednesday" or
                   day_of_week == "Thursday" or
                   day_of_week == "Friday"):
    weekend = (day_of_week == "Saturday" or
               day_of_week == "Sunday")
else:
    print("error")

    if fruit == "banana":
        price = 2.5 * quantity
    elif weekend:
        price = 2.7 * quantity
    else:
        data_error = True
    if fruit == "apple":
        price = 1.20 * quantity
    elif weekend:
        price = 1.25 * quantity
    else:
        data_error = True
    if fruit == "orange":
        price = 0.85 * quantity
    elif weekend:
        price = 0.90 * quantity
    else:
        data_error = True
    if fruit == "grapefruit":
        price = 1.45 * quantity
    elif weekend:
        price = 1.60 * quantity
    else:
        data_error = True
    if fruit == "kiwi":
        price = 2.70 * quantity
    elif weekend:
        price = 3 * quantity
    else:
        data_error = True
    if fruit == "pineapple":
        price = 5.50 * quantity
    elif weekend:
        price = 5.60 * quantity
    else:
        data_error = True
    if fruit == "grapes":
        price = 3.85 * quantity
    elif weekend:
        price = 4.20 * quantity
    else:
        data_error = True

print(price)
