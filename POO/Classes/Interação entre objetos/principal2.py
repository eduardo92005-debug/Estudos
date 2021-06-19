from ClockDisplay import ClockDisplay

def main():
   #O relogio foi setado para 22:56 no construtor
   relogio = ClockDisplay()
   print(relogio.getTime())
   for i in range(124): #Acionei 124 vezes para chegar a 1 hora
      relogio.timeTick()
   print(relogio.getTime())
   #Poderiamos exibir essa hora usando o metodo setTime()
main()
