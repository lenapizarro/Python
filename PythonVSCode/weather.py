#This code uses conditionals

temperature = int(input("What is the current temperature?\n"))

if temperature > 80:
    print("It's too hot! Stay inside!")
elif temperature < 60:
    print("It's too cold, stay inside!")
else:
    print("Enjoy the outdoors!")


# ------------------------------------------------------------
# Understanding other conditionals and other logical operators
# -------------------------------------------------------------

temperature2 = int(input("What is the current temperature?\n"))
forecast = 'rain'

if temperature2 > 80 or temperature2 < 60 and forecast != 'cloudy': #Using 61: first or = FALSE, and = TRUE => else will be executed 
    print("Stay inside!")                                           #Using 40: first or = TRUE, and = TRUE => all is true, condition will be executed
else:
    print("Enjoy the outdoors!")

