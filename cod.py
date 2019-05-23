import mraa
from time import sleep

#Clasa Pin, contine toate metodele necesare utilizarii senzorului si ledurilor
#Metodele care au la finalul numelui cuvantul Sensor sunt folosite strict pentru senzor
#Celelalte metode sunt folosite pentru leduri
class Pin():

    #Constructor gol
    def __init__(self):
        self = self   

    #Metoda folosita pentru initializarea senzorului pe intrarea analogica data de nrPin
    def setSensor(self,nrPin):
        self.pin = mraa.Aio(nrPin)
        self.pin.setBit(12)

    #Metoda care preia datele citite de senzor si le prelucreaza
    def readSensor(self):
        self.raw = self.pin.read()
        self.voltage = self.raw / 819.0 * 1000
        return(voltage)

    #Metoda folosita pentru initializarea ledurilor folosind Gpio
    def setLed(self,nrPin):
        self.pin = mraa.Gpio(nrPin)
        self.pin.dir(mraa.DIR_OUT)
        self.pin.write(0)
        
    #Aprindere led
    def turnOn(self):
        self.pin.write(1)
        
    #Stingere led   
    def turnOff(self):
        self.pin.write(0)

def function(value,Green,Red,SensorLed):

    # Daca valoarea returnata de functia readSensor este mai mare de 2000 inseamna ca senzorul este in aer
    # Ambele leduri de pe breadboard sunt stinse si becul modulului este aprins ceea ce indica ca senzorul poate fi folosit
    if(value>2000):
        Green.turnOff()
        Red.turnOff()
        SensorLed.turnOn()
        print(value + " - Senzorul este in aer!")

    # Daca valoarea returnata de functia readSensor se afla in intervalul (1500 - 2000] inseamna ca senzorul este in pamant uscat
    # Ledul rosu se aprinde avertizand ca pamantul trebuie udat
    # Ledul verde si cel de pe modul raman stinse
    elif(value<=2000 & value>1500):
        Green.turnOff()
        Red.turnOn()
        SensorLed.turnOff()
        print(value + " - Senzorul este in pamant uscat!") 
    
   # Daca valoarea returnata de functia readSensor se afla in intervalul (1000 - 1500] inseamna ca senzorul este in pamant umed
   # Ledul verde se aprinde informandu-ne ca solul nu are nevoie de apa
   # Ledul rosu si cel de pe modul raman stinse
    elif(value<=1500 & value>1000):
        Green.turnOn()
        Red.turnOff()
        SensorLed.turnOff()
        print(value + " - Senzorul este in pamant umed!") 

   # Daca valoarea returnata de functia readSensor este mai mica de 1000 inseamna ca senzorul este in apa
   # Ambele leduri de pe breadboard se vor aprinde avertizand ca senzorul este in apa sau solul este prea umed
   # Ledul de pe modul ramane stins  
    else:
        Green.turnOn()
        Red.turnOn()
        SensorLed.turnOff()
        print(value + " - Senzorul este in apa!") 
    

def main():
    #Initializam ledul modulului senzorului
    SensorLed = Pin()
    SensorLed.setLed(2)

    #Initializam ledul verde 
    Green = Pin()
    Green.setLed(13)

    #Initializam ledul rosu
    Red = Pin()
    Red.setLed(12)

    #Initializam senzorul
    Sensor = Pin()
    Sensor.setSensor(0)

    while(true):
        #Citim valoarea returnata de functia readSensor, afisam valorile citite si informatiile legate de aceasta in consola
        #si aprindem/stingem ledurile in functie de valoarea citita
        current = Sensor.readSensor()

        function(current,Green,Red,SensorLed)
        sleep(2.5)

if __name__ == "__main__":
    main()
