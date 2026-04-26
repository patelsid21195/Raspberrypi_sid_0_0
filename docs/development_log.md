# Development Log

## Session: Robot Movement Software Setup

### Date
2026-04-26

### Goal
Create the first software version of robot movement control before connecting physical motors.

### Work Completed
- Connected to Raspberry Pi using VS Code Remote SSH.
- Reviewed project structure: `src/`, `tests/`, `hardware/`, `docs/`, `scripts/`.
- Created `src/movement.py`.
- Added `RobotMovement` class with movement commands:
  - `move_forward()`
  - `move_backward()`
  - `turn_left()`
  - `turn_right()`
  - `stop()`
- Updated `src/main.py` to run a movement test sequence.
- Confirmed simulated movement works:
  - forward = left/right positive speed
  - backward = left/right negative speed
  - left/right turns = opposite wheel speeds
  - stop = motors stopped
- Added movement tests in `tests/test_movement.py`.
- Fixed import issues by using package-style imports:

```python
from src.motors import MotorController
from src.movement import RobotMovement
```

- Learned to run the app as a module:

```bash
python3 -m src.main
```

- Added VS Code launch configurations for:
  - running the robot main program
  - running pytest tests
- Successfully ran all tests.

### Test Result
```text
8 passed
```

### Problems Faced
- Tried to use `apt` on the MacBook terminal; learned `apt` only works on Raspberry Pi/Linux.
- Import errors happened because code was run as a file instead of as a module.
- Fixed VS Code launch config by using:

```json
"module": "src.main"
```

### Decisions Made
- Keep `main.py` for robot behavior.
- Keep `movement.py` for high-level movement commands.
- Keep `motors.py` for motor control logic.
- Keep `config.py` for GPIO pin settings.
- Run tests before connecting real motors.

### Current Status
The robot movement logic works in software simulation, and all tests pass.

### Next Steps
- Verify TB6612FNG motor driver wiring.
- Confirm GPIO mapping in `hardware/pin_config.md`.
- Use a separate motor power supply.
- Connect Raspberry Pi GND to motor driver GND.
- Replace simulated motor prints with real GPIO/PWM control.
- Test one motor slowly with wheels lifted off the table.
