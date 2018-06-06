import motor_factory as mf

import xml.etree.ElementTree as ET
from array import array
from random import random

my_arr = array('d', (random() for i in range(1000)))
print(my_arr[100])
all_motors = {}  # Use a dictionary to store the motors
print("Element tree imported.")
tree = ET.parse('config.xml')
print("Tree  = ", tree)
root = tree.getroot()

scanner = root.tag
print("Config read for scanner", scanner)

config_date = root.attrib["date"]
config_version = root.attrib["version"]
print("date =", config_date)
print("version =", config_version)
print()

for motor in root.iter("motor"):
    motor_type = motor.attrib["type"]
    motor_name = motor.attrib["name"]
    config = {}
    motor_units = motor.findtext("units")
    motor_steps_per_unit = motor.findtext("motor_steps_per_unit")
    motor_cooperate_with = motor.findtext("cooperate_with")
    allowed_directions = []
    for allowed_direction in motor.findall("allowed_direction"):
        allowed_directions.append(allowed_direction.text)
    safe_direction = motor.findtext("safe_direction")
    safe_position = motor.findtext("safe_position")
    min_posn = motor.findtext("position/min")
    max_posn = motor.findtext("position/max")
    park_posn = motor.findtext("position/park")
    initialise_posn = motor.findtext("position/initialise")
    if motor_type == "filter_bar":
        filters = {}
        for a_filter in motor.findall("filter"):
            filter_name = a_filter.attrib["name"]
            filters[filter_name] = a_filter.findtext("position")
        config["filters"] = filters
        print("filters = ", filters)

    config["name"] = motor_name
    config["allowed_directions"] = allowed_directions
    config["cooperate_with"] = motor_cooperate_with
    config["initialise_position"] = initialise_posn
    config["max_position"] = max_posn
    config["min_position"] = min_posn
    config["park_position"] = park_posn
    config["safe_direction"] = safe_direction
    config["safe_position"] = safe_position
    config["steps_per_unit"] = motor_steps_per_unit
    config["units"] = motor_units

    print(motor_type)
    print("-----------")
    print("motor name =", motor_name)
    print("motor units =", motor_units)
    print("motor steps per unit =", motor_steps_per_unit)
    print("cooperate with =", motor_cooperate_with)
    print("min = ", min_posn)
    print("max = ", max_posn)
    print("park = ", park_posn)
    print("initialise = ", initialise_posn)
    print("allowed directions = ", allowed_directions)
    print("safe direction = ", safe_direction)
    print("safe position = ", safe_position)

    # Create the motor from the config file
    new_motor = mf.create_motor(motor_type=motor_type, config=config)
    print("new motor = ", new_motor)
    print()
    all_motors[motor_name] = new_motor

print("all motors")
print(all_motors)
