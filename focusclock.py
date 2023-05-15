import time

def pomodoro_timer(minutes):
    """
    Starts a Pomodoro timer for the specified number of minutes.
    """
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print('Time up!')
