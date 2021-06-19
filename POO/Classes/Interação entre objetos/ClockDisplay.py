from NumberDisplay import NumberDisplay
class ClockDisplay:
    """__hours - classe NumberDisplay
       __minutes - classe NumberDisplay
       __displayString - string"""
    def __init__(self):
        self.__hours = NumberDisplay(24)
        self.__minutes = NumberDisplay(60)
        self.__seconds = NumberDisplay(60)
        self.__updateDisplay()

    def __updateDisplay(self):
        self.__displayString = self.__hours.getDisplayValue() + ":" + self.__minutes.getDisplayValue() + ":" + self.__seconds.getDisplayValue()
    def timeTick(self):
        self.__seconds.increment()
        if(self.__seconds.getValue() == 0):
            self.__minutes.increment()
            if(self.__minutes.getValue() == 0):
                self.__hours.increment()
        self.__updateDisplay()
    #Getters
    def getHours(self):
        return self.__hours.getDisplayValue()
    def getMinutes(self):
        return self.__minutes.getDisplayValue()
    def getSeconds(self):
        return self.__seconds.getDisplayValue()
    def getTime(self):
        return self.__displayString
    #Setters
    def setHours(self,replacementValue):
        self.__hours.setValue(replacementValue)
    def setMinutes(self,replacementValue):
        self.__minutes.setValue(replacementValue)
    def setSeconds(self,replacementValue):
        self.__seconds.setValue(replacementValue)
    def setTime(self,hour,minute,second):
        if(hour < 24 and hour >= 0):
           self.__hours.setValue(hour)
        if (minute < 60 and minute >= 0):
            self.__minutes.setValue(minute)
        if(second < 60 and second >= 0):
            self.__seconds.setValue(second)
        self.__updateDisplay()
