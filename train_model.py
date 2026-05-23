import pandas as pd
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

print("Loading datasets...")

folder = "archive"
dfs = []

for file in os.listdir(folder):

    if file.endswith(".csv"):

        path = os.path.join(folder, file)
        df = pd.read_csv(path)

        print("Processing:", file)

        df.columns = df.columns.str.lower().str.strip()

        rename_map = {
            "sellingprice": "selling_price",
            "price": "selling_price",
            "selling_price": "selling_price",
            "km_driven": "kms_driven",
            "kms_driven": "kms_driven",
            "fuel": "fuel_type",
            "fuel_type": "fuel_type",
            "seller_type": "seller_type",
            "transmission": "transmission",
            "owner": "owner",
            "year": "year"
        }

        df = df.rename(columns=rename_map)

        needed = [
            "year",
            "selling_price",
            "kms_driven",
            "fuel_type",
            "seller_type",
            "transmission",
            "owner"
        ]

        cols = [c for c in needed if c in df.columns]

        df = df[cols]

        dfs.append(df)

df = pd.concat(dfs, ignore_index=True)

print("Combined shape:", df.shape)

df.dropna(inplace=True)

print("After cleaning:", df.shape)

# 🔹 Convert prices to LAKHS if dataset used rupees
df["selling_price"] = df["selling_price"].apply(
    lambda x: x/100000 if x > 1000 else x
)

# Feature engineering
df["car_age"] = 2024 - df["year"]

df.drop("year", axis=1, inplace=True)

# One-hot encoding
df = pd.get_dummies(df, drop_first=True)

X = df.drop("selling_price", axis=1)
y = df["selling_price"]

print("Total training rows:", len(X))

# Save feature columns
os.makedirs("model", exist_ok=True)
pickle.dump(X.columns, open("model/columns.pkl", "wb"))

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model/car_price_model.pkl", "wb"))

print("Model trained successfully!")





# ... your current code up to training the model
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model/car_price_model.pkl", "wb"))
print("Model trained successfully!")

# ===================== NEW PART: TRAIN & TEST ACCURACY =====================
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Predict on train and test
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Compute R² score
train_acc = r2_score(y_train, y_train_pred)
test_acc = r2_score(y_test, y_test_pred)

print(f"Train Accuracy (R²): {train_acc:.4f}")
print(f"Test Accuracy (R²): {test_acc:.4f}")

# Plot simple bar chart
plt.figure(figsize=(6,4))
plt.bar(["Train Accuracy", "Test Accuracy"], [train_acc, test_acc], color=["#801010", "#b43737"])
plt.ylim(0, 1)
plt.title("Random Forest Regressor Accuracy")
plt.ylabel("R² Score")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()






























#styles.css
# /* ===================== BODY & BACKGROUND ===================== */
# body {
#   font-family: 'Poppins', sans-serif;
#   margin: 0;
#   padding: 0;
#   overflow-x: hidden;
#   display: flex;
#   justify-content: center;
#   align-items: center;
#   min-height: 100vh;
#   background: linear-gradient(135deg, #4a4850, #dadae2, #5a5f68);
#   perspective: 1200px;
#   position: relative;
# }



# @keyframes drive {
#   0% { transform: translateX(0) rotateY(0deg); }
#   50% { transform: translateX(120vw) rotateY(10deg); }
#   100% { transform: translateX(0) rotateY(0deg); }
# }

# /* ===================== CONTAINER & HEADER ===================== */
# .container {
#   text-align: center;
#   width: 95%;
#   max-width: 750px;
#   z-index: 2;
#   animation: fadeIn 1s ease-in-out;
# }

# h1 {
#   font-size: 44px;
#   margin-bottom: 5px;
#   text-shadow: 2px 2px 14px rgba(0,0,0,0.6);
# }

# .subtitle {
#   opacity: 0.85;
#   margin-bottom: 35px;
#   font-weight: 300;
#   font-size: 18px;
# }

# /* ===================== CARD ===================== */
# .card {
#   background: rgba(199, 182, 182, 0.95);
#   color: #1f2125;
#   padding: 40px;
#   border-radius: 25px;
#   box-shadow: 0 25px 50px rgba(0,0,0,0.4);
#   transition: transform 0.4s ease, box-shadow 0.4s ease;
# }

# .card:hover {
#   transform: rotateY(5deg) rotateX(2deg) translateY(-6px);
#   box-shadow: 0 35px 70px rgba(0,0,0,0.5);
# }

# /* ===================== FORM GRID ===================== */
# .form-grid {
#   display: grid;
#   grid-template-columns: 1fr 1fr;
#   gap: 25px;
# }

# /* ===================== INPUTS & ICONS ===================== */
# .input-group {
#   position: relative;
#   display: flex;
#   flex-direction: column;
#   text-align: left;
# }

# .input-group label {
#   margin-bottom: 5px;
#   font-weight: 500;
# }

# .neon-icon {
#   position: absolute;
#   top: 50%;
#   left: 12px;
#   transform: translateY(-50%);
#   font-size: 18px;
#   color: #a10c0c;
#   text-shadow: 0 0 6px #f5f0f0, 0 0 12px #e4dede;
#   pointer-events: none;
#   transition: transform 0.3s, text-shadow 0.3s;
# }

# .input-group input,
# .input-group select {
#   padding: 12px 12px 12px 40px;
#   border-radius: 12px;
#   border: 1px solid #533f3f;
#   font-size: 15px;
#   outline: none;
#   transition: 0.3s, box-shadow 0.3s;
# }

# .input-group input:focus,
# .input-group select:focus {
#   border-color: #911b21;
#   box-shadow: 0 0 12px #9b4e4e;
# }

# .input-group:hover .neon-icon {
#   transform: translateY(-50%) translateX(-2px) scale(1.3);
#   text-shadow: 0 0 12px #d4d1d1, 0 0 25px #9b3e4a;
# }

# /* ===================== BUTTON ===================== */
# .predict-btn {
#   margin-top: 25px;
#   width: 100%;
#   padding: 15px;
#   border: none;
#   border-radius: 20px;
#   background: linear-gradient(45deg, #bd2c33, #af3e3e);
#   color: white;
#   font-size: 17px;
#   font-weight: 600;
#   cursor: pointer;
#   transition: all 0.3s ease;
#   box-shadow: 0 12px 30px rgba(202, 38, 60, 0.5);
# }

# .predict-btn:hover {
#   transform: scale(1.08) translateY(-4px);
#   box-shadow: 0 25px 60px rgba(221, 89, 89, 0.6);
# }

# /* ===================== RESULT CARD ===================== */
# .result-card {
#   margin-top: 30px;
#   background: linear-gradient(145deg, #ffffff, #f0f0f0);
#   color: #222;
#   padding: 30px;
#   border-radius: 25px;
#   box-shadow: 0 25px 60px rgba(0,0,0,0.35);
#   animation: slideDown 0.5s ease forwards;
# }

# .result-card h2 {
#   margin: 0;
#   color: #444;
#   text-shadow: 1px 1px 5px rgba(0,0,0,0.2);
# }

# .result-card p {
#   font-size: 28px;
#   font-weight: bold;
#   color: #b43737;
#   margin-top: 12px;
#   text-shadow: 1px 1px 8px rgba(0,0,0,0.2);
# }

# /* ===================== ANIMATIONS ===================== */
# @keyframes fadeIn {
#   0% {opacity:0; transform: translateY(-20px);}
#   100% {opacity:1; transform: translateY(0);}
# }

# @keyframes slideDown {
#   0% {opacity:0; transform: translateY(-30px);}
#   100% {opacity:1; transform: translateY(0);}
# }
