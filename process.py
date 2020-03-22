import pickle
with open("test1.txt", "rb") as fp:
    b = pickle.load(fp)


print(b)



def process():
    for messages in b:
        a = messages.split('\n')
        if len(a) >= 3:
            print("name = " + a[0] + "\nmessage = "+ a[-2]+"\ntime = "+ a[-1]+"\n\n\n")

process()