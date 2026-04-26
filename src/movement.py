"""
High-level robot movement commands.

This module turns simple robot actions like "move forward" or "turn left"
into left/right motor speed commands.
"""

from src.motors import MotorController


class RobotMovement:
    """
    High-level movement controller for a two-wheel robot.

    This class does not talk directly to GPIO pins.
    It sends speed commands to MotorController.
    """

    def __init__(self, motor_controller: MotorController) -> None:
        """
        Create a movement controller.

        Args:
            motor_controller: Motor controller used to drive the wheels.
        """
        self.motor_controller = motor_controller

    def move_forward(self, speed: float = 0.3) -> None:
        """Move the robot forward."""
        print("Movement command: forward")
        self.motor_controller.set_speed(speed, speed)

    def move_backward(self, speed: float = 0.3) -> None:
        """Move the robot backward."""
        print("Movement command: backward")
        self.motor_controller.set_speed(-speed, -speed)

    def turn_left(self, speed: float = 0.3) -> None:
        """Turn the robot left."""
        print("Movement command: left")
        self.motor_controller.set_speed(-speed, speed)

    def turn_right(self, speed: float = 0.3) -> None:
        """Turn the robot right."""
        print("Movement command: right")
        self.motor_controller.set_speed(speed, -speed)

    def stop(self) -> None:
        """Stop the robot."""
        print("Movement command: stop")
        self.motor_controller.stop()