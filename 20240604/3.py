from codrone_edu.drone import *
import time
drone = Drone()
drone.pair()

print("이륙")
drone.takeoff()

print("2초간 호버링")
drone.hover(2)
time.sleep(1)

print("오른쪽 삼각 비행")
drone.triangle()
time.sleep(1)

print("왼쪽 삼각 비행")
drone.triangle(60, 1, -1)
time.sleep(1)

print("착륙")
drone.land()
drone.close()

drone.land()
drone.close()
