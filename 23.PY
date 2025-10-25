# BY TAKING INPUT IN WHILE LOOP
pin = "1234"
trials = 1
while trials<= 3:
    input_pin = input(f"trials-{trials} | PIN>> ")
    trials += 1
if input_pin == pin:
    print("CORRECT")
    breakpoint
    

else:
    print("INCORRECT")