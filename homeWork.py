from parinya import LINE
import datetime
import csv
import time as Time

def make_csv():
    with open('homeWork.csv', mode='w',encoding='utf-8',newline="") as cvs_file:
        csv_writer = csv.writer(cvs_file, delimiter=',')
        for i in range(len(data)):
            csv_writer.writerow(data[i])

line = LINE("4vV3B81Wt7BLoVytgmE2U4H7o8ZaYSFCx0LL1X9gQzJ")
data = []
with open("homeWork.csv",mode="r",encoding='utf-8')as cvs_file:
    csv_reader = csv.reader(cvs_file, delimiter=',')
    for row in csv_reader:
        data.append(row)
    print(data)
while True:
    now = datetime.datetime.now()
    day = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
    time = str(now.now().hour)+":"+str(now.minute)+":"+str(now.second)
    if time != "6:0:0":
        for i in range(len(data)):
            subject =str("วิชา :"+data[i][0])
            sent_time = str("วันที่ส่ง :"+data[i][1])
            discrip =str("รายละเอียด :"+data[i][2])
            text = day+"\n"+subject+"\n"+sent_time+"\n"+discrip
            line.sendtext(text)
            if str(data[i][1]) == str(day):
                del data[i]
            make_csv()
        break
    Time.sleep(1)
