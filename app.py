from flask import Flask, render_template, request
import numpy as np
import os
from werkzeug.utils import secure_filename
import cv2

app = Flask(__name__)
app.config['UPLOAD_IMG'] = 'static'

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        with open('obj.names', 'r') as f:
            classes = f.read().splitlines()

        net = cv2.dnn.readNetFromDarknet("yolov4-obj.cfg", "yolov4-obj_last.weights")
                
        model = cv2.dnn_DetectionModel(net)
        model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
                
        img = cv2.imread(file_path)

        classIds, scores, boxes = model.detect(img, confThreshold=0.6, nmsThreshold=0.4)
                
        for (classId, score, box) in zip(classIds, scores, boxes):
            cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
            color=(0, 255, 0), thickness=2)
                
            text = classes[classId]
            cv2.putText(img, text, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
            color=(0, 255, 0), thickness=2)

        cv2.imwrite("static/detected.jpg", img)

        img_path = os.path.join(app.config['UPLOAD_IMG'], "detected.jpg")

        return render_template('index.html', img_path = img_path)
    return render_template('index.html', img_path = "")

if __name__ == '__main__':
    app.run(debug=True)