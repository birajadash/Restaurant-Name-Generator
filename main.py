import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American", "Korean", "Chinese", "Japanese", "Thai", "Vietnamese", "French", "Spanish", "Greek", "Turkish", "Lebanese", "Mediterranean", "German", "British", "African", "Caribbean", "Brazilian", "Portuguese", "Russian", "Australian", "Canadian", "Scandinavian", "Irish", "Dutch", "Belgian", "Swiss", "Austrian", "Czech", "Polish", "Hungarian", "Romanian", "Bulgarian", "Ukrainian", "Georgian", "Armenian", "Azerbaijani", "Kazakh", "Uzbek", "Turkmen", "Kyrgyz", "Tajik", "Afghan", "Pakistani", "Bangladeshi", "Nepalese", "Sri Lankan", "Bhutanese", "Maldivian", "Tibetan", "Mongolian", "North Korean", "South Korean", "Filipino", "Indonesian", "Malaysian", "Singaporean", "Thai", "Vietnamese", "Laotian", "Cambodian", "Burmese", "Bruneian", "Timorese", "Papua New Guinean", "Solomon Islander", "Vanuatuan", "Fijian", "Tongan", "Samoan", "Tuvaluan", "Kiribati", "Marshallese", "Palauan", "Micronesian", "Nauruan", "Marshall Islander", "Kosraean", "Pohnpeian", "Chuukese", "Yapese", "Belauan", "Saipanese", "Guamanian", "Marshallese", "Mariana Islander", "Carolinian", "Kosraean", "Pohnpeian", "Chuukese", "Yapese", "Belauan", "Saipanese", "Guamanian", "Marshallese", "Mariana Islander", "Carolinian", "Kosraean", "Pohnpeian", "Chuukese", "Yapese", "Belauan", "Saipanese", "Guamanian", "Marshallese", "Mariana Islander"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)

