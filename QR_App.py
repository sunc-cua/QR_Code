# libraries
import streamlit as st
import qr_maker

st.title('Create Your Own QR Code')

# (1) Type in your hyperlink for your QR code
hyper_link  = st.text_input("Type in your hyperline for QR code such as:", "https://engineering.catholic.edu/eecs/index.html")
st.write("Test your link first:", hyper_link)

# (2) User input: QR Code Size (inches)
# qr_size = st.number_input("Your QR Code Size:" )
qr_size = st.slider('Slide me', min_value=6, max_value=12)
st.write("Your code size is", qr_size)


# test
qr_maker.qr_code(hyper_link, qr_size)
st.image("QR_logo.png", caption='Your QR-logo')