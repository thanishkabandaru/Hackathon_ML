from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Input form page

@app.route('/predict', methods=['POST'])
def predict():
    # Get form inputs
    present_price = float(request.form['present_price'])
    kms_driven = int(request.form['kms_driven'])
    year = int(request.form['year'])
    owner = int(request.form['owner'])
    fuel = request.form['fuel']
    seller = request.form['seller']
    transmission = request.form['transmission']

    # ======== ML Prediction Logic ========
    # Replace this dummy logic with your trained model
    predicted_price = present_price * 0.8  # Dummy example
    # =====================================

    return render_template('prediction.html', predicted_price=predicted_price)

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # from flask import Flask, render_template, request
# import pandas as pd
# import pickle

# app = Flask(__name__)

# model = pickle.load(open("model/car_price_model.pkl", "rb"))
# columns = pickle.load(open("model/columns.pkl", "rb"))

# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/predict", methods=["POST"])
# def predict():

#     present_price = float(request.form["present_price"])
#     kms_driven = int(request.form["kms_driven"])
#     year = int(request.form["year"])
#     owner = int(request.form["owner"])

#     fuel = request.form["fuel"]
#     seller = request.form["seller"]
#     transmission = request.form["transmission"]

#     car_age = 2024 - year

#     data = {
#         "kms_driven": kms_driven,
#         "owner": owner,
#         "car_age": car_age
#     }

#     if fuel == "Diesel":
#         data["fuel_type_Diesel"] = 1

#     if fuel == "Petrol":
#         data["fuel_type_Petrol"] = 1

#     if seller == "Individual":
#         data["seller_type_Individual"] = 1

#     if transmission == "Manual":
#         data["transmission_Manual"] = 1

#     df = pd.DataFrame([data])

#     df = df.reindex(columns=columns, fill_value=0)

#     prediction = model.predict(df)

#     output = round(prediction[0], 2)

#     return render_template(
#         "index.html",
#         prediction_text=f"Estimated Price: ₹{output} Lakhs"
#     )


# if __name__ == "__main__":
#     app.run(debug=True)






 