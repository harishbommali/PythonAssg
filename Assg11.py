ns=int(input('no.of students: '))
n=input('Enter the name of the student: ')
m1=int(input('Enter mark1(physics): '))
m2=int(input('Enter mark2(chemistry): '))
m3=int(input('Enter mark3(maths): '))
total=m1+m2+m3
print('marks',total)
avg=total/3
if avg>=50:
    status='pass'
else:
    status='fail'
if avg>=90:
    gra='A+'
elif avg>=80 and avg<90:
    gra='A'
elif avg>=70 and avg<80:
    gra='B+'
elif avg>=60 and avg<70:
    gra='B'
elif avg>=50 and avg<60:
    gra='C'
else:
    grade='F'                       
print(f'total mark: {total}, average :{avg},grade:{gra},status: {status}')
print('conclusion')



#Note:i was trying apply no.of times for while loop,but not working properly may be he syntax problem. can you please solve it sir
#choice='Y'
#while choice.lower()=='yes' or choice.lower()=='y':
#choice=('do you have a student(y/n):')
