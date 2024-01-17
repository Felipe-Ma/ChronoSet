import requests
import subprocess
import time


def setTime():
    url = "http://worldtimeapi.org/api/timezone/America/Los_Angeles"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            time_data = response.json()
            current_time = time_data["datetime"]

            date, time = current_time.split("T")
            time = time.split(".")[0]
            timeSet = date + " " + time

            subprocess.run(["sudo", "timedatectl", "set-time", timeSet], check=True)

        else:
            print("Failed")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    while True:
        print('-' * 30 + "Setting Time" + '-' * 30)
        setTime()
        print('-' * 30 + "Going to Sleep" + '-' * 30)
        time.sleep(60)
