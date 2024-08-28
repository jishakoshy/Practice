from datetime import datetime,timedelta

today = datetime.now().date()

tomors = today + timedelta(days =1)
print(tomors)
