import cv2
from flask import Flask, render_template, Response

app = Flask(__name__)
video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_BUFFERSIZE, 1)

def video_stream():
    while True:
        ret, frame = video.read()
        if not ret:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def greet():
    return "hello world"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
