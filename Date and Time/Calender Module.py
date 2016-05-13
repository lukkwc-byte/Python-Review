import calendar
MM, DD, YYYY = map(int, input().strip().split())
weekdays = {0:'MONDAY', 1:'TUESDAY', 2:'WEDNESDAY', 3:'THURSDAY', 4:'FRIDAY', 5:'SATURDAY', 6:'SUNDAY'}
print(weekdays[calendar.weekday(year=YYYY, month=MM, day=DD)])