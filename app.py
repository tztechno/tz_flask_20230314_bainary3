
import cv2
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    thres=128
    if request.method == 'POST':
        thres=int(request.form.get('thres', '128'))
        print('you selected',thres)
        img = cv2.imread('static/sample.png')
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('static/gray_img.png', gray_img)
        threshold_val = thres
        max_val = 255
        threshold_type = cv2.THRESH_BINARY
        _, binary_img = cv2.threshold(gray_img, threshold_val, max_val, threshold_type)
        cv2.imwrite('static/binary_img.png',binary_img)

        return render_template('index.html',thres=thres)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

