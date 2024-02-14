import pandas as pd
import streamlit as st
import pickle
import webbrowser
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
model = pickle.load(open('los1.pkl','rb'))
def predict_length_of_stay(input_df):
    prediction = model.predict(input_df)
    return prediction

def main():
    st.title('Hospital Length of Stay Prediction')
    input_data = {}
    st.markdown("<h3 style='text-align: left;'>Patient Information:</h3>", unsafe_allow_html=True)
    colu3, colu4 = st.columns(2)
    with colu3:
        Age= st.number_input('**Enter Patient Age**',min_value=0, max_value=100)
    with colu4:
        st.selectbox('**Severity of Illness**',('Extreme','Moderate','Minor'),index=None,placeholder="Choose the severity of Illness",)
    colu1, colu2 = st.columns(2)
    with colu1:
        #input_data['misc']= st.sidebar.number_input('misc',min_value=0, max_value=120)
        st.markdown("<h3 style='text-align: center;'>Clinical Information:</h3>", unsafe_allow_html=True)
        input_data['num_callouts']= st.number_input('**Number of callouts**')
        if(input_data['num_callouts']==0.00):
            input_data['num_callouts']=0
        input_data['num_diagnosis']= st.number_input('**Number of diagnosis**')
        if(input_data['num_diagnosis']==0.00):
            input_data['num_diagnosis']=0
        input_data['num_procs'] = st.number_input('**Number of procedures**')
        if(input_data['num_procs']==0.00):
            input_data['num_procs']=0
        input_data['num_input'] = st.number_input('**Number of inputs**')
        if(input_data['num_input']==0.00):
            input_data['num_input']=0
        input_data['num_rx'] = st.number_input('**Number of prescriptions**')
        if(input_data['num_rx']==0.00):
            input_data['num_rx']=0
        input_data['num_transfers'] = st.number_input('**Number of transfers**')
        if(input_data['num_transfers']==0.00):
            input_data['num_transfers']=0
    with colu2:
        st.markdown("<h3 style='text-align: center;'>Comorbidity Information:</h3>", unsafe_allow_html=True)
        input_data['injury'] = st.number_input('**Injury**',min_value=0, max_value=120)
        input_data['blood'] = st.number_input('**Blood**',min_value=0, max_value=120)
        input_data['digestive'] = st.number_input('**Digestive**',min_value=0, max_value=120)
        input_data['genitourinary'] = st.number_input('**Genitourinary**',min_value=0, max_value=120)
        input_data['skin'] = st.number_input('**Skin**',min_value=0, max_value=120)
        input_data['respiratory'] = st.number_input('**Respiratory**',min_value=0, max_value=120)
        input_data['infectious'] = st.number_input('**Infectious**',min_value=0, max_value=120)
    input_df = pd.DataFrame([input_data])
    colu1, colu2, colu3 = st.columns(3)
    with colu1:
        st.write('')
    with colu2:
        c=st.button('**Predict Length of Stay**')
    if c:
        #features = np.array([[num_callouts,num_diagnosis,num_procs,num_input,num_rx,num_transfers,injury,blood,digestive,genitourinary,skin,respiratory,infectious]])  # Add more features as required
        prediction=predict_length_of_stay(input_df)[0]
        prediction=round(prediction)
        st.markdown("<h2 style='text-align: center;'>Predicted Length of Stay: <b>{}</b> days</h3>".format(prediction), unsafe_allow_html=True)
        st.write(input_df)
        
if __name__ == '__main__':
    main()


