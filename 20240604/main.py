from codrone_edu.drone import time *
import time
drone = Drone()
drone.pair()

for i in range(3):
    drone.speed_change(i+1)
    time.sleep(1)
    speed = drone.get_control_speed()
    print(speed)

    drone.takeoff()
    time.sleep(4)
    drone.set_pitch(30)
    drone.move(2)
    time.sleep(2)
    drone.set_pitch(-30)
    drone.move(2)
    time.sleep(2)
    drone.land()
    time.sleep(2)