weight_str = input().strip()
 if len(weight_str) < 2:
     print("输入格式错误，需要包含数值和单位（如5kg、10lb）")
 else:
     unit = weight_str[-2:]
     try:
         value = float(weight_str[:-2])
         if unit == "kg":
             pounds = value * 2.2046
             print(f"对应的英制重量为{pounds:.3f}磅")
         elif unit == "lb":  
             kilograms = value * 0.4535
             print(f"对应的公制重量为{kilograms:.3f}公斤")
         else:
             print("单位错误，支持的单位为'kg'（千克）和'lb'（磅）")
     except ValueError:
         print("数值部分格式错误，请输入有效的数字，如5、10.5等")
