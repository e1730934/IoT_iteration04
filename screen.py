from rpi_lcd import LCD
#import the Ipython display module clear_output methods
import time

REPEAT_MSG = 3
LCD = LCD()
def LcdDefault(remainingPlaces):
    try:
        LCD.text("Welcome to",1)
        LCD.text("Dalubi parking", 2)
        time.sleep(2)
        LCD.clear()
        LCD.text('Place remaining:',1)
        LCD.text(f'{remainingPlaces} spots', 2)
        time.sleep(5)
            
    finally:
            LCD.clear()


def LcdParkingFull():
    try:     
        LCD.text("Sorry we're",1)
        LCD.text("full for today", 2)
    finally:
        LCD.clear()

def LcdAdmited(name):
    for x in range(0,REPEAT_MSG):
        try:     
            LCD.text("Welcome",1)
            LCD.text(name, 2)
            time.sleep(3)
            LCD.clear()
            LCD.text('Have a good day!',1)
            time.sleep(3)    
        finally:
            LCD.clear()

def LcdAccesDenied():
    for x in range(0,REPEAT_MSG):
        try:     
            LCD.text("Acces denied",1)
            time.sleep(2)
            LCD.clear()
            LCD.text("More details",1)
            LCD.text("at our office", 2)
            time.sleep(2)  
        finally:
            LCD.clear()

def LcdNotFound():
    try:     
        LCD.text("Don't recognise",1)
        LCD.text("your plate", 2)
        time.sleep(3)
        LCD.clear()
        LCD.text('want to try',1)
        LCD.text('again?',1)
        time.sleep(3)    
    finally:
        LCD.clear()