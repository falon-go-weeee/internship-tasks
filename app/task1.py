from datetime import datetime
import dateutil.parser
import re

def parse_date_time(dt):
    formats = ["%d-%m-%Y","%Y-%m-%d","%d/%m/%Y","%Y/%m/%d"]
    for format in formats:
        try:
            date = datetime.strptime(dt, format)
        except:
            continue
    # print(date)
    return date
        
def convert_to_epoch(date):
    if type(date) == str:
        # date = dateutil.parser.parse(dt)
        date = parse_date_time(dt)
        print(dt, " : ",date.strftime("%Y-%m-%d"))
    # epoch = datetime(int(date.strftime("%Y")), int(date.strftime("%m")), int(date.strftime("%d"))).strftime('%s')
    epoch = datetime.timestamp(date)
    print("epoch", epoch)
    return epoch

def convert_to_date(epoch):
    date = datetime.fromtimestamp(epoch)
    print("date", date)
    return date

if __name__ == "__main__":
    dt = "23/06/2021"
    date = convert_to_epoch(dt)
    convert_to_date(date)
    dt = "23-06-2021"
    date = convert_to_epoch(dt)
    convert_to_date(date)
    dt = "2021/06/23"
    date = convert_to_epoch(dt)
    convert_to_date(date)
    dt = "2021-06-23"
    date = convert_to_epoch(dt)
    convert_to_date(date)
    # dt = "23 june 2021"
    # convert_to_epoch(dt)
    # dt = "june 23 021"
    # date = convert_to_epoch(dt)
    # print(date)
    # dt = datetime.datetime.now()
    # convert_to_epoch(dt)