import motor_factory as mf

print("Motor program")
print("*********************************************")
print("Possible motors are:-")
print("top_collimator")
print("bottom_collimator")
print("left_collimator")
print("right_collimator")
print("filter_bar")

print("To exit the program, enter the character 'x'")
response = ''
# response = input('Enter the motor type to create.\n')
all_motors = []
while response != 'x':
    if len(response) > 0:
        print('about to create a new motor')
        new_motor = mf.create_motor(response)
        if new_motor:
            print("Created ")
            print(new_motor)
            print("adding motor to the list of all motors created")
            all_motors.append(new_motor.name)
        else:
            print("Not adding motor")
    response = input('Enter the motor type to create.\n')

print("The motors created are ")
print(all_motors)
