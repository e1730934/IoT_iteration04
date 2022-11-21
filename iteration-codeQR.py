from gpiozero import Button, LED
from dbRequests import *
from screen import *
import cv2, serial

ser = serial.Serial('/dev/ttyACM0', 9600)

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
lcd = LCD()

BUTTON = Button(23)
GREEN_LED = LED(17)
RED_LED = LED(27)


def BlinkingLight(led):
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
    led.on()


def openGate():
    ser.write(1)
    ser.write(0)


def closeGate():
    ser.write(0)
    ser.write(1)


# TODO Verifier que l'employe existe dans la BD, ouvrir la barriere et afficher son nom sur le LCD
def verify(data):
    prenom, nom = data.split(' ')  # Split full name and insert into prenom and nom variables
    prenom = prenom[0].upper() + prenom[1:]   # Capitalize first letter of prenom
    nom = nom[0].upper() + nom[1:]  # Capitalize first letter of nom
    driver = GetStaffByFullName(prenom[0], nom)[0]
    if driver is not None:
        if CheckPassPayed(driver['immatriculation']):
            RED_LED.off()
            openGate()
            GREEN_LED.on()
            LcdAdmited(driver)
            GREEN_LED.off()
            RED_LED.on()
            return False
        else:
            BlinkingLight(RED_LED)
            LcdAccesDenied()
            return False
    else:
        BlinkingLight(RED_LED)
        LcdNotFound()
        print("Want to try again? (y/n)")
        answer = input("")

        if answer.lower() == "n":
            return False


# Cette fonction prend une "bounding box" et la dessine sur le flux video de cv2
def drawBox(bbox):
    points = [(int(bbox[0][i][0]), int(bbox[0][i][1])) for i in range(len(bbox[0]))]
    for i in range(len(points)):
        cv2.line(img, points[i - 1], points[i], (0, 255, 0), 2)
    cv2.putText(img, data, (points[0][0], points[0][1] - 5), cv2.FONT_HERSHEY_SIMPLEX,
                (points[1][0] - points[0][0]) * 0.004, (0, 0, 255), 1, cv2.LINE_AA)


closeGate()

while True:
    try:
        _, img = cap.read()
        data, bbox, _ = detector.detectAndDecode(img)
        if bbox is not None:
            drawBox(bbox)
            if data:
                verify(data)
                break
        cv2.imshow("img", img)
        if cv2.waitKey(1) == ord("q"):
            break
    except KeyboardInterrupt:
        lcd.clear()
        break
    except Exception as e:
        pass

cap.release()
cv2.destroyAllWindows()

