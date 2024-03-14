import streamlit as st
import sqlite3
import pandas as pd


def main():
    connect = sqlite3.connect('Liquor_Database.db')
    cursor = connect.cursor()

    st.markdown("<h2 style='text-align: center; color:"
                " white;'>Liquor Recipe Ingredient Search System</h2>",
                unsafe_allow_html=True)

    # Create a two-column layout
    col1, col2 = st.columns(2)

    # Create the first selectbox for selecting ingredient types(major)
    with col1:
        type_selection = st.selectbox("Select Type", ["Select Type", "Liquor", "Mixer", "Garnish", "Glass"])

        if type_selection == "Liquor":
            st.write("Liquor Table Data:")
            query = "SELECT * FROM Spirit;"
            df = pd.read_sql_query(query, connect)
            st.dataframe(df)

        elif type_selection == "Mixer":
            st.write("Mixer Table Data:")
            query = "SELECT * FROM Mixer;"
            df = pd.read_sql_query(query, connect)
            st.dataframe(df)

        elif type_selection == "Garnish":
            st.write("Garnish Table Data:")
            query = "SELECT * FROM Garnish;"
            df = pd.read_sql_query(query, connect)
            st.dataframe(df)

        elif type_selection == "Glass":
            st.write("Glass Table Data:")
            query = "SELECT * FROM GlassType;"
            df = pd.read_sql_query(query, connect)
            st.dataframe(df)

        else:
            pass

    # Create the second box for selecting specific types(minor)
    # based on the first selection
    with col2:
        if type_selection == "Liquor":

            query2 = "SELECT DISTINCT sprt_name FROM Spirit;"
            cursor.execute(query2)
            liquor_items = cursor.fetchall()

            selected_spirit = st.selectbox("Select Liquor:", [str(liquor[0]) for liquor in liquor_items], index=None)

            # Initialize selected_spirit_id with a default value
            selected_spirit_id = ""

            # Check if a liquor is selected before querying the ID
            if selected_spirit:
                query3 = (f"SELECT DISTINCT sprt_id FROM Spirit"
                          f" WHERE sprt_name = '{selected_spirit}';")
                cursor.execute(query3)
                selected_spirit_row = cursor.fetchone()

                if selected_spirit_row is not None:
                    selected_spirit_id = selected_spirit_row[0]

            # Query based on the selected spirit ID
            query4 = (f"SELECT * FROM DrinkRecipe WHERE sprt_id"
                      f" = '{selected_spirit_id}';")
            df = pd.read_sql_query(query4, connect)

            if selected_spirit_id and df.empty:
                st.write("No recipe with this ingredient."
                         " Please select another ingredient")
            elif selected_spirit_id:
                st.write("Recipes:")
                st.dataframe(df)

        elif type_selection == "Mixer":

            query2 = "SELECT DISTINCT mix_name FROM Mixer;"
            cursor.execute(query2)
            mixer_items = cursor.fetchall()

            selected_mixer = st.selectbox("Select Mixer:", [str(mixer[0]) for mixer in mixer_items], index=None)

            selected_mixer_id = ""

            if selected_mixer:
                query3 = (f"SELECT DISTINCT mix_id FROM Mixer"
                          f" WHERE mix_name = '{selected_mixer}';")
                cursor.execute(query3)
                selected_mixer_row = cursor.fetchone()

                if selected_mixer_row is not None:
                    selected_mixer_id = selected_mixer_row[0]

            query4 = (f"SELECT * FROM DrinkRecipe WHERE"
                      f" mix_id = '{selected_mixer_id}';")
            df = pd.read_sql_query(query4, connect)
            if selected_mixer_id and df.empty:
                st.write("No recipe with this ingredient."
                         " Please select another ingredient")
            elif selected_mixer_id:
                st.write("Recipes:")
                st.dataframe(df)

        elif type_selection == "Garnish":

            query2 = "SELECT DISTINCT Garnish_name FROM Garnish;"
            cursor.execute(query2)
            garnish_items = cursor.fetchall()

            selected_garnish = st.selectbox("Select Garnish:", [str(garnish[0]) for garnish in garnish_items], index=None)

            selected_garnish_id = ""

            if selected_garnish:
                query3 = (f"SELECT DISTINCT Garnish_id FROM Garnish"
                          f" WHERE Garnish_name = '{selected_garnish}';")
                cursor.execute(query3)
                selected_garnish_row = cursor.fetchone()

                if selected_garnish_row is not None:
                    selected_garnish_id = selected_garnish_row[0]

            query4 = (f"SELECT * FROM DrinkRecipe WHERE"
                      f" Garnish_id = '{selected_garnish_id}';")
            df = pd.read_sql_query(query4, connect)
            if selected_garnish_id and df.empty:
                st.write("No recipe with this ingredient."
                         " Please select another ingredient")
            elif selected_garnish_id:
                st.write("Recipes:")
                st.dataframe(df)

        elif type_selection == "Glass":

            query2 = "SELECT DISTINCT glass_name FROM GlassType;"
            cursor.execute(query2)
            glass_items = cursor.fetchall()

            selected_glass = st.selectbox("Select Glass:", [str(glass[0]) for glass in glass_items], index=None)

            selected_glass_id = ""

            if selected_glass:
                query3 = (f"SELECT DISTINCT glass_id FROM GlassType"
                          f" WHERE glass_name = '{selected_glass}';")
                cursor.execute(query3)
                selected_glass_row = cursor.fetchone()

                if selected_glass_row is not None:
                    selected_glass_id = selected_glass_row[0]

            query4 = (f"SELECT * FROM DrinkRecipe WHERE glass_id"
                      f" = '{selected_glass_id}';")
            df = pd.read_sql_query(query4, connect)
            if selected_glass_id and df.empty:
                st.write("No recipe with this ingredient."
                         " Please select another ingredient")
            elif selected_glass_id:
                st.write("Recipes:")
                st.dataframe(df)

        else:
            pass

    connect.close()


if __name__ == "__main__":
    main()
