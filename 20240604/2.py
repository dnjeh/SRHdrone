from codrone_edu.drone import *
import time
drone = Drone()
drone.pair()

print("이륙")
drone.takeoff()

print("2초간 호버링")
drone.hover(2)
time.sleep(1)

print("오른쪽 사각 비행")
drone.square()
time.sleep(1)

print("왼쪽 사각 비행")
drone.square(60, 1, -1)
time.sleep(1)

print("착륙")
drone.land()
drone.close()

drone.land()
drone.close()
