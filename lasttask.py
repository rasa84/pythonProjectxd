import random

maxValue = 10000
var1 = random.randint(1000, 9999)
var2 = random.randint(1000, 9999)
var3 = random.randint(1000, 9999)
var4 = random.randint(1000, 9999)
var5 = random.randint(1000, 9999)
var6 = random.randint(1000, 9999)

print(var1, var2, var3, var4, var5, var6)
min1 = var1

if var2 < min1:
    min1 = var2
if var3 < min1:
    min1 = var3
if var4 < min1:
    min1 = var4
if var5 < min1:
    min1 = var5
if var6 < min1:
    min1 = var6

if var1 == min1:
    var1 = maxValue
elif var2 == min1:
    var2 = maxValue
elif var3 == min1:
    var3 = maxValue
elif var4 == min1:
    var4 = maxValue
elif var5 == min1:
    var5 = maxValue
else:
    var6 = maxValue

min2 = var1
if var2 < min2:
    min2 = var2
if var3 < min2:
    min2 = var3
if var4 < min2:
    min2 = var4
if var5 < min2:
    min2 = var5
if var6 < min2:
    min1 = var6
# print(var1, var2, var3, var4, var5, var6)
if var1 == min2:
    var1 = maxValue
elif var2 == min2:
    var2 = maxValue
elif var3 == min2:
    var3 = maxValue
elif var4 == min2:
    var4 = maxValue
elif var5 == min2:
    var5 = maxValue
else:
    var6 = maxValue

min3 = var1
if var2 < min3:
    min3 = var2
if var3 < min3:
    min3 = var3
if var4 < min3:
    min3 = var4
if var5 < min3:
    min3 = var5
if var6 < min3:
    min3 = var6
# print(var1, var2, var3, var4, var5, var6)
if var1 == min3:
    var1 = maxValue
elif var2 == min3:
    var2 = maxValue
elif var3 == min3:
    var3 = maxValue
elif var4 == min3:
    var4 = maxValue
elif var5 == min3:
    var5 = maxValue
else:
    var6 = maxValue

min4 = var1
if var2 < min4:
    min4 = var2
if var3 < min4:
    min4 = var3
if var4 < min4:
    min4 = var4
if var5 < min4:
    min4 = var5
if var6 < min4:
    min4 = var6
# print(var1, var2, var3, var4, var5, var6)
if var1 == min4:
    var1 = maxValue
elif var2 == min4:
    var2 = maxValue
elif var3 == min4:
    var3 = maxValue
elif var4 == min4:
    var4 = maxValue
elif var5 == min4:
    var5 = maxValue
else:
    var6 = maxValue

min5 = var1
if var2 < min5:
    min5 = var2
if var3 < min5:
    min5 = var3
if var4 < min5:
    min5 = var4
if var5 < min5:
    min5 = var5
if var6 < min5:
    min5 = var6
# print(var1, var2, var3, var4, var5, var6)
if var1 == min5:
    var1 = maxValue
elif var2 == min5:
    var2 = maxValue
elif var3 == min5:
    var3 = maxValue
elif var4 == min5:
    var4 = maxValue
elif var5 == min5:
    var5 = maxValue
else:
    var6 = maxValue

min6 = var1
if var2 < min6:
    min6 = var2
if var3 < min6:
    min6 = var3
if var4 < min6:
    min6 = var4
if var5 < min6:
    min6 = var5
if var6 < min6:
    min6 = var6
# print(var1, var2, var3, var4, var5, var6)
if var1 == min6:
    var1 = maxValue
elif var2 == min6:
    var2 = maxValue
elif var3 == min6:
    var3 = maxValue
elif var4 == min6:
    var4 = maxValue
elif var5 == min6:
    var5 = maxValue
else:
    var6 = maxValue

print(f"Surūšiuoti skaičiai: {min6}, {min5}, {min4}, {min3}, {min2}, {min1}")
