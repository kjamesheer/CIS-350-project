import streamlit as st
import sqlite3
import pandas as pd


def home_page():
    connect = sqlite3.connect('Liquor_Database.db')
    cursor = connect.cursor()

    st.image('1096302.jpg')
    st.write('<div style="text-align: center; font-size: 24px;">Search for recipes:</div>', unsafe_allow_html=True)

    # Create a two-column layout
    col1, col2 = st.columns(2)

    # Create the first selectbox for selecting ingredient types(major)
    with col1:
        type_selection = st.selectbox("Select Type:", ["Liquor", "Mixer", "Garnish", "Glass"], index=None)

    # Create the second box for selecting specific types(minor)
    # based on the first selection
    if type_selection == "Liquor":
        with col2:

            query1 = "SELECT DISTINCT sprt_name FROM Spirit;"
            cursor.execute(query1)
            liquor_items = cursor.fetchall()

            selected_spirit = st.selectbox("Select Liquor:", [str(liquor[0]) for liquor in liquor_items], index=None)

        # Initialize selected_spirit_id with a default value
        selected_spirit_id = ""

        # Check if a liquor is selected before querying the ID
        if selected_spirit:
            query2 = (f"SELECT DISTINCT sprt_id FROM Spirit"
                    f" WHERE sprt_name = '{selected_spirit}';")
            cursor.execute(query2)
            selected_spirit_row = cursor.fetchone()

            if selected_spirit_row is not None:
                selected_spirit_id = selected_spirit_row[0]

        # Query based on the selected spirit ID
        query3 = (f"SELECT Favorite, drnk_name as Drinks, AlcContent as [Alcohol Content], description as Description FROM DrinkRecipe WHERE"
                    f" sprt_id = '{selected_spirit_id}';")
        df = pd.read_sql_query(query3, connect)

        if selected_spirit_id and df.empty:
            st.write("No recipe with this ingredient."
                " Please select another ingredient")
        elif selected_spirit_id:
            st.write("Recipes:")
            st.data_editor(df, column_config={"Favorite": st.column_config.CheckboxColumn("favorite", default=False)} ,disabled=["Drinks", "Alcohol Content", "Description"], hide_index=True)

    elif type_selection == "Mixer":
        with col2:

            query1 = "SELECT DISTINCT mix_name FROM Mixer;"
            cursor.execute(query1)
            mixer_items = cursor.fetchall()

            selected_mixer = st.selectbox("Select Mixer:", [str(mixer[0]) for mixer in mixer_items], index=None)

        selected_mixer_id = ""

        if selected_mixer:
            query2 = (f"SELECT DISTINCT mix_id FROM Mixer"
                      f" WHERE mix_name = '{selected_mixer}';")
            cursor.execute(query2)
            selected_mixer_row = cursor.fetchone()

            if selected_mixer_row is not None:
                selected_mixer_id = selected_mixer_row[0]

        query3 = (f"SELECT Favorite, drnk_name as Drinks, AlcContent as [Alcohol Content], description as Description FROM DrinkRecipe WHERE"
                  f" mix_id = '{selected_mixer_id}';")
        df = pd.read_sql_query(query3, connect)
        if selected_mixer_id and df.empty:
            st.write("No recipe with this ingredient."
                     " Please select another ingredient")
        elif selected_mixer_id:
            st.write("Recipes:")
            st.data_editor(df, column_config={"Favorite": st.column_config.CheckboxColumn("favorite", default=False)},
                           disabled=["Drinks", "Alcohol Content", "Description"], hide_index=True)

    elif type_selection == "Garnish":
        with col2:

            query1 = "SELECT DISTINCT Garnish_name FROM Garnish;"
            cursor.execute(query1)
            garnish_items = cursor.fetchall()

            selected_garnish = st.selectbox("Select Garnish:", [str(garnish[0]) for garnish in garnish_items], index=None)

        selected_garnish_id = ""

        if selected_garnish:
            query2 = (f"SELECT DISTINCT Garnish_id FROM Garnish"
                      f" WHERE Garnish_name = '{selected_garnish}';")
            cursor.execute(query2)
            selected_garnish_row = cursor.fetchone()

            if selected_garnish_row is not None:
                selected_garnish_id = selected_garnish_row[0]

        query3 = (f"SELECT Favorite, drnk_name as Drinks, AlcContent as [Alcohol Content], description as Description FROM DrinkRecipe WHERE"
                  f" Garnish_id = '{selected_garnish_id}';")
        df = pd.read_sql_query(query3, connect)
        if selected_garnish_id and df.empty:
            st.write("No recipe with this ingredient."
                     " Please select another ingredient")
        elif selected_garnish_id:
            st.write("Recipes:")
            st.data_editor(df, column_config={"Favorite": st.column_config.CheckboxColumn("favorite", default=False)} ,disabled=["Drinks", "Alcohol Content", "Description"], hide_index=True)

    elif type_selection == "Glass":
        with col2:

            query1 = "SELECT DISTINCT glass_name FROM GlassType;"
            cursor.execute(query1)
            glass_items = cursor.fetchall()

            selected_glass = st.selectbox("Select Glass:", [str(glass[0]) for glass in glass_items], index=None)

        selected_glass_id = ""

        if selected_glass:
            query2 = (f"SELECT DISTINCT glass_id FROM GlassType"
                      f" WHERE glass_name = '{selected_glass}';")
            cursor.execute(query2)
            selected_glass_row = cursor.fetchone()

            if selected_glass_row is not None:
                selected_glass_id = selected_glass_row[0]

        query3 = (f"SELECT Favorite, drnk_name as Drinks, AlcContent as [Alcohol Content], description as Description FROM DrinkRecipe WHERE"
                  f" glass_id = '{selected_glass_id}';")
        df = pd.read_sql_query(query3, connect)
        if selected_glass_id and df.empty:
            st.write("No recipe with this ingredient."
                     " Please select another ingredient")
        elif selected_glass_id:
            st.write("Recipes:")
            st.data_editor(df, column_config={"Favorite": st.column_config.CheckboxColumn("favorite", default=False)}, disabled=["Drinks", "Alcohol Content", "Description"], hide_index=True)

    else:
        pass

    connect.close()

