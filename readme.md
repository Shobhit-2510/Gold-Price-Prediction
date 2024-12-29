# Gold Price Prediction Using Random Forest Regressor

This project predicts gold prices using a Random Forest Regressor model. It leverages historical data and machine learning techniques to provide accurate predictions. The project is deployed as a web application using **Streamlit** and hosted on **Streamlit Cloud**.

---

## Features
- **User-Friendly Interface**: Enter relevant input features via an interactive UI to get predictions.
- **Model Explanation**: The model is built using a Random Forest Regressor, providing robust performance for regression tasks.
- **Deployment**: Accessible online through Streamlit for ease of use.

---

## Project Structure

```
Gold_Price_Prediction/
├── app.py                        # Streamlit app source code
├── Gold_Price_Pred_Model.pkl     # Trained model file
├── requirements.txt              # Python dependencies
└── Gold_Price_Prediction_Random_Forest_Regressor_.ipynb # Jupyter Notebook
```

---

## Installation and Setup

### Prerequisites
- Python 3.8 or later
- Streamlit installed
- Basic knowledge of Python and Git

### Clone the Repository
```bash
git clone https://github.com/Shobhit-2510/gold-price-prediction.git
cd gold-price-prediction
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Locally
To run the application locally, execute:
```bash
streamlit run app.py
```
Open the provided localhost URL in your browser.

---

## Deployment
The application is deployed on Streamlit Cloud. You can access it here:

[Gold Price Prediction App](https://gold-price-prediction.streamlit.app/)

---

## How It Works
1. The user provides input features through the Streamlit app.
2. The trained Random Forest Regressor model processes the inputs.
3. The model predicts the price of gold based on the provided features.

---

## Technologies Used
- **Python**: For data preprocessing, model building, and deployment.
- **Pandas, NumPy**: Data manipulation and analysis.
- **Scikit-learn**: Machine learning model development.
- **Streamlit**: Web application framework.

---

## Contribution
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add a new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- **Streamlit** for providing an excellent deployment platform.
- **Scikit-learn** for the robust machine learning library.
- Special thanks to the contributors and users who inspire continuous improvement.
