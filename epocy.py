import calendar  # to convert read able time to epocy time
import time
from datetime import date


user_date = str(input())  # Taking user input date and making into string type


if '-' in user_date:  # looking in user input for - in format

    try:  # Trying format '%Y-%m-%d'
        dash_epoch = calendar.timegm(time.strptime(user_date, '%Y-%m-%d'))
        print(dash_epoch)
    except:
        try:
            ask = input(
                'If your date format is mm-dd-yyyy enter \'M\' or dd-mm-yyyy enter \'D\':')
            if ask == 'M':
                dash_epoch = calendar.timegm(
                    time.strptime(user_date, '%m-%d-%Y'))
                print(dash_epoch)

            elif ask == 'D':
                dash_epoch = calendar.timegm(
                    time.strptime(user_date, '%d-%m-%Y'))
                print(dash_epoch)
        except:
            print('Unable to convert the provided date')
elif '.' in user_date:
    try:
        dash_epoch = calendar.timegm(time.strptime(user_date, '%Y.%m.%d'))
        print(dash_epoch)
    except:
        try:
            ask = input(
                'If your date format is mm.dd.yyyy enter \'M\' or dd.mm.yyyy enter \'D\':')
            if ask == 'M':
                dash_epoch = calendar.timegm(
                    time.strptime(user_date, '%m.%d.%Y'))
                print(dash_epoch)

            elif ask == 'D':
                dash_epoch = calendar.timegm(
                    time.strptime(user_date, '%d.%m.%Y'))
                print(dash_epoch)
        except:
            print('Unable to convert the provided date')

elif '/' in user_date:
    try:
        dash_epoch = calendar.timegm(time.strptime(user_date, '%Y/%m/%d'))
        print(dash_epoch)
    except:
        try:
            ask = input(
                'If your date format is mm-dd-yyyy enter \'M\' or dd-mm-yyyy enter \'D\':')
            if ask == 'M':
                dash_epoch = calendar.timegm(
                    time.strptime(user_date, '%m/%d/%Y'))
                print(dash_epoch)

            elif ask == 'D':
                dash_epoch = calendar.timegm(
                    time.strptime(user_date, '%d/%m/%Y'))
                print(dash_epoch)
        except:
            print('Unable to convert the provided date')
elif '\\' in user_date:
    try:
        dash_epoch = calendar.timegm(time.strptime(user_date, '%Y\%m\%d'))
        print(dash_epoch)
    except:
        try:
            ask = input(
                'If your date format is mm\dd\yyyy enter \'M\' or dd\mm\yyyy enter \'D\':')
            if ask == 'M':
                dash_epoch = calendar.timegm(
                    time.strptime(user_date, '%m\%d\%Y'))
                print(dash_epoch)

            elif ask == 'D':
                dash_epoch = calendar.timegm(
                    time.strptime(user_date, '%d\%m\%Y'))
                print(dash_epoch)
        except:
            print('Unable to convert the provided date')
else:
    try:
        dash_epoch = calendar.timegm(time.strptime(user_date, '%Y%m%d'))
        print(dash_epoch)
    except:
        try:
            ask = input(
                'If your date format is mmddyyyy enter \'M\' or ddmmyyyy enter \'D\':')
            if ask == 'M':
                dash_epoch = calendar.timegm(
                    time.strptime(user_date, '%m%d%Y'))
                print(dash_epoch)
            elif ask == 'D':
                dash_epoch = calendar.timegm(
                    time.strptime(user_date, '%d%m%Y'))
                print(dash_epoch)
        except:
            print('Unable to convert the provided date')
