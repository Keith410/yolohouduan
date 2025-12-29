from datetime import datetime
from flask import jsonify

from ultralytics import YOLO
from PIL import Image, ImageDraw,ImageFont
import random
import os
num_objects=0
def predict_image(image_data):
    model = YOLO("C:\\Users\\陈yk\\Desktop\\智能系统作业\\大作业\\一级项目Ⅱ(1)\\一级项目Ⅱ\\FlaskHouduan\\flaskb\\WWW\\bestv11a.pt")

    result = model.predict(image_data)

    for r in result:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image


        random_num = random.randint(0, 100)

        filename = datetime.now().strftime("%Y%m%d%H%M%S") + "_" + str(random_num) + "." + image_data.rsplit('.', 1)[1]

        saveOutputs = "C:\\Users\\陈yk\\Desktop\\智能系统作业\\大作业\\一级项目Ⅱ(1)\\一级项目Ⅱ\\FlaskHouduan\\flaskb\\WWW\\outputs\\" + filename

        num_objects = len(r.boxes)
        # 在图像上显示检测的物体数量
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("arial.ttf", 30)
        draw.text((10, 10), f"Fish Number: {num_objects}", fill=(255, 0, 0), font=font)
        
        im.save(saveOutputs)



    return filename

def returnNum():
    return num_objects