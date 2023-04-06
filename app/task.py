import pandas as pd
import re

def convert_to_dict(string_ls):
    res_dict = {}
    for j in range(len(string_ls)):
        string_ls[j] = re.sub(r'\'',"", string_ls[j])
        string_ls[j] = string_ls[j].split(":")
        # print(len(string_ls[i][j]))
        try:
                res_dict[string_ls[j][0].strip()] = string_ls[j][1]
            # else:
            #     print("empty_value in : ",string_ls[j][0])
        except:
            continue
    return res_dict

def ret_list_of_dict(string):
    res_ls = []
    string_ls = re.findall(r'\{.*?\}', string)
    # print(string_ls)
    for i in range(len(string_ls)):
        string_ls[i] = re.sub('{',"", string_ls[i])
        string_ls[i] = re.sub('}',"", string_ls[i])
        # print(type(string_ls[i]))
        string_ls[i] = string_ls[i].split(",")
        # print(len(string_ls[i]))
        # print(string_ls[i])
        res_ls.append(convert_to_dict(string_ls[i]))
        # print(string_ls[i])
        # print(res_dict)
        # break
    # print(res_ls)
    return res_ls

def create_column_from_list(df):
    df1 = pd.DataFrame()
    pre = ''    
    for i,rows in df.iterrows():
        # lst  = eval(rows["people"])
        lst = ret_list_of_dict(rows["people"])
        for di in lst:
            if di['role'].upper().strip() == 'CONTRACTOR':
                pre = 'contractor_'
            if di['role'].upper().strip() == 'APPLICANT':
                pre = 'applicant_'
            if di['role'].upper().strip() == 'OWNER':
                pre = 'owner_'
            for val in list(di.keys()):
                if pre+val not in df1.columns:
                    df1.insert(len(df1.columns), pre+val, di[val])
                    rows[pre+val] = di[val]
                else:
                    rows[pre+val] = di[val]
        df1 = df1.append(rows,ignore_index=True)
        # break
        if i>100:
            break
    return df1

if __name__ == "__main__":
    df = pd.read_csv("/home/akshay/Chistats/TASK/Kern_Scrap_Permits_Final_Filled_Missing_Zip.csv")
    # print(df["people"])
    df1 = create_column_from_list(df)
    print(df1)
    df1.to_csv("final.csv",index=False)