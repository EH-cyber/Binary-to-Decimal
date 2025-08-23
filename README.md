# Binary-to-Decimal

This will currently give you the ability to convert base 10 numbers to base 2 (binary) numbers.  I am working on updating the code to allow for a fourth and fifth option in which users would be able to also convert to and from hex.  With that a seventh and eighth option may ensue which would allow for the conversion from hex to base 10.

Update: 22 August 2025
Created newBinary.py
This is the updated version of the program and will be the one updated. It will consist of updated comments and functions.

    Functions in this version are:
        * main()
            * This is the main function to run the program including the match-case to determine the users decision of what function to perform
            * Requires no input but will prompt user for input decision and numbers to convert
            * Outputs in
        * toBinary()
            * This function will convert base10, decimal, numbers to binary. This will convert whole numbers and fractions.
            * Input required is decNum
            * decNum is a float number that will be converted
            * Output is a string of binary numbers
        * cleanStr()
            * This function will clean the string of binary from the list made in toBinary()
            * Input required is dirtyNum. Optional input is fracWhole.
                * dirtyNum is the string made in toBinary() that has remenants of the list it came from
                * fracWhole is optional input that should be used for whole numbers. When used the value used should be the number 1
            * Output from this function is a clean string of binary
        *