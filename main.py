from djitellopy import Tello

# Create an instance of the Tello class
tello = Tello()

# Connect to the Tello drone
tello.connect()

# Take off
tello.takeoff()

# # Fly the drone
# tello.send_rc_control(0, 50, 0, 0)  # Fly forward with a speed of 50

# # Wait for a few seconds
# tello.send_rc_control(0, 0, 0, 0)  # Stop the drone

# Land the drone
tello.land()

# Disconnect from the drone
tello.end()
