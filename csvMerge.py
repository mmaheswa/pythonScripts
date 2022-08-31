from csv import DictReader
import glob
import os
import pandas as pd

# Get current folder path.
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))

# Define the formateed CSV Header.
modifiedHeaders = ['tagLine','followerCount','website','domain','industry','companySize','headquarters','CompanyType','founded','specialties','companyAddress','mainCompanyID','industryCode','salesNavigatorLink','employeesOnLinkedIn','query','timestamp','companyUrl','phone','isClaimable','DataError','linkedinID','companyName']

print("------------------------------------------------------")
print("Converting CSV files !!")
print("------------------------------------------------------")
mainData = []
for filename in csv_files:
    with open(filename, 'r', encoding='utf-8') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            companyRowData = []
            for headerName in modifiedHeaders:
                try:
                    companyRowData.append(row[headerName])
                except:
                    companyRowData.append(' ')
            mainData.append(companyRowData)
        print(" Processed File : " + str(filename))
print("------------------------------------------------------")
companyData = pd.DataFrame(mainData, columns=modifiedHeaders)
companyData.to_csv('formatted.csv', index=False)
print(" Done!!!")
