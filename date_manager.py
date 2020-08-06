"""module to help date usage"""

#how many days each month has
DAYS_BY_MONTH = [
    31,0,#for february, feb_days() will be used
    31,30,31,30,31,31,30,31,30,31]
#
        
def feb_days(year):
    #returns how many days february has on a specific year
    if not year%4 == 0:
        return 28
    
    elif not year%100 == 0:
        return 29
    
    elif not year%400 == 0:
        return 28
    
    else:
        return 29

def up_month(amount,date,join_date=True):
    '''
advances or retreats date's month by a certain amount.
date format can be [day,month,year] or "day/month/year"
    '''

    #dealing with date
    if type(date) is str:
        date = [int(x) for x in date.split("/")]
        
    day,month,year=date
    #february days
    days_by_month = DAYS_BY_MONTH[:]
    days_by_month[1] = feb_days(year)
    
    #changing month
    month+=amount
    
    #fixing month excess or lack, eg: 2/15/2020 or 2/-15/2020
    while month not in range(1,13):
        sign = 1 if month>12 else -1
        month -= 12*sign
        year += sign*1

    #fixing day
    day = days_by_month[month-1] if day > days_by_month[month-1]\
          else day

    #

    return [day,month,year] if join_date==False\
           else "/".join(map(str,[day,month,year]))
    
    

if __name__ == '__main__':
    while True:
        print(up_month( int(input("amount:")), input("date:")))
