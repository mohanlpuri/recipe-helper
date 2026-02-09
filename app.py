import streamlit as st
import langChainRecipeHelper as langChainRecipeHelper

st.title("Best Dish & Recipe Finder")

place = st.selectbox(
    "Pick a place",
    ["Rome", "London", "Paris", "New Delhi"]
)

if st.button("Generate"):
    with st.spinner("Thinking..."):
        result = langChainRecipeHelper.combined_chain.invoke({"place": place})

    # result is a dict: {"place":..., "dish":..., "recipe":...}
    st.subheader("Best Dish")
    st.write(result["dish"])

    st.subheader("Recipe")
    st.write(result["recipe"])





