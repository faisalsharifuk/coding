# pseudocode begins here
# declare first variable num1 as a float with upfront value
# declare second variable num2 as an integer with upfront value
# declare third variable num3 as an integer with upfront value
# declare fourth variable string1 as a string with upfront value
# convert num1 into an integer using the cast function int()
# convert num2 into a float using the cast function float()
# convert num3 into a String using the cast function str()
# convert string1 into an integer using the cast function int()
# print variable num1 on first line
# print variable num2 on second line
# print variable num3 on third line
# print variable string1 on fourth line

# program begins here

# declare variables with fixed values
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

# perform casting on variables
num1 = int(num1)
num2 = float(num2)
num3 = str(num3)
string1 = int(string1)

# print variables on separate lines using f-string
print(f"First variable num1 after casting is integer type: {num1}")
print(f"Second variable num2 after casting is float type: {num2}")
print(f"Third variable num3 after casting is string type: {num3}")
print(f"Fourth variable string1 after casting is integer type: {string1}")