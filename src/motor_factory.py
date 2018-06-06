import motor
known_motors = ["collimator", "filter_bar", "rotation"]


def create_motor(motor_type, config):
    if motor_type in known_motors:
        if motor_type == "collimator":
            new_motor = motor.CollimatorMotor(config)
        if motor_type == "filter_bar":
            new_motor = motor.FilterBarMotor(config)
        if motor_type == "rotation":
            new_motor = motor.RotationMotor(config)
        return new_motor
    else:
        print("Unrecognised motor type: ", motor_type)
        return None
