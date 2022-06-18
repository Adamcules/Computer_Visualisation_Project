import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('keras_model.h5')


def camera_loop():
    global cap
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    now = time.time()
    timer = 0
    while True:
        end = time.time()
        timer = (end - now)

        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        global prediction 
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # Timer closes window after 5 seconds
        if timer >= 5:
            break

def run_model():
    camera_loop()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_model()           

