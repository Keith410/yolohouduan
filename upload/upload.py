import sys
sys.path.append("C:\\Users\\陈yk\\Desktop\\flaskb\\WWW")#更改为当前项目的绝对地址
import base64
import io
from datetime import datetime
from flask import Flask, request, jsonify, send_from_directory
import os
import random
from werkzeug.utils import secure_filename
from predict import predict_image
from PIL import Image

# # 获取当前位置的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

#获取上传图片并推理
@app.route("/post",methods=["POST"])
def post():
    if request.method == 'POST':
        img_base64 = request.form.get('picture')
        image = base64.b64decode(img_base64)
        image =Image.open(io.BytesIO(image))
        save_path = "C:\\Users\\陈yk\\Desktop\\flaskb\\WWW\\inputs\\inputs."+ image.format.lower()
        image.save(save_path)
        #返回输出的图片的名称
        res = predict_image(save_path)
        data = {"msg": "success","res":res}
        payload = jsonify(data)
    return payload


#将推理结果返回前端
@app.route("/outputs/<path:filename>", methods=["GET"])
def get(filename):
   
    return send_from_directory('C:\\Users\\陈yk\\Desktop\\flaskb\\WWW\\outputs', filename)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
