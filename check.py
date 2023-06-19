import cv2

cam  = cv2.VideoCapture(0)
image_counter = 0

while True:
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed")
            break

        cv2.imshow("PT2", frame)


        k = cv2.waitKey(1)
        if obj == "car":
            img_name = f"car{image_counter}.png"
            cv2.imwrite(img_name,frame)
            image_counter += 1
            break
        elif k % 256 == 27:
            cam.release()
            cam.destroy()
        else:
            cam.release()
            cam.destroy()

