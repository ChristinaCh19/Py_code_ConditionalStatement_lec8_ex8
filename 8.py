exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

difference = 0
result = ''
message = ''
hours = 0
minutes = 0

exam = (exam_hour * 60) + exam_minutes
arrival = (arrival_hour * 60) + arrival_minutes

if arrival == exam:
    print('On time')

elif arrival < exam:
    difference = exam - arrival
    if difference <= 30:
        print('On time')
    elif difference > 30:
        print('Early')

    if difference >= 60:
        hours = difference // 60
        minutes = difference % 60
        print(f'{hours}:{minutes:02} hours before the start')
    elif difference < 60:
        minutes = difference
        print(f'{minutes} minutes before the start')

elif arrival > exam:
    difference = arrival - exam
    print('Late')
    if difference >= 60:
        hours = difference // 60
        minutes = difference % 60
        print(f'{hours}:{minutes:02} hours after the start')
    elif difference < 60:
        minutes = difference
        print(f'{minutes} minutes after the start')














