import streamlit as st
import pandas as pd
import joblib

st.title("Cross-sell Prediction")

st.markdown("""
               This app predicts whether the policyholders (customers) from the past year of an insurance company that provided health insurance are likely to be interested in vehicle insurance offered by the same company.
        """)

st.sidebar.header("Input policy holder Information")

df = pd.read_csv('train.csv')

gender = st.sidebar.selectbox("Gender",pd.unique(df['Gender']))
Age = st.sidebar.number_input("Age" , min_value = 20 ,max_value=90 ,step =1)
driving_license = st.sidebar.selectbox("Driving_License",["Yes","No"])
if driving_license == 'Yes':
        driving_license = 1
else:
        driving_license = 0
Region_code = st.sidebar.number_input("Region_Code" , min_value = 0.0 , max_value = 55.0 , step = 1.0)
previously_insures = st.sidebar.selectbox("Previously_Insured",["Yes","No"])
if previously_insures == 'Yes':
        previously_insures = 1
else: 
        previously_insures = 0
Vehicle_Age = st.sidebar.selectbox("Vehicle_Age",pd.unique(df['Vehicle_Age']))
Vehicle_damage = st.sidebar.selectbox("Vehicle_Damage",pd.unique(df['Vehicle_Damage']))
annual_premium = st.sidebar.number_input("annual_premium")
policy_sales_channel = st.sidebar.number_input("Policy_Sales_Channel")
vintage = st.sidebar.number_input("vintage")

inputs={
        "Gender":gender,
        'Age' : Age,
        'Driving_License' : driving_license,
        'Region_Code' : Region_code,
        'Previously_Insured' : previously_insures ,
        'Vehicle_Age' : Vehicle_Age,
        'Vehicle_Damage' : Vehicle_damage ,
        'Annual_Premium' : float(annual_premium) ,
        'Policy_Sales_Channel' : float(policy_sales_channel) ,
        'Vintage' : vintage
}

if st.sidebar.button("Predict cross-sell"):
        try:
                model=joblib.load('cross-sell-prediction.pkl')
                x_input = pd.DataFrame(inputs, index =[0])
                prediction = model.predict(x_input)

                st.write("### Prediction Result")
                if prediction == 1:
                        # Custom green success message
                        st.markdown(
                                "<h3 style='color: green;'>The Policy holder is interested in Vehicle Insurance.</h3>",
                                unsafe_allow_html=True
                        )
                else:
                        # Custom red message
                        st.markdown(
                                "<h3 style='color: red;'>The Policy holder is not interested in Vehicle Insurance.</h3>",
                                unsafe_allow_html=True
                        )
        except Exception as e:
                st.error(f"Error in prediction:{e}")