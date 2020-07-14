# content = 'On May 15, 2020, we received your Form I-765, Application for Employment Authorization, Receipt Number YSC2090248025, and sent you the receipt notice that describes how we will process your case. Please follow the instructions in the notice. If you do not receive your receipt notice by June 14, 2020, contact the USCIS Contact Center at www.uscis.gov/contactcenter. If you move, go to www.uscis.gov/addresschange to give us your new mailing address.'
# if content != 'sdf':
#     print("sd\\ns")
# else:
#     print(0)
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

f = open('C:\\Users\\ningz\\Desktop\\OPT\\' + timestr + '.csv', 'a')
f.write('test\n')
f.write('se')

f.close