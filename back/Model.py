import pandas as pd
# 행렬 연산 패키지
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

# 데이터 분할: train, test
from sklearn.model_selection import train_test_split
# 예측/회귀 Decision test
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


def load_model1():
    result = None
    try:
        print("================Modeling================")
        model_1 = pd.read_excel(
            './a03_DataSet/model1_dataset_adj.xlsx', sheet_name='Sheet1')
        model_1 = pd.get_dummies(model_1.drop('customer_id', axis=1))
        def f(x): return 0 if x > 0 else 1
        model_1['risk'] = model_1['insu_risk_expense'].apply(f)
        model_1_y = model_1['risk']
        model_1_x = model_1.drop(
            ['insu_risk_expense', 'risk'], axis=1, inplace=False)

        df_train_x, df_test_x, df_train_y, df_test_y = train_test_split(
            model_1_x, model_1_y, test_size=0.3, random_state=1234)
        print("===============================222222=================")
        tree_final = DecisionTreeClassifier(
            min_samples_leaf=86, max_depth=5, random_state=1234)
        result = tree_final.fit(df_train_x, df_train_y)
    except Exception as e:
        print("================MODELING ERROR================")
        print(e)
    return result


def load_model2():
    result = None
    try:
        print("================Modeling================")
        df_raw = pd.read_excel(
            './a03_DataSet/model2_dataset_adj.xlsx', sheet_name='Sheet1')
        df_raw = pd.get_dummies(df_raw.drop('customer_id', axis=1))
        df_raw.dropna(inplace=True)
        df_raw_y = df_raw["risk"]
        df_raw_x = df_raw.drop(
            ['insu_risk_expense', 'risk'], axis=1, inplace=False)

        df_train_x, df_test_x, df_train_y, df_test_y = train_test_split(
            df_raw_x, df_raw_y, test_size=0.3, random_state=1234)
        v_feature_name = df_train_x.columns
        scaler = StandardScaler()
        df_scaled_x = scaler.fit_transform(df_raw_x)
        df_scaled_x = pd.DataFrame(df_scaled_x, columns=v_feature_name)

        df_train_x, df_test_x, df_train_y, df_test_y = train_test_split(
            df_scaled_x, df_raw_y, test_size=0.3, random_state=1234)
        nn_scaled = MLPClassifier(random_state=1234)
        nn_scaled.fit(df_train_x, df_train_y)

        nn_final = MLPClassifier(
            activation='logistic', solver='adam', batch_size=35, random_state=1234)
        print(nn_final.fit(df_train_x, df_train_y))
        result = nn_final.fit(df_train_x, df_train_y)
    except Exception as e:
        print("================MODELING ERROR================")
        print(e)
    return result


def load_model_Lasso():
    result = None
    try:
        # Load Train Data
        print("================Modeling================")
        df1 = pd.read_csv("model_data.csv", encoding="cp949")
        print("학습 데이터 row / column 수 : ", df1.shape)

        # Data Preprocessing
        df1["WEIGHT"] = df1["WEIGHT"].fillna(df1["WEIGHT"].mean())
        df1 = df1.dropna()

        # Select Target
        X = df1[["AGE", "WEIGHT", "RUNTIME", "RUNPULSE", "RSTPULSE", "MAXPULSE"]]
        Y = df1[["OXY"]]
        print("설명 변수 데이터 row/column 수 : ", X.shape)
        print("목표 변수 데이터 row/column 수 : ", Y.shape)

        print("================Split Data================")
        # Split Data set
        X_train, X_test, Y_train, Y_test = train_test_split(
            X, Y, test_size=0.3, random_state=1234
        )
        print("Train X 데이터 row/column 수 :", X_train.shape)
        print("Test X 데이터 row/column 수 :", X_test.shape)
        print("Train Y 데이터 row/column 수 :", Y_train.shape)
        print("Test Y 데이터 row/column 수 :", Y_test.shape)

        # Fitting Model
        model = Lasso()
        result = model.fit(X_train, Y_train)

    except Exception as e:
        print("================MODELING ERROR================")
    finally:
        pass
    return result


def model_Score_Lasso():
    result = None
    try:
        # Load Train Data
        print("==========MODEL SCORE==========")
        # df1 = pd.read_csv("model_data.csv", encoding="cp949")
        result = jsonify([{
            "img": "",
            "name": "강태훈",
            "designation": "Throat Specialist",
            "content":
            "Libero perspiciatis sequi delectus, maxime, voluptatum minima nam amet ultrices",
            "socials": [
                {
                    "icon": "facebook-f",
                    "url": "https://facebook.com"
                },
                {
                    "icon": "twitter",
                    "url": "https://twitter.com"
                },
                {
                    "icon": "linkedin-in",
                    "url": "https://linkedin.com"
                },
                {
                    "icon": "instagram",
                    "url": "https://instagram.com"
                }
            ]
        }])

    except Exception as e:
        print("==========MODEL SCORE ERROR==========")
        print(e)
    finally:
        pass
    return result
