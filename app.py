# Mengimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Menulis judul
st.markdown("<h1 style='text-align: center; '> Real Estate Price Prediction </h1>", unsafe_allow_html=True)
st.markdown('---'*10)


# Fungsi untuk prediksi
def final_prediction(values, model):
    global prediction
    prediction = model.predict(values)
    return prediction

# Ini merupakan fungsi utama
def main():
    
    # Nilai awal
    Age = 32.0
    Distance_MRT = 84.87882
    Total_Sotres = 10
    Latitude = 24.98298
    longitude = 121.54024
    
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            Age = st.number_input('Age', value=Age)
        with col2:
            Distance_MRT = st.number_input('Distance_MRT', value=Distance_MRT)
        with col3:
           Total_Sotres = st.number_input('Total_Sotres', value=Total_Sotres)
            
    st.markdown('---'*10)
    
    with st.container():
        col4, col5 = st.columns(2)
        with col4:
           Latitude = st.number_input('Latitude', value=Latitude)
        with col5:
           longitude = st.number_input('longitude', value=longitude)

        
    data = {
        'Age': Age,
        'Distance_MRT': Distance_MRT,
        'Total_Sotres': Total_Sotres,
        'Latitude': Latitude,
        'longitude': longitude,
        }
    
    kolom = list(data.keys())
    
    df_final = pd.DataFrame([data.values()],columns=kolom)
    
    # load model
    my_model = pickle.load(open('model_regresi_realestate.pkl', 'rb'))
    
    # Predict
    result = round(float(final_prediction(df_final, my_model)),2)
    
    st.markdown('---'*10)
    
    st.write('<center><b><h3>Predicted Price= ', result,'</b></h3>', unsafe_allow_html=True)
           
if __name__ == '__main__':
	main() 

