from datetime import datetime, timedelta
from time import sleep
import csv, math
from pathlib import Path
from orbit import ISS

G = 6.67*10**-11
Mass = 6*10**24
Earth_r = 6370000

base_folder = Path(__file__).parent.resolve()

def add_to_csv(data, file_name):
    with open(base_folder / file_name, "a") as file:
        writer = csv.writer(file)
        writer.writerow(data)
        
def create_file(file_name):
    with open(file_name, 'w', newline= '') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                "datetime",
                "longitude",
                "orbit_speed"
            )
        )

# Create a variable to store the start time
start_time = datetime.now()
# Create a variable to store the current time
# (these will be almost the same at the start)
now_time = datetime.now()
create_file("data.csv")

if __name__ == "__main__":
    # Run a loop for 1 minute
    while (now_time < start_time + timedelta(seconds=15)):
        orbit = ISS().coordinates()
        sleep(1)
        print(now_time)
        Total_radio = orbit.elevation.m + Earth_r
        orbit_speed = math.sqrt(G*Mass/Total_radio)
        print(orbit_speed)
        # Update the current time
        add_to_csv(
            (
               now_time,
               orbit.longitude.degrees,
               orbit_speed
            ),
            "data.csv"
        )
        now_time = datetime.now()