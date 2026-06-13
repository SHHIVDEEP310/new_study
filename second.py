import streamlit as st
from datetime import date

st.title("Boss with Dabin")

#1.
# now radio use for the putting the multiple check option 
option = st.radio("Q: Choose your meta character with your way?",["@","#","$","%","^","&","*"])
# now put the check  box

# 2.
anti_ragging = st.checkbox("I agree with all term and condition that company have(Dabin Cyber_atterker), I read the all pagess with all siutble condition.")

# if anti_ragging:
#     st.success("Finally! you have entered into the next step.")

# 3.
#this just selectbox 
st.write("Now Let's start the new page.")
network_log = st.selectbox("Q: Choose your network action?",["TCP","UDP","HTTP","HTTPS","Custom TCP","portwithband"])

# 4. 
# now add the new question with new idea
slied = st.slider("Q: Choose your Bandwith?", min_value=10, max_value=60, step=5,value=20)

#5.
# take the input as number value
take_input = st.number_input("Q: Enter The integer value of, how many people are connect with your wifi?", min_value=0,max_value=12,value=1)
take_text = st.text_input("Q: Enter your First name?")
take_text1 = st.text_input("Q: Enter your Last name?")
take_dob = st.date_input("Q: Enter your dob but original?",min_value=date(2000,1,1),max_value=date(2030,1,1),value=date.today(),format="DD/MM/YYYY")
    

if st.button("This is your All:"): # and button is use for making the any button like search barlike
    st.success(f"Your choosen {option}\n, {anti_ragging}\n, {network_log}\n ,{slied}\n,{take_input}, {take_text} {take_text1} , {take_dob} is really greatfull! ")
    