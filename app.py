import os
import json
from flask import Flask, render_template, request, jsonify
from face_recognition_service import get_image_with_landmarks

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './incoming'

@app.route('/<string:selectedGender>/<string:pastBirthYear>/<string:placeNumber>', methods=["POST"])
def index(selectedGender, pastBirthYear, placeNumber):
    if selectedGender == "male" and int(pastBirthYear) < 1000 and int(placeNumber) < 25:
        baseImage = "./img/1.jpg"
    elif selectedGender == "male" and 1000 <= int(pastBirthYear) <= 1300 and int(placeNumber) < 25:
        baseImage = "./img/2.jpg"
    elif selectedGender == "male" and 1300 < int(pastBirthYear) <= 1300 and int(placeNumber) < 25:
        baseImage = "./img/3.jpg"
    elif selectedGender == "male" and 1300 < int(pastBirthYear) <= 1600 and int(placeNumber) < 25:
        baseImage = "./img/4.jpg"
    elif selectedGender == "male" and 1600 < int(pastBirthYear) < 1900 and int(placeNumber) < 25:
        baseImage = "./img/5.jpg"
    elif selectedGender == "male" and int(pastBirthYear) < 1000 and 25 <= int(placeNumber) < 50:
        baseImage = "./img/6.jpg"
    elif selectedGender == "male" and 1000 <= int(pastBirthYear) <= 1300 and 25 <= int(placeNumber) < 50:
        baseImage = "./img/7.jpg"
    elif selectedGender == "male" and 1300 < int(pastBirthYear) <= 1300 and 25 <= int(placeNumber) < 50:
        baseImage = "./img/8.jpg"
    elif selectedGender == "male" and 1300 < int(pastBirthYear) <= 1600 and 25 <= int(placeNumber) < 50:
        baseImage = "./img/9.jpg"
    elif selectedGender == "male" and 1600 < int(pastBirthYear) < 1900 and 25 <= int(placeNumber) < 50:
        baseImage = "./img/10.jpg"
    elif selectedGender == "male" and int(pastBirthYear) < 1000 and 50 <= int(placeNumber):
        baseImage = "./img/11.jpg"
    elif selectedGender == "male" and 1000 <= int(pastBirthYear) <= 1300 and 50 <= int(placeNumber):
        baseImage = "./img/12.jpg"
    elif selectedGender == "male" and 1300 < int(pastBirthYear) <= 1300 and 50 <= int(placeNumber):
        baseImage = "./img/13.jpg"
    elif selectedGender == "male" and 1300 < int(pastBirthYear) <= 1600 and 50 <= int(placeNumber):
        baseImage = "./img/30.jpg"
    elif selectedGender == "male" and 1600 < int(pastBirthYear) < 1900 and 50 <= int(placeNumber):
        baseImage = "./img/31.jpg"
    elif selectedGender == "female" and int(pastBirthYear) < 1000 and int(placeNumber) < 25:
        baseImage = "./img/14.jpg"
    elif selectedGender == "female" and 1000 <= int(pastBirthYear) <= 1300 and int(placeNumber) < 25:
        baseImage = "./img/15.jpg"
    elif selectedGender == "female" and 1300 < int(pastBirthYear) <= 1300 and int(placeNumber) < 25:
        baseImage = "./img/16.jpg"
    elif selectedGender == "female" and 1300 < int(pastBirthYear) <= 1600 and int(placeNumber) < 25:
        baseImage = "./img/17.jpg"
    elif selectedGender == "female" and 1600 < int(pastBirthYear) < 1900 and int(placeNumber) < 25:
        baseImage = "./img/18.jpg"
    elif selectedGender == "female" and int(pastBirthYear) < 1000 and 25 <= int(placeNumber) < 50:
        baseImage = "./img/19.jpg"
    elif selectedGender == "female" and 1000 <= int(pastBirthYear) <= 1300 and 25 <= int(placeNumber) < 50:
        baseImage = "./img/20.jpg"
    elif selectedGender == "female" and 1300 < int(pastBirthYear) <= 1300 and 25 <= int(placeNumber) < 50:
        baseImage = "./img/21.jpg"
    elif selectedGender == "female" and 1300 < int(pastBirthYear) <= 1600 and 25 <= int(placeNumber) < 50:
        baseImage = "./img/22.jpg"
    elif selectedGender == "female" and 1600 < int(pastBirthYear) < 1900 and 25 <= int(placeNumber) < 50:
        baseImage = "./img/23.jpg"
    elif selectedGender == "female" and int(pastBirthYear) < 1000 and 50 <= int(placeNumber):
        baseImage = "./img/24.jpg"
    elif selectedGender == "female" and 1000 <= int(pastBirthYear) <= 1300 and 50 <= int(placeNumber):
        baseImage = "./img/25.jpg"
    elif selectedGender == "female" and 1300 < int(pastBirthYear) <= 1300 and 50 <= int(placeNumber):
        baseImage = "./img/26.jpg"
    elif selectedGender == "female" and 1300 < int(pastBirthYear) <= 1600 and 50 <= int(placeNumber):
        baseImage = "./img/27.jpg"
    elif selectedGender == "female" and 1600 < int(pastBirthYear) < 1900 and 50 <= int(placeNumber):
        baseImage = "./img/28.jpg"
    else:
        baseImage = "./img/32.jpg"
    image = request.files["image"]
    path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(path)
    result_from_landmarks = get_image_with_landmarks(path, baseImage)
    os.remove(path)

        # return result_from_landmarks

        # return jsonify({
        #     result_from_landmarks
        # })
    return json.dumps(result_from_landmarks)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port, debug=True)