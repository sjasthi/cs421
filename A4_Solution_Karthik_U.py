##############################################################
# Autor: Karthik U
# Program: A4 (CS421@SILC)
##############################################################

#The user for the input 
day = input ("what day is today? ")

#convert the input to uppercase
day = day.upper()
print ("After upper case", day)
#grab the first three characters
day = day[0:3]
print ("After three characters", day)


#Print today's date - first letters of the day entered
print("Today's date is : ", day)

#use these conditions to branch off
if (day == "MON"): 
   Print("1. Attend school class for most of the day")
   Print("2. Eat my lunch")
   Print("3. finish your school work")
   Print("4. Eat a snack")
   Print("5. Have dinner")
   Print("6. Drink some milk")
   Print("7. Go to bed")
elif (day == "TUE"):
   Print("1. Attend school class for most of the day")
   Print("2. Eat my lunch")
   Print("3. finish your school work")
   Print("4. Eat a snack")
   Print("5. Have dinner")
   Print("6. Drink some milk")
   Print("7. Go to bed")
elif (day == "WED"):
   Print("1. Attend school class for most of the day")
   Print("2. Eat my lunch")
   Print("3. finish your school work")
   Print("4. Eat a snack")
   Print("5. Have dinner")
   Print("6. Drink some milk")
   Print("7. Go to bed")
elif (day == "THU"):
   Print("1. Attend school class for most of the day")
   Print("2. Eat my lunch")
   Print("3. finish your school work")
   Print("4. Eat a snack")
   Print("5. Have dinner")
   Print("6. Drink some milk")
   Print("7. Go to bed")
elif (day == "FRI"):
   Print("1. Attend school class for most of the day")
   Print("2. Eat my lunch")
   Print("3. finish your school work and CS421@SILC assignment due")
   Print("4. Eat a snack")
   Print("5. Have dinner")
   Print("6. Drink some milk")
   Print("7. Go to bed")
elif (day == "SAT"):
   Print("1.Get ready for the day")
   Print("2.Eat breakfast")
   Print("3.Attend online SLIC for two hours")
   Print("4.CS421@SILC assignment due with late penalty")
   Print("5.Eat lunch")
   Print("6.Watch some tv")
   Print("7.Have dinner")
   Print("8.Drink milk")
   Print("9.Brush my teeth")
   Print("10.Go to bed")
elif (day == "SUN"):
   Print("1.Get ready for the day")
   Print("2.Eat breakfast")
   Print("Play with brother")
   Print("4.Eat lunch")
   Print("CS421@SILC assignment is published and it will not be graded")
   Print("5.Watch some tv")
   Print("6.Have dinner")
   Print("7.Drink milk")
   Print("8.Brush my teeth")
   Print("9.Go to bed")  
else: 
   print("Error: Sorry! I don’t understand what you are saying")
