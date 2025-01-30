"""
    script: miles_per_gallon_lab.py
    action: a. Determines miles-per-gallon from input
            b. Prints a cumulative MPG when user desires to quit.
            c. SENTINEL check on gallons_used only
    author: David Vance
    date: 29 January 2025
"""

#global variables
SENTINEL = -1


def input_age():
    """
    Prompt user for age, then checks for the following conditions:
    - If the age is not an integer, capture the error, print an error
      message and prompt the user for another value
    - If the age is the SENTINEL, print an exit message and exit module
    - If the age does not fall within the expected range of 1 to 110,
      print an error message and prompt the user for another value

    action: Prompt user for age.  Loop while the age is not an integer, is
            not the SENTINEL value, or falls outside of limited values.
            Exit the method when age is an integer and falls within
            allowed range of 1 to 110.
    input:  age
    output: entry prompt, error message (if needed)
    return: age
    """
    # local variables
    age = ''

    # Loop while age has a null value
    while not age:
        try: 
            # Prompt user for age as an integer
            age = int(input("Enter an age between 1 and 110 (or -99 to exit): "))

            if age == SENTINEL:
                # If age == SENTINEL print message and exit module
                print("\nThank you for using Heart Rate Calculator.\n")
                raise SystemExit

            elif age < 1 or age > 110:
                # Else if age is not in expected range print message and reset input loop
                print("\n*** The age must be between 1 and 110 (or -99 to exit) ***")
                age = ''
    
        except ValueError:
            # Capture error if age is not an integer    
            print("\n*** Your entry must be an integer.  Please try again. ***")
    return age


def function():
    """
    Description.  

    action: 
    input:  
    output: 
    return: 
    """
    # Logic notes
    


    return 


# MAIN PROCESSING
# Call to main() function, intitiate processing, print reports, end program

def main():
    """
    Description.
    
    action: 
    input:  
    output: 
    return: 
    """

    
    # Display Heart Rate report
    print(f'\nAT AGE {age}')
    print(f'Target heart rate is between {lowTargetHeartRate:.0f} and {highTargetHeartRate:.0f}.')
    print("\nThank you for using Heart Rate Calculator.\n")

    return


if __name__ == '__main__':
    main()
