#reading temp from the hat, kill the program using Ctrl-C
import explorerhat as hat
import time
def main():
  #print("Hello World!")
  try:
     while True:
       temp = hat.analog.one.read()
       #converting voltage to celcius
       temp = 25 + (temp - 0.75) * 100
       print(temp)
       if temp > 34:
         hat.output.one.on()
         time.sleep(1)
         hat.output.one.off()
       time.sleep(1)
  except KeyboardInterrupt:
    pass
if __name__== "__main__":
  main()
print("lol")