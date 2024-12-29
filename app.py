# importing the necessary libraries
import pickle
import numpy as np
import streamlit as st

# load the saved model to a file
with open('Gold_Price_Pred_Model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
    
def gold_price_pred(input_data):
    '''Predict the price of gold'''
    
    # convert data into numpy array
    input_data_as_numpy_array = np.array(input_data)

    # reshape the numpy array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction

def main():
    st.title("Gold Price Prediction")
    
    # getting the input data from the user
    SPX = st.number_input("Enter the SPX value: ")
    USO = st.number_input("Enter the USO value: ")
    SLV = st.number_input("Enter the SLV value: ")
    EUR_USD = st.number_input("Enter the EUR/USD value: ")
    
    if st.button("Predict Gold Price"):
        input_data = [SPX, USO, SLV, EUR_USD]
        prediction = gold_price_pred(input_data)
        st.success(f"The predicted gold price is {prediction[0]}")
        
if __name__ == "__main__":
    main()
    