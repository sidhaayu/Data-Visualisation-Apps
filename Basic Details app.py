import streamlit as st

st.title('Basic Widgets App')
st.write('This app shows the basic widgets of streamlit!!!')



# --- NAME INPUT ---
name = st.text_input('Enter your name:')

if st.button('Submit Name'):
    st.write(f'Welcome to streamlit {name}')
else:
    st.write("Name Please?")




# --- AGE SLIDER ---
age = st.slider("Select your age:", 1, 100, 20)

if st.button('Check Age'):
    if age > 18:
        st.write("You are an adult")
    else:
        st.write("You are not an adult")
else:
    st.write("Age please?")



# --- FAVORITE COLOR ---
fav_color = st.selectbox("Select fav color:", ['red', 'blue', 'pink', 'black'])



# --- TERMS CHECKBOX ---
agree_terms = st.checkbox("I agree to the terms")



# --- FINAL SUBMIT ---
if st.button('Submit All'):
    if agree_terms:
        st.success(
            f'Hello {name}, welcome to streamlit. '
            f'You are {age} years old and your fav color is {fav_color}'
        )
    else:
        st.warning("Please agree to the terms and conditions")
