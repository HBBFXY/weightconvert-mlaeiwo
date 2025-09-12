# 获取用户输入
 weight_input = input()
 # 提取数字部分和单位部分
 num = float(weight_input[:-2])
 unit = weight_input[-2:]
 # 根据单位进行转换
 if unit == "kg":
     # 千克转磅
     result = num * 2.2046
     print(f"对应的英制重量为{result:.3f}磅")
 elif unit == "pd":
     # 磅转千克
     result = num / 2.2046
     print(f"对应的公制重量为{result:.3f}公斤")
