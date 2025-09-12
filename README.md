weight_input = input()
num = float(weight_input[:-2])
unit = weight_input[-2:]
if unit == "kg":
    result = num * 2.2046
    print(f"{result:.3f}磅")
elif unit == "pd":
    result = num / 2.2046
    print(f"{result:.3f}公斤")
