import streamlit as st
import sqlite3

def main():
    connect = sqlite3.connect('Liquor_Database.db')
    cursor = connect.cursor()
    cursor.execute('select * from DrinkRecipe')
    result = cursor.fetchall()
    st.write(result)

    st.markdown("<h2 style='text-align: center; color: white;'>Liquor Recipe Ingredient Search System</h2>", unsafe_allow_html=True)

    # Create a two-column layout
    col1, col2 = st.columns(2)

    # Create the first selectbox for selecting ingredient types(major)
    with col1:
        type_selection = st.selectbox("Select Type", ["Select Type", "Liquor", "Mixer", "Garnish", "Glass"])

    # Create the second box for selecting specific types(minor) based on the first selection
    with col2:
        if type_selection == "Liquor":

            # Run the SQL query to get all unique spirit values
            query = "SELECT DISTINCT sprt_name FROM Spirit;"
            cursor.execute(query)
            liquor_items = cursor.fetchall()

            # Create a Streamlit selectbox and populate it with options
            selected_spirit = st.selectbox("Select Liquor:", [str(liquor[0]) for liquor in liquor_items], index=None)
            if not None:
                st.write(f"Selected Liquor: {selected_spirit}")

        elif type_selection == "Mixer":
            query = "SELECT DISTINCT mix_name FROM Mixer;"
            cursor.execute(query)
            mixer_items = cursor.fetchall()

            selected_mixer = st.selectbox("Select Mixer:", [str(mixer[0]) for mixer in mixer_items], index=None)
            if not None:
                st.write(f"Selected Mixer: {selected_mixer}")

        elif type_selection == "Garnish":
            query = "SELECT DISTINCT Garnish_name FROM Garnish;"
            cursor.execute(query)
            garnish_items = cursor.fetchall()

            selected_garnish = st.selectbox("Select Garnish:", [str(garnish[0]) for garnish in garnish_items], index=None)
            if not None:
                st.write(f"Selected Garnish: {selected_garnish}")

        elif type_selection == "Glass":
            query = "SELECT DISTINCT glass_name FROM GlassType;"
            cursor.execute(query)
            glass_items = cursor.fetchall()

            selected_glass = st.selectbox("Select Glass:", [str(glass[0]) for glass in glass_items], index=None)
            if not None:
                st.write(f"Selected Glass: {selected_glass}")
        else:
            pass

    connect.close()

if __name__ == "__main__":
    main()
