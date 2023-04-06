from datetime import datetime
import pandas as pd
import dateutil.parser
import re

def parse_date_time(date):
    formats = ["%m-%d-%Y","%d-%m-%Y","%Y-%m-%d","%m/%d/%Y","%d/%m/%Y","%Y/%m/%d"]
    for format in formats:
        try:
            date = date.split(" ")[0]
            # print(date)
            date = datetime.strptime(date, format)
            # date = dateutil.parser.parse(date)
            # print(date)
            return date
        except:
            continue
    else:   
        # print("exception : ", date)
        return False

def convert_to_epoch(dt):
    date = parse_date_time(dt)
    # print(date, " : ",date.strftime("%Y-%m-%d"))
    if date:
        epoch = datetime(int(date.strftime("%Y")), int(date.strftime("%m")), int(date.strftime("%d"))).strftime('%s')
        # epoch = datetime.timestamp(date)
        print("epoch", epoch)
        return epoch
    else:
        return dt

def convert_to_date(epoch):
    date = datetime.fromtimestamp(epoch)
    # print("date", date)
    return date

def replace_date_with_timestamp(df):
    df["permit_applied_date"] =  df["permit_applied_date"].apply(convert_to_epoch)
    print(df["permit_applied_date"])
    return df

if __name__=="__main__":
    df = pd.read_csv("/home/akshay/Chistats/TASK/Manatee_Permits_Missing_Zip_New_Missing_Zip_Filled_Missing_Zip.csv")
    # print(df["permit_applied_date"])
    new_df = replace_date_with_timestamp(df)
    new_df.to_csv("/home/akshay/Chistats/TASK/op.csv",index=False)
