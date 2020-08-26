from bs4 import BeautifulSoup
import csv
import requests
import time

candidates = set(['Card Was Delivered To Me By The Post Office', 'New Card Is Being Produced', 'Card Was Mailed To Me', 'Card Was Picked Up By The United States Postal Service', 'Case Was Approved'])
other = set(['', ' ', 'Case Rejected Because I Sent An Incorrect Fee', 'Fees Were Waived', 'Request for Initial Evidence Was Mailed', 'Fingerprint Fee Was Received'])
pending ='Case Was Received'
# my_case_num = 2090248050
start = 2090248000
end = 2090248100
url_prefix = 'https://egov.uscis.gov/casestatus/mycasestatus.do?appReceiptNum=YSC'
count_total = 0
count_valid = 0
count_other = 0
count_pending = 0
step = 0
timestr = time.strftime("%Y%m%d-%H%M%S")

outfile = 'C:\\Users\\ningz\\Desktop\\OPT\\' + str(start) + '_' + str(end) + '_' + timestr + '.csv'
with open(outfile, 'w', newline='') as csvfile:
    for i in range(start, end):
        url = url_prefix + str(i)
        response = requests.get(url)
        bs = BeautifulSoup(response.text, 'html.parser')
        temp = bs.find(class_='col-lg-12 appointment-sec center')
        if not temp:
            print("error")
            time.sleep(0.2)
            continue
        content = temp.find('p').get_text()
        status = temp.find('h1').get_text()
        # print(i, status, content)

        if status in candidates:
            count_valid += 1
        elif status == pending and 'I-765' in content:
            count_pending += 1
            status = 'Pending'
        else:
            count_other += 1
            status = 'Other'
        time.sleep(0.2)
        step += 1
        if status != 'Other':
            s1 = content.split('On ', 1)[1]
            s2 = s1.split(',', 1)
            date = s2[0]

            reswriter = csv.writer(csvfile, delimiter = ',', quotechar=',', quoting = csv.QUOTE_MINIMAL)
            idx = str(i)
            reswriter.writerow([idx] + [status] + [date])
            print(i, status, date)

print('total:', step)
# print('total I-765:', count_total)
print('finished:', count_valid)
print('pending:', count_pending)
print('other:', count_other)