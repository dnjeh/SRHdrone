from codrone_edu.drone import *
import time
drone = Drone()
drone.pair()

print("이륙")
drone.takeoff()

print("2초간 호버링")
drone.hover(2)
time.sleep(1)

print("오른쪽 원 비행")
drone.circle()
time.sleep(1)
print("왼쪽 원 비행")
drone.circle(75, -1)
time.sleep(1)

print("착륙")
drone.land()
drone.close()

drone.land()
drone.close()
