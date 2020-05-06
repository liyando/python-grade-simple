num1=int(input(' Input Nilai Tugas: '))
num2=int(input(' Input Nilai uts: '))
num3=int(input(' Input Nilai uas:'))

num=int((num1/100*30)+(num2/100*30)+(num3/100*40))

print('')
print('HASIL')
print('===========')
print('TUGAS:',num1)
print('UTS',num2)
print('UAS',num3)
print('AKHIR',num)

if num<=100 and num>=90:
    print('GRADE:A')
elif num<85 and num>90:
    print('GRADE:A-')
elif num < 80 and num > 85:
    print('GRADE:B+')
elif num < 75 and num > 80:
    print('GRADE:B')
elif num < 70 and num > 75:
    print('GRADE:B-')
elif num <70 and num >65:
    print('GRADE:C+')
elif num <65 and num >60:
    print('GRADE:C-')
elif num <60 and num >50:
    print('GRADE:D')
elif num <50 and num >40:
    print('GRADE:E')
elif num <40 and num >0:
    print('GRADE:T')
else :
    print('Sorry! You are fail')
