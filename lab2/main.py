from datetime import datetime, timedelta

def add_minutes_to_time(time_str, minutes_to_add):
    
    time_object = datetime.strptime(time_str, "%H:%M")
    

    new_time = time_object + timedelta(minutes=minutes_to_add)
    

    return new_time.strftime("%H:%M")


initial_time = input()
minutes = int(input())

result = add_minutes_to_time(initial_time, minutes)
print(f"Результат: {result}")  