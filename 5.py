import datetime, time

dt = datetime.datetime.now()

print(dt.date())

persum = input ("mata in ditt personnummer(yyyymmdd)")

dtpers = dt.strptime(persumm, '%Y%m%d')

if dt.month()  == dtpers.month() dt.day() == dtpers.day():
    print ("grattis det är din födelsedag!" , dtpers.date())