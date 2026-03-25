# Pin Configuration

## Purpose
This document records the planned electrical mapping between the Raspberry Pi
and the TB6612FNG motor driver.

## Planned GPIO Mapping

### Left Motor
- IN1 -> GPIO 17
- IN2 -> GPIO 27
- PWM -> GPIO 18

### Right Motor
- IN1 -> GPIO 22
- IN2 -> GPIO 23
- PWM -> GPIO 13

## Notes
- Final wiring must be verified physically before powering motors.
- Raspberry Pi must not power the motors directly.
- Motor power will come from a separate supply later.