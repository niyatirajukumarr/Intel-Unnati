import cv2
import serial
import time
import numpy as np

arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)
cap = cv2.VideoCapture(0)

def detect_color(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    red_lower = np.array([0, 120, 70])
    red_upper = np.array([10, 255, 255])
    green_lower = np.array([40, 70, 70])
    green_upper = np.array([80, 255, 255])
    blue_lower = np.array([100, 150, 0])
    blue_upper = np.array([140, 255, 255])
    
    mask_red = cv2.inRange(hsv, red_lower, red_upper)
    mask_green = cv2.inRange(hsv, green_lower, green_upper)
    mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)
    
    if cv2.countNonZero(mask_red) > 500:
        return 'R', (0, 0, 255)
    elif cv2.countNonZero(mask_green) > 500:
        return 'G', (0, 255, 0)
    elif cv2.countNonZero(mask_blue) > 500:
        return 'B', (255, 0, 0)
    else:
        return 'N', (255, 255, 255)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape
    roi = frame[height//2 - 50: height//2 + 50, width//2 - 50: width//2 + 50]
    color, bgr = detect_color(roi)

    if color != 'N':
        arduino.write(color.encode())

    cv2.rectangle(frame, (width//2 - 50, height//2 - 50), (width//2 + 50, height//2 + 50), bgr, 2)
    cv2.putText(frame, f"Detected: {color}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, bgr, 2)

    cv2.imshow("Object Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
