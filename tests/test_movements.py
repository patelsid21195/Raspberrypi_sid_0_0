"""
Tests for high-level robot movement commands.
"""

from src.movement import RobotMovement


class FakeMotorController:
    """
    Fake motor controller used for testing movement commands.

    It records what speed values were requested instead of controlling hardware.
    """

    def __init__(self) -> None:
        """Create a fake motor controller."""
        self.last_left_speed = None
        self.last_right_speed = None
        self.stop_called = False

    def set_speed(self, left_speed: float, right_speed: float) -> None:
        """
        Record requested motor speeds.

        Args:
            left_speed: Requested left motor speed.
            right_speed: Requested right motor speed.
        """
        self.last_left_speed = left_speed
        self.last_right_speed = right_speed

    def stop(self) -> None:
        """Record that stop was called."""
        self.stop_called = True


def test_move_forward_sets_both_motors_forward() -> None:
    """Verify forward movement sets both motors to positive speed."""
    fake_motor = FakeMotorController()
    movement = RobotMovement(fake_motor)

    movement.move_forward(0.3)

    assert fake_motor.last_left_speed == 0.3
    assert fake_motor.last_right_speed == 0.3


def test_move_backward_sets_both_motors_backward() -> None:
    """Verify backward movement sets both motors to negative speed."""
    fake_motor = FakeMotorController()
    movement = RobotMovement(fake_motor)

    movement.move_backward(0.3)

    assert fake_motor.last_left_speed == -0.3
    assert fake_motor.last_right_speed == -0.3


def test_turn_left_sets_opposite_motor_speeds() -> None:
    """Verify left turn sets left backward and right forward."""
    fake_motor = FakeMotorController()
    movement = RobotMovement(fake_motor)

    movement.turn_left(0.3)

    assert fake_motor.last_left_speed == -0.3
    assert fake_motor.last_right_speed == 0.3


def test_turn_right_sets_opposite_motor_speeds() -> None:
    """Verify right turn sets left forward and right backward."""
    fake_motor = FakeMotorController()
    movement = RobotMovement(fake_motor)

    movement.turn_right(0.3)

    assert fake_motor.last_left_speed == 0.3
    assert fake_motor.last_right_speed == -0.3


def test_stop_calls_motor_controller_stop() -> None:
    """Verify stop command calls the motor controller stop method."""
    fake_motor = FakeMotorController()
    movement = RobotMovement(fake_motor)

    movement.stop()

    assert fake_motor.stop_called is True