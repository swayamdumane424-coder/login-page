import streamlit as st
st.title("Upload image App")
image= st.file_uploader(
    " image uploder",
    type=["png","jpg","jpeg"],width=300)
if image  :
    st.success("image successfully uploded",width=300)
    st.image(image,width=500)
