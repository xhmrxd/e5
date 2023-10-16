import time

def countdown(minutes):
    while minutes >= 0:
        mins, secs = divmod(minutes, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        minutes -= 1
    print("时间到！")

if __name__ == "__main__":
    countdown(25) # 设定专注时间为25分钟，你可以根据需要修改这个时间。
