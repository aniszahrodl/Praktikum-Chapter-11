from datetime import *
from datetime import datetime as dtm

def diffDate(x):
    now= datetime.date(datetime.now())
    P= datetime.date(dtm.strptime(x, '%Y-%m-%d'))
    i=now-P
    print(i.days)

diffDate('2021-1-3')
