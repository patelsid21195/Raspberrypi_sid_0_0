"""
Main entry point for the robot software.

This module is responsible for:
1. Booting the software system
2. Initializing the motor controller
3. Running a simple timed control loop
4. Stopping the robot safely on exit or interruption

At this stage, the motor controller is still a software abstraction.
Real GPIO interaction will be added later.
"""

import time
from motors import MotorController


def main() -> None:
    """
    Start the robot application.

    This function initializes the motor controller, runs a simple
    heartbeat loop for development testing, and ensures that the
    motors are stopped safely if the program exits or is interrupted.

    Returns:
        None
    """
    print("Robot system booting...")

    motor_controller = MotorController()
    motor_controller.initialize()

    try:
        for i in range(5):
            print(f"System heartbeat {i + 1}")
            motor_controller.set_speed(0.3, 0.3)
            time.sleep(1)

        motor_controller.stop()
        print("Robot system finished test run")

    except KeyboardInterrupt:
        motor_controller.stop()
        print("Interrupted safely by user")

    except Exception as exc:
        motor_controller.stop()
        print(f"Unexpected error: {exc}")
        raise


if __name__ == "__main__":
    main()