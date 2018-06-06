"""
This is the motor class file.
Things not included:
Motor speed
Acceleration
Holding force
Backlash
Direction to approach final position
"""


class BasicMotor:
    current_position = None

    def __init__(self, config=None):
        # The following properties are common to all motors
        self.name = config.get("name")
        print("name = ", self.name)
        self.allowed_directions = config.get("allowed_directions")
        self.cooperate_with = config.get("cooperate_with")
        self.initialise_posn = config.get("initialise_position")
        self.max_posn = config.get("max_position")
        self.min_posn = config.get("min_position")
        self.park_posn = config.get("park_position")
        self.safe_posn = config.get("safe_position")
        self.steps_per_unit = config.get("steps_per_unit")
        self.units = config.get("units")

    def move_to(self, move_to_position=current_position):
        self.current_position = move_to_position
        return self.current_position

    def __str__(self):
        return "Motor " + self.name

    def __repr__(self):
        return "Motor object (" + self.name + ")"


class CollimatorMotor(BasicMotor):
    def __init__(self, config=None):
        # These properties are specific to collimators
        self.safe_direction = config.get("safe_direction")
        super(CollimatorMotor, self).__init__(config)

    def __str__(self):
        return self.name

    def move_by(self, move_amount_mm, move_direction):
        if move_direction in self.allowed_directions and move_amount_mm > 0:
            if self.current_position + move_amount_mm <= self.max_position:
                self.current_position += move_amount_mm
            return self.current_position

    def move_to(self, move_to_position):
        if self.cooperate_with is None:
            print("Can't move a collimator if other collimator's position is unknown")
            return None

        current_to_safe = abs(self.current_position - self.safe_posn)
        new_position_to_safe = abs(move_to_position - self.safe_posn)
        if current_to_safe >= new_position_to_safe:
            self.current_position = move_to_position
            return self.current_position

        other_collimator_to_safe = abs(self.cooperate_with.current_position - self.safe_posn)
        if new_position_to_safe <= other_collimator_to_safe:
            self.current_position = move_to_position
            return self.current_position
        else:
            self.current_position = self.cooperate_with.current_position
            return self.current_position

    def add_to_cooperate_with(self, other_motor):
        self.cooperate_with = other_motor


class FilterBarMotor(BasicMotor):

    def __init__(self, config):
        # These properties are specific to the filter bar
        self.filters = config.get("filters")
        self.safe_direction = config.get("safe_direction")
        super(FilterBarMotor, self).__init__(config)


class RotationMotor(BasicMotor):

    def __init__(self, config):
        # These properties are specific to the rotation motor
        self.safe_direction = config.get("safe_direction")
        super(RotationMotor, self).__init__(config)

    def move_to(self, move_to_position=None):
        self.current_position = move_to_position
        return self.current_position


def main():
    print("The Motors module.")


if __name__ == "__main__":
    main()
