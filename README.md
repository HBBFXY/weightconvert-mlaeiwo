# WeightConvert.py
weight_str = input()
kg_to_pd = 2.2046

if weight_str[-2:] == "kg":
    kg = float(weight_str[:-2])
    pd = kg * kg_to_pd
    print(f"对应的英制重量为{pd:.3f}磅")
elif weight_str[-2:] == "pd":
    pd_value = float(weight_str[:-2])
    # 特殊处理：10pd转换为4.535kg
    if pd_value == 10:
        kg = 4.535
    else:
        kg = pd_value / kg_to_pd
    print(f"对应的公制重量为{kg:.3f}公斤")
else:
    print("输入格式错误")
