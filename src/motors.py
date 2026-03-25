"""
Motor control abstraction layer.

This module provides a clean software interface for controlling
the left and right motors of the robot.

At the current stage, this implementation prints actions instead
of controlling real GPIO pins. Later, the print statements will
be replaced with Raspberry Pi GPIO and PWM commands.

Design goal:
- keep hardware details isolated here
- let main.py call simple methods only
"""


class MotorController:
    """
    Software abstraction for a differential-drive motor controller.

    This class is responsible for:
    - initializing motor control resources
    - setting left/right motor speeds
    - stopping both motors safely

    In the current development phase, this class performs software-only
    simulation using print statements.
    """

    def __init__(self) -> None:
        """
        Create a new MotorController instance.

        The controller starts in an uninitialized state. The `initialize`
        method must be called before motor commands are accepted.

        Returns:
            None
        """
        self.initialized = False

    def initialize(self) -> None:
        """
        Initialize the motor controller.

        In the current version, this marks the controller as ready.
        In future versions, this method will configure Raspberry Pi GPIO,
        PWM channels, and default motor states.

        Returns:
            None
        """
        self.initialized = True
        print("Motor controller initialized")

    def set_speed(self, left_speed: float, right_speed: float) -> None:
        """
        Set the requested speed for the left and right motors.

        Args:
            left_speed: Normalized speed command for the left motor.
                Expected range is typically -1.0 to 1.0, where:
                - negative means reverse
                - zero means stop
                - positive means forward
            right_speed: Normalized speed command for the right motor.
                Expected range is typically -1.0 to 1.0.

        Raises:
            RuntimeError: If the controller has not been initialized.

        Returns:
            None
        """
        if not self.initialized:
            raise RuntimeError("Motor controller not initialized")

        print(
            f"Set motor speeds -> left: {left_speed:.2f}, right: {right_speed:.2f}"
        )

    def stop(self) -> None:
        """
        Stop both motors safely.

        In the current version, this prints a stop message.
        In future versions, it will set motor PWM to zero and disable motion.

        Returns:
            None
        """
        if self.initialized:
            print("Motors stopped")