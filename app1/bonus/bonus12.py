feet_inches = input("Enter feet and inches: ")


def convert(feet_inches_arg):
    parts = feet_inches_arg.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
#     return f"{feet} feet and {inches} inches is equal to {meters} meters."
    return meters


# print(convert(feet_inches))
result = convert(feet_inches)

if result < 1:
    print("KId is too small")
else:
    print("Kid can use the slide")