from datetime import date, time, datetime, timedelta

world_cup_2022 = date(2030, 11, 21)
print(world_cup_2022)

print(world_cup_2022.year)
print(world_cup_2022.month)
print(world_cup_2022.day)



today = date.today()
print(today)

# some_day = date.fromordinal(738488)
# print(some_day)

another_day = date.fromisoformat('2022-11-21')
print(another_day)

days_to_worldcup = world_cup_2022 - today
print(days_to_worldcup)

time1 = time()

print(time1)

print(time1.hour)
print(time1.minute)
print(time1.second)

time1 = time()

print(time1)

print(time1.hour)
print(time1.minute)
print(time1.second)

time2 = time(hour=15, minute=29, second=20)
print(time2)

time3 = time.fromisoformat('18:44:50')

print(time3)


world_cup_2022 = datetime(year=2022, month=11, day=21, hour=13, minute=0, second=0)
print(world_cup_2022)

world_cup_2022 = datetime(year=2022, month=11, day=21, hour=13, minute=0, second=0)
print(world_cup_2022)

now = datetime.now()
print(now)

today = datetime.today()
print(today)

world_cup_2022 = datetime.fromisoformat('2022-11-21 13:08:00')
print(world_cup_2022)

count_down = now - world_cup_2022
print("Count Down:", count_down)


delta = timedelta(days = 28, seconds = 39, minutes = 55, hours = 4, weeks= 3)

now = datetime.now()

print(now - delta)

print(now.strftime('%A, %d/%B/%Y'))