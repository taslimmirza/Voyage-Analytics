import streamlit as st
import joblib
import pandas as pd

# Load the model and encoders
svd_model = joblib.load('models/hotel_recommendation_model.pkl')
user_encoder = joblib.load('encoders_scalers/user_encoder.pkl')

st.title('Travel Recommendation System')

user_code = st.text_input('Enter your User Code:', '')

if st.button('Recommend Hotels'):
    if user_code:
        # user_code directly used after encoding
        encoded_user = user_encoder.transform([user_code])[0]
        # Generate recommendations
        predictions = svd_model.predict(encoded_user)
        top_recommendations = pd.DataFrame(predictions, columns=['Hotel', 'Score']).nlargest(5, 'Score')
        st.write(top_recommendations)
    else:
        st.write("Please enter a valid user code.")
