from codrone_edu.drone import *
import time
drone = Drone()
drone.pair()

print("이륙")
drone.takeoff()

print("2초간 호버링")
drone.hover(2)
time.sleep(1)

t = 3500

print("팔자 비행")
for yaw, timet in [(50, t), (-50, t*2), (50, t)]:
    drone.sendControlWhile(0, 30, yaw, 0, timet)
time.sleep(1)

print("착륙")
drone.land()
drone.close()

drone.land()
drone.close()
