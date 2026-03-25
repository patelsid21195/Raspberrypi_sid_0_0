"""
Central configuration for robot hardware and software constants.

This module stores all project-wide constants in one place.
That includes GPIO pin assignments and PWM settings.

Keeping these values centralized makes the system easier to:
- maintain
- debug
- rewire later without changing logic files
"""

# Left motor pin mapping
LEFT_MOTOR_IN1 = 17
LEFT_MOTOR_IN2 = 27
LEFT_MOTOR_PWM = 18

# Right motor pin mapping
RIGHT_MOTOR_IN1 = 22
RIGHT_MOTOR_IN2 = 23
RIGHT_MOTOR_PWM = 13

# PWM configuration
PWM_FREQUENCY = 1000