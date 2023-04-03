

def time_split(time):
    hour = time.split(":")[0]
    min = time.split(":")[1]

    return [hour, min]

def howManyHoursMore(startingMinutes, addedMinutes):
    totalMinutes = startingMinutes + addedMinutes

    extraHours = totalMinutes // 60

    remainingMinutes = totalMinutes % 60 

    return [extraHours, remainingMinutes]

def howManyDaysMore(startingHours, addedHours):
    totalHours = startingHours + addedHours

    extraDays = totalHours // 24
    extraFlips = totalHours // 12

    remainingHours = totalHours % 24
    
    if (remainingHours // 12) > 0:
        ##extraFlips = extraFlips + 1 
        remainingHours = remainingHours - 12

    return [extraDays, extraFlips, remainingHours]

def whichLetters(startingLetters, flips):
    if (flips % 2) == 0 : return startingLetters
    elif startingLetters == "PM" : return "AM"
    else : return "PM"

def whichDay(day, daysPassed):
    thisDay = day.lower()
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    indNewDay = (days.index(thisDay) + daysPassed) % 7
    newDay = days[indNewDay]

    return newDay
    

def add_time(startingTime, addedTime, day) : 
    sHours = int(time_split(startingTime.split()[0])[0])
    sMinutes = int(time_split(startingTime.split()[0])[1])
    letters = startingTime.split()[1]

    aHours = int(time_split(addedTime.split()[0])[0])
    aMinutes = int(time_split(addedTime.split()[0])[1])

    hmhm = howManyHoursMore(sMinutes, aMinutes)
    hmdm = howManyDaysMore(sHours, aHours + hmhm[0])    

    if(letters == "PM" and (hmdm[1] % 2) == 1) : hmdm[0] = hmdm[0] + 1         

    if hmhm[1] < 10 :
        fMinutes = "0" + str(hmhm[1])
    else:
        fMinutes = str(hmhm[1])

    fHour = str(((sHours + hmdm[2]) % 12) + 1 )

    pmOrAm = whichLetters(letters, hmdm[1])

    extraDays = hmdm[0]

    dotw = whichDay(day, extraDays)

    if(extraDays == 1):
        finalTime = fHour + ":" + fMinutes + " " + pmOrAm + ", " + dotw + " (next day)"
    elif(extraDays > 1):
        finalTime = fHour + ":" + fMinutes + " " + pmOrAm + ", " + dotw + " (" + str(extraDays) + " days later)"
    else:
        finalTime = fHour + ":" + fMinutes + " " + pmOrAm 

    return finalTime

print( add_time("11:43 PM", "54:10", "MondaY") )

