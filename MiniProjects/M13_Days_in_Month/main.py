def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  days = month_days[month-1]
  if is_leap(year) == False:
    return days
  elif is_leap(year) == True:
    if days == 28:
      days +=1
    return days
  
year = int(input())
month = int(input())
days = days_in_month(year, month)
print(days)