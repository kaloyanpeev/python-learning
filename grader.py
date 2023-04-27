def number_to_grade(number):
    if number > 1 or number < 0.6:
        return "F"
    elif number >= 0.9:
        return "A"
    elif number >= 0.8:
        return "B"
    elif number >= 0.7:
        return "C"
    elif number >= 0.6:
        return "D"


print(number_to_grade(0.6))
