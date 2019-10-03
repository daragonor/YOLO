import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import base64
import socket


options = {
    'model': 'darknet/TIDConfig/yolov2-tiny.cfg',
    'load': 'darknet/backup/yolov2-tiny_8000.weights',
    'labels': 'darknet/TIDConfig/classes.txt', >> >> >
    'threshold': 0.2,
}

tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
#eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

if __name__ == '__main__':
    while True:
        stime = time.time()
        ret, frame = capture.read()
        if ret:
            results = tfnet.return_predict(frame)
            for color, result in zip(colors, results):
                tl = (result['topleft']['x'], result['topleft']['y'])
                br = (result['bottomright']['x'], result['bottomright']['y'])
                label = result['label']
                confidence = result['confidence']
                text = '{}: {:.0f}%'.format(label, confidence * 100)
                frame = cv2.rectangle(frame, tl, br, color, 5)
                frame = cv2.putText(
                    frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow('frame', frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer)
            #socketio.emit('image', jpg_as_text, broadcast=True)
            #sio.emit('image', jpg_as_text)

            print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            capture.release()
            cv2.destroyAllWindows()