def all_recipes():
    connect = sqlite3.connect('Liquor_Database.db')
    cursor = connect.cursor()

    st.sidebar.title("Filter:")

    query1_ar = "SELECT DISTINCT sprt_name FROM Spirit;"
    cursor.execute(query1_ar)
    liquor_items = cursor.fetchall()

    selected_liquors = []

    on1 = st.sidebar.toggle('Liquor:')
    if not on1:
        for liquor in liquor_items:
            selected_liq = st.sidebar.checkbox(f"{liquor[0]}")
            if selected_liq:
                selected_liquors.append(liquor[0])

    length = len(selected_liquors)

    if selected_liquors:
        st.sidebar.write(f"{length} liquors selected")


    query2_ar = "SELECT DISTINCT mix_name FROM Mixer;"
    cursor.execute(query2_ar)
    mixer_items = cursor.fetchall()

    selected_mixers = []

    on2 = st.sidebar.toggle('Mixers:')
    if not on2:
        for mixer in mixer_items:
            selected_mix = st.sidebar.checkbox(f"{mixer[0]}")
            if selected_mix:
                selected_mixers.append(mixer[0])

    length2 = len(selected_mixers)

    if selected_mixers:
        st.sidebar.write(f"{length2} mixers selected")

    query3_ar = "SELECT DISTINCT Garnish_name FROM Garnish;"
    cursor.execute(query3_ar)
    garnish_items = cursor.fetchall()

    selected_garnishes = []

    on3 = st.sidebar.toggle('Garnishes:')
    if not on3:
        for garnish in garnish_items:
            selected_gar = st.sidebar.checkbox(f"{garnish[0]}")
            if selected_gar:
                selected_garnishes.append(garnish[0])

        length3 = len(selected_garnishes)

    if selected_garnishes:
        st.sidebar.write(f"{length3} garnishes selected")

    query4_ar = "SELECT DISTINCT glass_name FROM GlassType;"
    cursor.execute(query4_ar)
    glass_items = cursor.fetchall()

    selected_glasses = []

    on4 = st.sidebar.toggle('Glasses:')
    if not on4:
        for glass in glass_items:
            selected_gl = st.sidebar.checkbox(f"{glass[0]}")
            if selected_gl:
                selected_glasses.append(glass[0])

        length4 = len(selected_glasses)

    if selected_glasses:
        st.sidebar.write(f"{length4} glasses selected")

    query5_ar = "SELECT DISTINCT Difficulty FROM DrinkRecipe;"
    cursor.execute(query5_ar)
    diff_items = cursor.fetchall()

    selected_difficulties = []

    on5 = st.sidebar.toggle('Difficulties:')
    if not on5:
        for diff in diff_items:
            selected_dif = st.sidebar.checkbox(f"{diff[0]}")
            if selected_dif:
                selected_difficulties.append(diff[0])

    if selected_difficulties:
        if len(selected_difficulties) == 1:
            st.sidebar.write(f"{selected_difficulties[0]} selected")
        if len(selected_difficulties) == 2:
            st.sidebar.write(f"{selected_difficulties[0]} and {selected_difficulties[1]} selected")
        if len(selected_difficulties) == 3:
            st.sidebar.write("All difficulties selected")


    query6_ar = "SELECT DISTINCT Color_Of_Drink FROM DrinkRecipe;"
    cursor.execute(query6_ar)
    color_items = cursor.fetchall()

    selected_colors = []

    on6 = st.sidebar.toggle('Colors:')
    if not on6:
        for color in color_items:
            selected_clr = st.sidebar.checkbox(f"{color[0]}")
            if selected_clr:
                selected_colors.append(color[0])

    if selected_colors:
        if len(selected_colors) == 1:
            st.sidebar.write(f"{selected_colors[0]} selected")
        if len(selected_colors) == 2:
            st.sidebar.write(f"{selected_colors[0]} and {selected_colors[1]} selected")

#-------------------------------------------------------#

    sql_query = "SELECT * FROM DrinkRecipe"

    if selected_difficulties or selected_colors:
        sql_query += " WHERE "

    if selected_difficulties:
        sql_query += "(" + " OR ".join([f"Difficulty = '{diff}'" for diff in selected_difficulties]) + ")"

    if selected_difficulties and selected_colors:
        sql_query += " AND "

    if selected_colors:
        sql_query += "(" + " OR ".join([f"Color_Of_Drink = '{clr}'" for clr in selected_colors]) + ")"

    # Execute SQL query
    df = pd.read_sql_query(sql_query, connect)

    # Display DataFrame
    st.dataframe(df, hide_index=True)

#--------------------------------------------------#

    connect.close()


#-----------------------------------------------------------------------#
st.markdown("<h2 style='text-align: center; color:"
            " white;'>Liquor Recipe Ingredient Search System</h2>",
            unsafe_allow_html=True)
selected_page = st.radio("Pages:", ["Home", "All Recipes"])

if selected_page == "Home":
    home_page()

if selected_page == "All Recipes":
    all_recipes()
