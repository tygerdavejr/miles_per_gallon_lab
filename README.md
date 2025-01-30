# CIS131_Miles_Per_Gallon_Lab
Determine miles per gallon

PROGRAM Target Heart Rate
David Vance
CIS 131 - Programming and Problem Solving II
Professor Kevin Chang
29 January 2025

# INITIATIONS
# Import modules, declare CONSTANTS, set variables, build dictionaries and 
# build classes

CONSTANT SENTINEL = 0

FUNCTION input Age()
    # Ask user for age and confirm it is an integer value
    TRY: 
        age = integer INPUT "Enter an age between 1 and 110 (or 0 to exit)"
    EXCEPT ValueError:
        PRINT "Your entry must be an integer.  Please try again."
    ELSE:
        RETURN age
END FUNCTION 


FUNCTION determine Age()
    # Ask user for age and validate input for integer, SENTINEL and within age range
    age = input age() from FUNCTION
    # Loop until age is within target range or exit program early
    WHILE age < 1 or age > 110:
        IF age == SENTINEL:
            PRINT "\nThank you for using Heart Rate Calculator"
            FORCE EARLY PROGRAM EXIT
        PRINT "\n *** Please enter an age between 1 and 110 (or 0 to exit) ***"
        age = input age() from FUNCTION
    RETURN age
END FUNCTION


FUNCTION determine target heart rates (age)
    # Calculate the maximum heart rate first (220 - age), then calculate the 
    # low target heart rate (50%) and high target heart rate (85%) from that value.
    maximum heart rate = 220 - age
    low target heart rate = maximum heart rate * .5
    high target heart rate = maximum heart rate * .85
    return low target heart rate, high target heart rate
END FUNCTION


# MAIN PROCESSING
# Call to main() function, intitiate processing, print reports, end program

FUNCTION main()
    # Display header for report
    PRINT "This module determines target heart rate based on an age"
    PRINT "value of 1 to 110."   
    age = determine age() from FUNCTION
    low target heart rate and high target heart rate = determine target heart rates(age) from FUNCTION  # Pass this back as a tupile
    PRINT "At age " + age
    PRINT "Target heart rate is between " + minimum heart rate + " and " + maximum heart rate" 
END FUNCTION

# PROGRAM ENTRY POINT

IF __name__ == "__main__" THEN
    CALL main()
END IF


END PROGRAM



LAB PARAMETERS
Drivers are concerned with the mileage obtained by their automobiles. One driver has kept track of several tankfuls of gasoline
by recording miles driven and gallons used for each tankful. Develop a sentinel-controlled-repetition script that prompts the 
user to input the miles driven and gallons used for each tankful. The script should calculate and display the miles per gallon 
obtained for each tankful. After processing all input information, the script should calculate and display the combined miles 
per gallon obtained for all tankfuls (that is, total miles driven divided by total gallons used).


Enter the gallons used (-1 to end): 12.8
Enter the miles driven: 287
The miles/gallon for this tank was 22.421875
Enter the gallons used (-1 to end): 10.3
Enter the miles driven: 200
The miles/gallon for this tank was 19.417475
Enter the gallons used (-1 to end): 5
Enter the miles driven: 120
The miles/gallon for this tank was 24.000000
Enter the gallons used (-1 to end): -1
The overall average miles/gallon was 21.601423

You will need to use your IDE to complete this assignment. Once completed, please submit your .py file to D2L. 
