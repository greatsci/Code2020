from bs4 import BeautifulSoup
import csv
import requests
import time

candidates = set(['Card Was Delivered To Me By The Post Office', 'New Card Is Being Produced', 'Card Was Mailed To Me', 'Card Was Picked Up By The United States Postal Service', 'Case Was Approved'])
other = set(['', ' ', 'Case Rejected Because I Sent An Incorrect Fee', 'Fees Were Waived', 'Request for Initial Evidence Was Mailed', 'Fingerprint Fee Was Received'])
pending ='Case Was Received'
my_case_num = 1990232080
url_prefix = 'https://egov.uscis.gov/casestatus/mycasestatus.do?appReceiptNum=YSC'
count_total = 0
count_valid = 0
count_other = 0
count_pending = 0
step = 0
for i in range(my_case_num - 5, my_case_num + 5):
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

    if status in candidates:
        count_valid += 1
    elif status == pending:
        count_pending += 1
    else:
        count_other += 1
    time.sleep(0.2)
    step += 1
    print(i, status)
print('total:', step)
print('total I-765:', count_total)
print('finished:', count_valid)
print('pending:', count_pending)
print('other:', count_other)