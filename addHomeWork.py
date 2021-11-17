import csv

with open('homeWork.csv', mode='a', encoding='utf-8',newline="") as cvs_file:
    csv_writer = csv.writer(cvs_file, delimiter=',')
    while True:
        subject = input("วิชา :")
        if subject == "stop":
            break
        sent_day = input("วันที่ส่ง :")
        discrip = input("รายละเอียดงาน :")
        csv_writer.writerow([subject,sent_day,discrip])