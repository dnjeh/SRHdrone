from codrone_edu.drone import *
import time
drone = Drone()
drone.pair()

print("이륙")
drone.takeoff()

print("2초간 호버링")
drone.hover(2)
time.sleep(1)

print("왼쪽 수제 나선형 비행")
drone.sendControlWhile(0, 0, 0, 30, 2000)
time.sleep(1)
drone.hover(1)
drone.sendControlWhile(0, 50, 40, -40, 10000)
time.sleep(1)

print("착륙")
drone.land()
drone.close()

drone.land()
drone.close()
