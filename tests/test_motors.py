"""
Basic tests for the motor controller abstraction.
"""

from src.motors import MotorController


def test_motor_controller_starts_uninitialized() -> None:
    """
    Verify that a new MotorController starts in an uninitialized state.

    Returns:
        None
    """
    controller = MotorController()
    assert controller.initialized is False


def test_motor_controller_initializes() -> None:
    """
    Verify that calling initialize sets the controller state correctly.

    Returns:
        None
    """
    controller = MotorController()
    controller.initialize()
    assert controller.initialized is True