import streamlit as st
import sqlite3
import pandas as pd

def main():
    connect = sqlite3.connect('Liquor_Database.db')
    cursor = connect.cursor()

    st.markdown("<h2 style='text-align: center; color: white;'>Liquor Recipe Ingredient Search System</h2>", unsafe_allow_html=True)

    # Create a two-column layout
    col1, col2 = st.columns(2)

    # Create the first selectbox for selecting ingredient types(major)
    with col1:
        type_selection = st.selectbox("Select Type", ["Select Type", "Liquor", "Mixer", "Garnish", "Glass"])

    # Create the second box for selecting specific types(minor) based on the first selection
    with col2:
        if type_selection == "Liquor":
            st.write("Liquor Table Data")

            query = "SELECT * FROM Spirit;"
            df = pd.read_sql_query(query, connect)

            # Display the dataframe in Streamlit
            st.dataframe(df)

            # Run the SQL query to get all unique spirit values
            query2 = "SELECT DISTINCT sprt_name FROM Spirit;"
            cursor.execute(query2)
            liquor_items = cursor.fetchall()

            # Create a Streamlit selectbox and populate it with options
            selected_spirit = st.selectbox("Select Liquor:", [str(liquor[0]) for liquor in liquor_items], index=None)

            query3 = "SELECT DISTINCT sprt_id FROM Spirit;"
            cursor.execute(query3)
            sprt_ids = cursor.fetchall()

            for liquor in sprt_ids:
                st.write(liquor[0])

        elif type_selection == "Mixer":
            st.write("Mixer Table Data")
            query = "SELECT * FROM Mixer;"
            df = pd.read_sql_query(query, connect)
            st.dataframe(df)

            query2 = "SELECT DISTINCT mix_name FROM Mixer;"
            cursor.execute(query2)
            mixer_items = cursor.fetchall()

            selected_mixer = st.selectbox("Select Mixer:", [str(mixer[0]) for mixer in mixer_items], index=None)

        elif type_selection == "Garnish":
            st.write("Garnish Table Data")
            query = "SELECT * FROM Garnish;"
            df = pd.read_sql_query(query, connect)
            st.dataframe(df)

            query2 = "SELECT DISTINCT Garnish_name FROM Garnish;"
            cursor.execute(query2)
            garnish_items = cursor.fetchall()

            selected_garnish = st.selectbox("Select Garnish:", [str(garnish[0]) for garnish in garnish_items], index=None)

        elif type_selection == "Glass":
            st.write("Glass Table Data")
            query = "SELECT * FROM GlassType;"
            df = pd.read_sql_query(query, connect)
            st.dataframe(df)

            query2 = "SELECT DISTINCT glass_name FROM GlassType;"
            cursor.execute(query2)
            glass_items = cursor.fetchall()

            selected_glass = st.selectbox("Select Glass:", [str(glass[0]) for glass in glass_items], index=None)
            #if not None:
                #st.write(f"Selected Glass: {selected_glass}")"""
        else:
            pass

    connect.close()

if __name__ == "__main__":
    main()
