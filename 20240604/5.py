from codrone_edu.drone import *
import time
drone = Drone()
drone.pair()

print("이륙")
drone.takeoff()

print("2초간 호버링")
drone.hover(2)
time.sleep(1)

print("오른쪽 지그재그 비행")
drone.sway()
time.sleep(1)

print("왼쪽 지그재그 비행")
drone.sway(30, 2, -1)
time.sleep(1)

print("착륙")
drone.land()
drone.close()

drone.land()
drone.close()
