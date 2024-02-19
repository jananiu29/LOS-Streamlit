import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.preprocessing import StandardScaler
import streamlit as st
# from lightgbm import LGBMRegressor
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.linear_model import PoissonRegressor
import pickle
# import webbrowser
# import joblib

#background_image_url = "C:\\Users\\janani.u.lv\\Downloads\\hos_bg.jpg"
#background_image_url = "https://urocoach.com//wp-content//uploads//2019//04//iStock-596098068.jpg"
#background_image_url = "https://st4.depositphotos.com//1008011//25427//i//450//depositphotos_254274782-stock-photo-medical-cosmetology-clinic-theme-blur.jpg"
#background_image_url ="https://encrypted-tbn0.gstatic.com//images?q=tbn:ANd9GcSwfl_XRPvKRKnFO0AXleh2jhYGjG8f9_xRNA&usqp=CAU"
background_image_url = "https://st2.depositphotos.com//2065849//8219//i//450//depositphotos_82195114-stock-photo-iv-drip-on-the-background.jpg"
background_style = f"""
    <style>
        .stApp {{
            background-image: url("{background_image_url}");
            background-size: contain;
        }}
    </style>
"""
st.markdown(background_style, unsafe_allow_html=True)
with open("los_lg.pkl", 'rb') as file:
     model = pickle.load(file)
def predict_length_of_stay(input_df):
    #y_test_preds=pr.predict(X_test_normalized)
    prediction = model.predict(input_df)
    return prediction

def main():
    df= pd.read_csv("dataset_ui.csv", sep=',')
    df=pd.DataFrame(df)
    st.title('Hospital Length of Stay Prediction')
    st.markdown("<h3 style='text-align: left;'>Patient Information:</h3>", unsafe_allow_html=True)
    id=st.number_input('**Enter Patient ID**',min_value=0, max_value=100000)
    input_data = {}
    colu3, colu4 = st.columns(2)
    with colu3:
        Age= st.number_input('**Enter Patient Age**',min_value=0, max_value=100)
    with colu4:
        st.selectbox('**Severity of Illness**',('Extreme','Moderate','Minor'),index=None,placeholder="Choose the severity of Illness",)
    st.markdown("<h3 style='text-align: center;'>Comorbidity Information:</h3>", unsafe_allow_html=True)
    colu1, colu2 = st.columns(2)
    with colu1:
        input_data['injury'] = st.number_input('**Injury**',min_value=0, max_value=120)
        input_data['blood'] = st.number_input('**Blood**',min_value=0, max_value=120)
        input_data['digestive'] = st.number_input('**Digestive**',min_value=0, max_value=120)
    input_data['genitourinary'] = st.number_input('**Genitourinary**',min_value=0, max_value=120)
    with colu2:
        input_data['skin'] = st.number_input('**Skin**',min_value=0, max_value=120)
        input_data['respiratory'] = st.number_input('**Respiratory**',min_value=0, max_value=120)
        input_data['infectious'] = st.number_input('**Infectious**',min_value=0, max_value=120)
        #colu1, colu2, colu3 = st.columns(3)
    c=st.button('**Predict Length of Stay**')
    if c:
        index = df[df['subject_id'] == id]
        blankIndex=[''] * len(index)
        index.index=blankIndex
            #input_data['misc']= st.sidebar.number_input('misc',min_value=0, max_value=120)
        st.markdown("<h3 style='text-align: center;'>Clinical Information:</h3>", unsafe_allow_html=True)
        colu5, colu6 = st.columns(2)
        input_data['num_callouts']=index['num_callouts'][0]
        input_data['num_diagnosis']=index['num_diagnosis'][0]
        input_data['num_procs']=index['num_procs'][0]
        input_data['num_input']=index['num_input'][0]
        input_data['num_rx']=index['num_rx'][0]
        input_data['num_transfers']=index['num_transfers'][0]
        with colu5:
            st.write("**Number of Callouts:**")
            st.write("<span style='font-size: 20px; font-weight: bold;'>", input_data['num_callouts'], "</span>", unsafe_allow_html=True)
            st.write("**Number of Diagnosis:**")
            st.write("<span style='font-size: 20px; font-weight: bold;'>", input_data['num_diagnosis'], "</span>", unsafe_allow_html=True)
            st.write("**Number of Procedures:**")
            st.write("<span style='font-size: 20px; font-weight: bold;'>", input_data['num_procs'], "</span>", unsafe_allow_html=True)
        with colu6:
            st.write("**Number of Inputs:**")
            st.write("<span style='font-size: 20px; font-weight: bold;'>", input_data['num_input'], "</span>", unsafe_allow_html=True)
            st.write("**Number of Prescriptions:**")
            st.write("<span style='font-size: 20px; font-weight: bold;'>", input_data['num_rx'], "</span>", unsafe_allow_html=True)
            st.write("**Number of Transfers:**")
            st.write("<span style='font-size: 20px; font-weight: bold;'>", input_data['num_transfers'], "</span>", unsafe_allow_html=True)

# # Define the data to be displayed
#         data = {
#             "Clinical Events":"",
#     "Number of Callouts": index['num_callouts'][0],
#     "Number of Diagnosis": index['num_diagnosis'][0],
#     "Number of Procedures": index['num_procs'][0],
#     "Number of Inputs": index['num_input'][0],
#     "Number of Prescriptions": index['num_rx'][0],
#     "Number of Transfers": index['num_transfers'][0]
#     }

# # Display data in a table format
#         st.table(data)

# If you want to display headers in bold, you can use markdown in the keys
        input_df = pd.DataFrame([input_data])
        prediction=predict_length_of_stay(input_df)[0]
        prediction=round(prediction)
        st.markdown("<h2 style='text-align: center;'>Predicted Length of Stay: <b>{}</b> days</h3>".format(prediction), unsafe_allow_html=True)
        
if __name__ == '__main__':
    main()


