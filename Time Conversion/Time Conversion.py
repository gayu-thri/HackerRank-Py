
def timeConversion(s):
    # Complete this function
    amOrPm = s[-2:]
    out = ""

    if(amOrPm == "PM"):
        if(int(s[0:2]) < 12):
            #1:05pm ->12+1= 13:05 
            out = out + str(12 + int(s[0:2])) + s[2:-2]   
        else:
            #12pm=12 on 24-hour clock
            out = out + str(int(s[0:2])) + s[2:-2]
    else:
        if(s[0:2] == '12'):
            out = out + "00" + s[2:-2]
        else:
            out = out + s[:-2]

    return out
s = input().strip()
result = timeConversion(s)
print(result)