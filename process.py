import pickle
from dateparser.search import search_dates
import re
with open("test1.txt", "rb") as fp:
    b = pickle.load(fp)


# print(b)

actual_message = []

def process():
    for messages in b:
        a = messages.split('\n')
        if len(a) >= 3:
            # print("name = " + a[0] + "\nmessage = "+ a[-2]+"\ntime = "+ a[-1]+"\n\n\n")
            actual_message.append(a[-2])

process()


# for i in actual_message:
#         event = r'(test|lab|fee|payment)'
#         day = r'(mon|tue|wed|thu|fri|sat|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|next.*week|next.*month)'
#         time = r'([0-9]:[0-9]+|[0-9]+.[0-9]+).*(am|pm)'
#         Subject = r'(\bss|\bsystem software|\bml|\bmachine learning|\bjava|\bjava)'
#         eventr = re.findall(event,i.lower()) 
#         dayr = re.findall(day,i.lower())
#         timer = re.findall(time,i.lower())
#         Subjectr = re.findall(Subject,i.lower())
#         if len(eventr) and len(dayr) and len(Subjectr) :
#             print('Subject :', Subjectr, end = ' ')
#             print(' Event:', eventr)
#             print('Day',dayr)
#             print('Time',timer)
            
#             print(i)


for i in b:
        event = r'(test|lab|fee|payment)'
        day = r'(mon|tue|wed|thu|fri|sat|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|next.*week|next.*month)'
        time = r'([0-9]:[0-9]+|[0-9]+.[0-9]+).*(am|pm)'
        Subject = r'(\bss|\bsystem software|\bml|\bmachine learning|\bjava|\bjava)'
        date = r'(\b[0-9]+.(th|rd|th|st))'
        eventr = set(re.findall(event,i.lower())) 
        dayr = set(re.findall(day,i.lower()))
        timer = list(set(re.findall(time,i.lower())))
        Subjectr = set(re.findall(Subject,i.lower()))
        dater = list(set(re.findall(date,i.lower())))
        
        Subjectstr = " ".join(Subjectr)
        eventstr = " ".join(eventr)
        daystr = " ".join(dayr)
        if len(dater):
            datestr = "".join(dater[0][0])
        if len(timer):
            timestr = " ".join(timer[0])

        if len(eventr) and len(dayr) and len(Subjectr) :
            # print(dater)
            print('Subject :' + Subjectstr +" "+ eventstr)
            

            print('Day :', daystr + " " + datestr)
            print('Time :',timestr)
            
            # print(i)

            print()
            print()

# for s in b:
#         event = re.findall(r'(test|lab|fee|payment)',s)
#         dates = search_dates(s)
#         if len(event):
#             print(event)
#             print(dates[0][0])
#             print()
#             print()


# process()