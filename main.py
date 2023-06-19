import cv2
import time
import easyocr
from datetime import datetime


plat_detector =  cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
parking = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
vacant = [0,0,0,0,0,0,0,0]
hours = [0,0,0,0,0,0,0,0]
car = [0,0,0,0,0,0,0,0]
video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FPS, 10)
reader = easyocr.Reader(['en'])

while True:
    try:
        ret, frame = video.read()
        gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        plate = plat_detector.detectMultiScale(gray_video, scaleFactor=1.2, minNeighbors=5, minSize=(25, 25))
        for (x, y, w, h) in plate:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imshow('NumPlate', frame)
            license_plate = frame[y:y + h, x:x + w, :]
            output = reader.readtext(license_plate)
            lp = output[-1][1]
            cr = output[-1][2]
            if (cr > 0.6):
                check = 0
                for i in vacant:
                    if i == 0:
                        a = vacant.index(i)
                        car[a] = lp
                        now = datetime.now()
                        current_time = now.strftime("%H")
                        hours[a] = current_time
                        print(lp, "go to", parking[a],"and your time of entry is",current_time)
                        vacant[a] = 1
                        check = 1
                        break
                if check == 0:
                    print("parking full bro")
                time.sleep(7)
            cv2.imshow('License Plate', license_plate)
    except IndexError:
        pass


    if ret == True:
        cv2.imshow('Video', frame)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    else:
        break


time.sleep(5)

while True:
    try:
        ret, frame = video.read()
        gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        plate = plat_detector.detectMultiScale(gray_video, scaleFactor=1.2, minNeighbors=5, minSize=(25, 25))
        for (x, y, w, h) in plate:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imshow('NumPlate', frame)
            license_plate = frame[y:y + h, x:x + w, :]
            output = reader.readtext(license_plate)
            lp = output[-1][1]
            cr = output[-1][2]
            if (cr > 0.6):
                check = 0
                for i in car:
                    if lp == i:
                        a = car.index(i)
                        print(lp, "Pay ₹60")
                        vacant[a] = 0
                        break

                time.sleep(7)
            cv2.imshow('License Plate', license_plate)
    except IndexError:
        pass


    if ret == True:
        cv2.imshow('Video', frame)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()