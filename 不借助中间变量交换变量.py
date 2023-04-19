a = int(input("请输入a:"))
b = int(input("请输入b:"))
c = int(input("请输入c:"))
a = b-a
b = b-a
a = a+b           # 通过三行代数运算交换a和b的值
result = a+c      # 计算交换过后a加c的值
print("a加c的值是：")
print(result)
