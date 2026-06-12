# now let's start the first day with first some id;

# Import the module name streamlit 
import streamlit as st

# now set the first titlclse as header it's also called they have one funciton name " title()"
st.title("This is the porject of Shivdeep Mishra")
# now move to the next one it's called the subheader
st.subheader("Being a part of the streamlit with gradio!")
# now move to the  next one it's called the text () which is stand for the text that user can see this;;
st.text("Welcome all of you This your contribution { with out you it's can't work}")




# now here we are going to defin the strips okay.
st.write(" choose your Favorite Phone!")
first_with = st.selectbox(" your favorite Andriod :", ["Vivo" , "Mi ", "Redmi","sumsung", "Motrola", "NOkia "])
# now call  that variable 
st.write(f"You Choose {first_with}, And very cromatic with did!")
