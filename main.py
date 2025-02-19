##################### Extra Hard Starting Project ######################

import pandas
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
today = now.day
month = now.month


dataframe = pandas.read_csv("birthdays.csv")
birthday_dictionary = dataframe.to_dict('records')

filenames = ['letter_templates/letter_1.txt','letter_templates/letter_2.txt','letter_templates/letter_3.txt']
my_email = "tiakchri@gmail.com"
password = "jqsg uqmq push btbe"

with open(filenames[0],'r') as file1, open(filenames[1],'r') as file2,open(filenames[2],'r') as file3:
    content1 = file1.read()
    content2 = file2.read()
    content3 = file3.read()
    letter_set = [content1,content2,content3]
    final_letter = random.choice(letter_set)
    for item in birthday_dictionary:
        if item['month'] == month and item['day'] == today:
            final_letter = final_letter.replace('[NAME]',str(item['name']))
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs="chritiak@gmail.com",
                                    msg=f"Subject:Happy Birthday! \n\n{final_letter}")


