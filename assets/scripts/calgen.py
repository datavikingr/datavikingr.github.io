import math, calendar
from datetime import datetime, timedelta

days = ["ᚠ","ᚢ","ᚦ","ᚩ","ᚱ","ᚳ","ᚷ"]
months = ["ᚫᚠᛏᛖᚱᚪᚷᛇᛚᚪ","ᛋᚩᛚᛗᚩᚾᚪᚦ","ᚻᚱᛖᚦᛗᚩᚾᚪᚦ","ᛇᛥᚱᛖᛗᚩᚾᚪᚦ","ᚦᚱᛁᛗᛁᛚᚳᛖᛗᚩᚾᚪᚦ","ᚫᚱᚪᛚᛁᚦᚪ","ᛚᛁᚦᚪᛗᚩᚾᚪᚦ","ᚫᚠᛏᛖᚱᚪᛚᛁᚦᚪ","ᚹᛇᛞᛗᚩᚾᚪᚦ","ᚻᚫᛚᛁᚷᛗᚩᚾᚪᚦ","ᚹᛁᚾᛏᛖᚱᚠᚣᛚᛖᚦ","ᛒᛚᚩᛏᛗᚩᚾᚪᚦ","ᚫᚱᚪᚷᛇᛚᚪ"]
#current_year = datetime.now().year
current_year = 2023
j = 1
master_array = []
yulestartadj_array = []
for i in range(0,365):
    day_num = i % 7
    dayoftheweek = days[day_num]
    week_num = math.floor((j / 7.0001) + 1)
    week_in_month = week_num % 4
    if week_in_month == 0: 
        week_in_month = 4 #is actually 4 and the rest of the math works out.
        dayoftheweek = dayoftheweek+dayoftheweek+dayoftheweek+dayoftheweek #ᚠᚠᚠᚠ
    # week_in_month == 1 requires no change; is already simply ᚠ
    elif week_in_month == 2:
        dayoftheweek = dayoftheweek+dayoftheweek #ᚠᚠ
    elif week_in_month == 3:
        dayoftheweek = dayoftheweek+dayoftheweek+dayoftheweek #ᚠᚠᚠ
    if j == 365:
        dayoftheweek = "ᚻᚫᛚᛁᚷᛏᛁᛞᚪ"
        month_num = 0
        monthoftheyear = ""
    else:
        month_num = math.floor((j / 28.0001) + 1)
        monthoftheyear = months[(month_num -1)]
    calendar_date = dayoftheweek+" "+monthoftheyear
    #print(str(j)+" "+calendar_date)
    master_array.append(calendar_date)
    j += 1
start_date = 8
for l in master_array:
    k = master_array.index(l)
    if start_date == len(master_array):
        start_date = 0
    if k == 0:
        yulestartadj_array.append("ᚾᛖᚹ᛫ᚷᛠᚱ᛫ᛞᚫᚷ")
    elif k == 32:
        yulestartadj_array.append("ᛁᛗᛒᚩᛚᚳ")
    elif k == 44:
        yulestartadj_array.append("ᚹᚪᛚᛖᚾᛏᛁᚾᛋ᛫ᛞᚫᚷ")
    elif k == 67:
        yulestartadj_array.append("ᛗᚩᛞᚱᚪ᛫ᛋᚣᛗᛒᛖᛚ")
    elif k == 79:
        yulestartadj_array.append("ᛇᛥᚱᛖ")
    elif k == 82:
        yulestartadj_array.append("ᚪᛁᚱᛁᛖ᛫ᛋᚣᛗᛒᛖᛚ")
    elif k == 93:
        yulestartadj_array.append("ᚳᚱᚪᛁᚷ᛫ᛋᚣᛗᛒᛖᛚ")
    elif k == 99:
        yulestartadj_array.append("ᛚᛖᚹᚣ᛫ᛋᚣᛗᛒᛖᛚ")
    elif k == 120:
        yulestartadj_array.append("ᛒᛖᛚᛏᚪᚾ")
    elif k == 171:
        yulestartadj_array.append("ᛚᛁᚦᚪ")
    elif k == 200:
        yulestartadj_array.append("ᛗᛁ᛫ᛋᚣᛗᛒᛖᛚ")
    elif k == 210:
        yulestartadj_array.append("ᛗᚪᚱᚳᚩ᛫ᛋᚣᛗᛒᛖᛚ")
    elif k == 212:
        yulestartadj_array.append("ᚠᚱᛖᚣᚠᚪᛉᛁ")
    elif k == 219:
        yulestartadj_array.append("ᚠᚪᚦᛖᚱ᛫ᛋᚣᛗᛒᛖᛚ")
    elif k == 247:
        yulestartadj_array.append("ᚹᛖᛞᛁᛝ᛫ᛋᚣᛗᛒᛖᛚ")
    elif k == 256:
        yulestartadj_array.append("ᛒᚱᚪᚾᛞᚩᚾ᛫ᛋᚣᛗᛒᛖᛚ")
    elif k == 263:
        yulestartadj_array.append("ᚻᚪᚢᛥᚪᛒᛚᚩᛏ")
    elif k == 265:
        yulestartadj_array.append("ᛗᛁᛣᛖ᛫ᛋᚣᛗᛒᛖᛚ")
    elif k == 281:
        yulestartadj_array.append("ᛚᛖᛁᚠ᛫ᛖᚱᛁᛉᚩᚾ᛫ᛋᚣᛗᛒᛖᛚ")
    elif k == 301:
        yulestartadj_array.append("ᛞᚪᚹᛁᛞ᛫ᛋᚣᛗᛒᛖᛚ")
    elif k == 303:
        yulestartadj_array.append("ᛋᚪᛗᚻᚪᛁᚾ")
    elif k == 354:
        yulestartadj_array.append("ᛗᚩᛞᚱᚪᚾᛁᚻᛏ")
    elif k == 355:
        yulestartadj_array.append("ᚷᛇᛚ")
    else:
        yulestartadj_array.append(master_array[start_date])
    #print(str(k + 1)+" "+yulestartadj_array[-1])
    start_date += 1
if calendar.isleap(current_year):
    yulestartadj_array.insert(59,"ᛚᛠᛈ᛫ᛞᚫᚷ")
print(yulestartadj_array)
#for t in yulestartadj_array:
#    print(str(yulestartadj_array.index(t)+1)+" "+t)