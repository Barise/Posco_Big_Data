from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import Model
import pandas as pd
import numpy as np

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route("/company/manage", methods=["post"])
def judgeBloodTest():
    print(request.json)
    resultFunc = Model.load_model1()
    inputValue = request.json
    gender = inputValue['params']['gender']
    age = int(inputValue['params']['age'])
    height = int(inputValue['params']['height'])
    weight = int(inputValue['params']['weight'])
    waist = float(inputValue['params']['waist'])
    bp_min = int(inputValue['params']['bp_min'])
    bp_max = int(inputValue['params']['bp_max'])
    bmi = weight / ((height * height) / 10000)
    resultDF = pd.DataFrame()
    if gender == 'M':
        resultDF = pd.DataFrame({'age': [age], 'bmi': [bmi], 'waist': [waist], 'bp_min': [
                                bp_max], 'bp_max': [bp_max], 'gender_F': [0], 'gender_M': [1]})

    elif gender == 'F':
        resultDF = pd.DataFrame({'age': [age], 'bmi': [bmi], 'waist': [waist], 'bp_min': [
                                bp_max], 'bp_max': [bp_max], 'gender_F': [1], 'gender_M': [0]})

    result = resultFunc.predict(resultDF)

    if isinstance(result[0], np.integer):
        ans = int(result[0])
    return jsonify({'judge': [ans]})


@app.route("/company/bloodtest", methods=["post"])
def resultBloodTest():
    resultFunc = Model.load_model2()
    inputValue = request.json
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(request.json)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    gender = inputValue['params']['gender']
    age = int(inputValue['params']['age'])
    height = int(inputValue['params']['height'])
    weight = int(inputValue['params']['weight'])
    waist = float(inputValue['params']['waist'])
    bp_min = int(inputValue['params']['bp_min'])
    bp_max = int(inputValue['params']['bp_max'])

    bmi = weight/((height*height)/10000)

    bt_chol = int(inputValue['params']['bt_chol'])
    bt_gluc = int(inputValue['params']['bt_gluc'])
    bt_rgpt = int(inputValue['params']['bt_rgpt'])
    bt_sgot = int(inputValue['params']['bt_sgot'])
    bt_sgpt = int(inputValue['params']['bt_sgpt'])

    if gender == 'M':
        resultDF = pd.DataFrame({'age': [age], 'bmi': [bmi], 'waist': [waist], 'bp_min': [bp_max], 'bp_max': [bp_max], 'bt_chol': [
                                bt_chol], 'bt_gluc': [bt_gluc], 'bt_rgpt': [bt_rgpt], 'bt_sgot': [bt_sgot], 'bt_sgpt': [bt_sgpt], 'gender_F': [0], 'gender_M': [1]})

    elif gender == 'F':
        resultDF = pd.DataFrame({'age': [age], 'bmi': [bmi], 'waist': [waist], 'bp_min': [bp_max], 'bp_max': [bp_max], 'bt_chol': [
                                bt_chol], 'bt_gluc': [bt_gluc], 'bt_rgpt': [bt_rgpt], 'bt_sgot': [bt_sgot], 'bt_sgpt': [bt_sgpt], 'gender_F': [1], 'gender_M': [0]})

    result = resultFunc.predict(resultDF)

    if isinstance(result[0], np.integer):
        ans = int(result[0])
    return jsonify({'judge': [ans]})


@ app.route("/customer/recommend", methods=["post"])
def customerRecommend():
    print(request.json)
    tempValue = sampleModel.model_Score_Lasso()
    return tempValue


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
