import calendar  # to convert read able time to epocy time
import time
from datetime import datetime


run = True
while run:
    # Taking user input date and making into string type
    user_date = str(input())

    if '-' in user_date:  # looking in user input for -./\ format for dates
        ymd = '%Y-%m-%d'
        mdy = '%m-%d-%Y'
        dmy = '%d-%m-%Y'
    elif '.' in user_date:
        ymd = '%Y.%m.%d'
        mdy = '%m.%d.%Y'
        dmy = '%d.%m.%Y'
    elif '/' in user_date:
        ymd = '%Y/%m/%d'
        mdy = '%m/%d/%Y'
        dmy = '%d/%m/%Y'
    elif '\\' in user_date:
        ymd = '%Y\%m\%d'
        mdy = '%m\%d\%Y'
        dmy = '%d\%m\%Y'
    else:
        ymd = '%Y%m%d'
        mdy = '%m%d%Y'
        dmy = '%d%m%Y'

    def epoch(user_date, ymd, mdy, dmy):

        try:  # Trying different format
            dash_epoch = calendar.timegm(time.strptime(user_date, ymd))
            return dash_epoch
        except:  # If value error trying different format again
            try:
                dash_epoch = calendar.timegm(time.strptime(user_date, mdy))
                return dash_epoch

            except:  # If value error for month trying different format again
                try:
                    dash_epoch = calendar.timegm(time.strptime(user_date, dmy))
                    return dash_epoch
                except:
                    print('Unable to convert the provided date')

    ep = epoch(user_date, ymd, mdy, dmy)
    try:
        if ep < 0:  # if negative epoch received stop code since it is less than 1970 years
            print('Unable to convert the provided date')
            run = False
        else:
            print(ep)
    except TypeError:
        pass
