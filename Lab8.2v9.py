import cv2
import numpy as np

fly_img = cv2.imread('fly64.png', cv2.IMREAD_UNCHANGED)

cap = cv2.VideoCapture(0)

total_x, total_y, frame_count = 0, 0, 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Ошибка: не удалось получить кадр.")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            total_x += cx
            total_y += cy
            frame_count += 1

            fly_resized = cv2.resize(fly_img, (64, 64))
            x_offset = cx - 32
            y_offset = cy - 32

            if x_offset >= 0 and y_offset >= 0 and x_offset + 64 <= frame.shape[1] and y_offset + 64 <= frame.shape[0]:
                alpha = fly_resized[:, :, 3] / 255.0
                alpha_inv = 1.0 - alpha

                for c in range(0, 3):
                    frame[y_offset:y_offset + 64, x_offset:x_offset + 64, c] = \
                        fly_resized[:, :, c] * alpha + \
                        frame[y_offset:y_offset + 64, x_offset:x_offset + 64, c] * alpha_inv

    cv2.imshow('Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if frame_count > 0:
    avg_x = total_x / frame_count
    avg_y = total_y / frame_count
    print(f"Средняя координата центра метки: ({avg_x}, {avg_y})")

cap.release()
cv2.destroyAllWindows()