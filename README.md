# 🚗 AI Car Price Predictor

A Flask web application that predicts used car prices based on key vehicle details such as original price, kilometers driven, year, owner type, fuel type, seller type, and transmission.

## Features

- User-friendly web form for entering car details.
- Predicts car price instantly after form submission.
- Clean and responsive UI.
- LocalStorage support to remember form inputs in the browser.
- Flask-based backend for easy integration with an ML model.

## Project Structure

```bash
project-folder/
├── app.py
├── templates/
│   ├── index.html
│   └── prediction.html
├── static/
│   └── style.css
└── README.md
```

## Requirements

- Python 3.8+
- Flask

Install dependencies:

```bash
pip install flask
```

## How to Run

1. Clone the repository:

```bash
cd ai-car-price-predictor
```

2. Run the Flask app:

```bash
python app.py
```

3. Open your browser and go to:

```bash
http://127.0.0.1:5000
```

## Usage

1. Enter the car details in the form.
2. Click **Predict Price**.
3. View the predicted car price on the result page.

## Notes

- The current prediction logic is a dummy example.
- Replace the dummy formula in `app.py` with your trained machine learning model for real predictions.

## Example Input Fields

- Original Price
- Kilometers Driven
- Year of Purchase
- Owner
- Fuel Type
- Seller Type
- Transmission

## Future Improvements

- Integrate a trained regression model.
- Add validation and error handling.
- Support more car attributes like brand, model, and location.
- Improve prediction accuracy with better preprocessing.

## License

This project is open source and available under the MIT License.