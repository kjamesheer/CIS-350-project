import streamlit as st

def main():
    st.markdown("<h2 style='text-align: center; color: white;'>Liquor Recipe Ingredient Search System</h2>", unsafe_allow_html=True)

    # Create a two-column layout
    col1, col2 = st.columns(2)

    # Create the first selectbox for selecting ingredient types(major)
    with col1:
        type_selection = st.selectbox("Select Type", ["Select Type", "Liquor", "Mixer", "Garnish", "Glass"])

    # Create the second box for selecting specific types(minor) based on the first selection
    with col2:
        if type_selection == "Liquor":
            liquor_selection = st.selectbox("Select Liquor", ["Select Liquor", "Vodka", "Gin", "Rum", "Whiskey"])
        elif type_selection == "Mixer":
            mixer_selection = st.selectbox("Select Mixer", ["Select Mixer", "Pop", "Juice", "Syrup", "Ginger Ale"])
        elif type_selection == "Garnish":
            garnish_selection = st.selectbox("Select Garnish", ["Select Garnish", "Cinnamon", "Salt rim", "Fruit", "Citrus"])
        elif type_selection == "Glass":
            glass_selection = st.selectbox("Select Glass", ["Select Glass", "Wine", "Collins", "Highball", "Martini"])
        else:
            pass

if __name__ == "__main__":
    main()
