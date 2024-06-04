from codrone_edu.drone import *
import time
drone = Drone()
drone.pair()

print("이륙")
drone.takeoff()

print("2초간 호버링")
drone.hover(2)
time.sleep(1)

print("지그재그 비행")
for roll, ttime in [(50, 1000), (-50, 2000), (50, 2000), (-50, 2000), (50, 2000), (-50, 1000)]:
    drone.sendControlWhile(roll, 0, 0, 0, ttime)
time.sleep(1)

print("착륙")
drone.land()
drone.close()

drone.land()
drone.close()
