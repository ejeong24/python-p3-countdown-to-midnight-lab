import time

def countdown(from_this_number):
    start=from_this_number
    while (start > 0):
        if (start > 0):
            print(f'{start} SECOND(S)!')
            start-=1
        if (start == 0):
            print('HAPPY NEW YEAR!')

def countdown_with_sleep(from_this_number, for_how_many_seconds=1):
    start=from_this_number
    while (start > 0):
        if (start > 0):     
            print(f'{start} SECOND(S)!')
            start-=1
            time.sleep(for_how_many_seconds)
        if (start == 0):
            print('HAPPY NEW YEAR!')

countdown(10)
countdown_with_sleep(10,1)
        