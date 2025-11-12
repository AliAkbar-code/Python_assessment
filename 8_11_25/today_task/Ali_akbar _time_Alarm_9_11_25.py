import time
import datetime
import os

def set_timer():
    try:
        seconds = int(input("Enter number of seconds for timer: "))
        if seconds < 0:
            print("Please enter a positive number!")
            return
        print(f"Timer set for {seconds} seconds...")
        time.sleep(seconds)
        print("\nTime's up!")
    except ValueError:
        print("Invalid input! Please enter an integer number.")

def alarm_seconds():
    try:
        seconds = int(input("Set alarm after how many seconds? "))
        if seconds < 0:
            print("Please enter a positive number!")
            return
        print(f"Alarm set for {seconds} seconds...")
        start = datetime.datetime.now()
        end = start + datetime.timedelta(seconds=seconds)
        
        while datetime.datetime.now() < end:
            time.sleep(1)
        
        print("\nAlarm ringing!")
        os.system("echo Alarm ringing!")
    except ValueError:
        print("Invalid input! Please enter an integer number.")

def main():
 while True:
    print("1. Set Timer")
    print("2. Set Alarm")
    choice = input("Choose (1/2): ")

    if choice == "1":
        set_timer()
    elif choice == "2":
        alarm_seconds()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
