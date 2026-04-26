"""
Main entry point for the robot software.

This script tests basic movement commands:
- forward
- backward
- left
- right
- stop
"""

import time

from motors import MotorController
from movement import RobotMovement


def main() -> None:
    """
    Start the robot movement test.
    """
    print("Robot system booting...")

    motor_controller = MotorController()
    motor_controller.initialize()

    robot = RobotMovement(motor_controller)

    try:
        print("Starting movement test...")

        robot.move_forward(0.3)
        time.sleep(2)

        robot.stop()
        time.sleep(1)

        robot.move_backward(0.3)
        time.sleep(2)

        robot.stop()
        time.sleep(1)

        robot.turn_left(0.3)
        time.sleep(1)

        robot.stop()
        time.sleep(1)

        robot.turn_right(0.3)
        time.sleep(1)

        robot.stop()

        print("Movement test finished")

    except KeyboardInterrupt:
        robot.stop()
        print("Interrupted safely by user")

    except Exception as exc:
        robot.stop()
        print(f"Unexpected error: {exc}")
        raise


if __name__ == "__main__":
    main()