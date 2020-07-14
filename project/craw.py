from bs4 import BeautifulSoup
import csv
import requests
import time

candidates = set(['Card Was Delivered To Me By The Post Office', 'New Card Is Being Produced', 'Card Was Mailed To Me', 'Card Was Picked Up By The United States Postal Service', 'Case Was Approved'])
other = set(['', ' ', 'Case Rejected Because I Sent An Incorrect Fee', 'Fees Were Waived', 'Request for Initial Evidence Was Mailed', 'Fingerprint Fee Was Received'])
pending ='Case Was Received'
my_case_num = 2090248050
url_prefix = 'https://egov.uscis.gov/casestatus/mycasestatus.do?appReceiptNum=YSC'
count_total = 0
count_valid = 0
count_other = 0
count_pending = 0
step = 0
timestr = time.strftime("%Y%m%d-%H%M%S")

with open('C:\\Users\\ningz\\Desktop\\OPT\\' + timestr + '.csv', 'w', newline='') as csvfile:
    for i in range(2090248100, 2090249000):
        url = url_prefix + str(i)
        response = requests.get(url)
    #   Exception has occurred: SSLError
    #   HTTPSConnectionPool(host='egov.uscis.gov', port=443): Max retries exceeded with url: /casestatus/mycasestatus.do?appReceiptNum=YSC1990232075 (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available."))
    #   File "C:\Users\ningz\Desktop\Code2020\craw.py", line 18, in <module>
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
            reswriter = csv.writer(csvfile, delimiter = ',', quotechar=',', quoting = csv.QUOTE_MINIMAL)
            idx = str(i)
            reswriter.writerow([idx] + [status] + [content[3:10]])
            print(i, status, content[3:10])

print('total:', step)
# print('total I-765:', count_total)
print('finished:', count_valid)
print('pending:', count_pending)
print('other:', count_other)