import pickle
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
        eventr = set(re.findall(event,i.lower())) 
        dayr = set(re.findall(day,i.lower()))
        timer = list(set(re.findall(time,i.lower())))
        Subjectr = set(re.findall(Subject,i.lower()))
        if len(eventr) and len(dayr) and len(Subjectr) :
            print('Subject :', " ".join(Subjectr), end = ' ')
            print(" ".join(eventr))
            print('Day :'," ".join(dayr))
            print('Time :'," ".join(timer[0]))
            
            print(i)

            print()
            print()



# process()