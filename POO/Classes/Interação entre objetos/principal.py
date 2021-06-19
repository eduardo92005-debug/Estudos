from ClockDisplay import ClockDisplay
from NumberDisplay import NumberDisplay

def main():
   relogio = ClockDisplay()
   print(relogio.getTime())
   relogio.setTime(10,20)
   print(relogio.getTime())
   print(relogio.getHours())
   print(relogio.getMinutes())
main()
