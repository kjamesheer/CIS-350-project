import streamlit as st
import sqlite3
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

_connect = """
connects to Liquor_database.db
"""

_cursor = """
executes certain query and related requests such
as cursor.execute() and cursor.fetchall()
"""


def home_page():
    """
    Holds all the information for the home page.
    This information includes the slide show pictures,
    type select, liquor select, and the graphical design
    such as buttons, dropdowns, and tables(Data_editor).

    Returns: None
    """
    connect = sqlite3.connect('Liquor_Database.db')
    cursor = connect.cursor()

    _, exp_col, _ = st.columns([1, 3, 1])
    with exp_col:
        components.html(
            """
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        .mySlides {display: none;}
        img {vertical-align: middle;}


        /* Fading animation */
        .fade {
          animation-name: fade;
          animation-duration: 1.5s;
        }

        @keyframes fade {
          from {opacity: .4}
          to {opacity: 1}
        }

        /* On smaller screens, decrease text size */
        @media only screen and (max-width: 300px) {
          .text {font-size: 11px}
        }
        </style>
        </head>
        <body>


        <div class="mySlides fade">
        <img src="https://unsplash.com/photos/QYWYnzvPTAQ/download?ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzEyNzA5OTUwfA&force=true"style="width:100%">
        </div>

        <div class="mySlides fade">
        <img src="https://unsplash.com/photos/7EbGkOm8pWM/download?ixid=M3wxMjA3fDB8MXxzZWFyY2h8M3x8Y29ja3RhaWxzfGVufDB8fHx8MTcxMjY5NDE4OXww&force=true" style="width:100%">
        </div>

        <div class="mySlides fade">
        <img src="https://images.unsplash.com/photo-1551024709-8f23befc6f87?q=80&w=3057&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3Dforce=true" style="width:100%">
        </div>

        <div class="mySlides fade">
        <img src="https://unsplash.com/photos/6EgxRnKU5BI/download?force=true"style="width:100%">
        </div>

        </div>
        <br>

        <div style="text-align:center">
          <span class="dot"></span>
          <span class="dot"></span>
          <span class="dot"></span>
          <span class="dot"></span>
        </div>

        <script>
        let slideIndex = 0;
        showSlides();

        function showSlides() {
          let i;
          let slides = document.getElementsByClassName("mySlides");
          let dots = document.getElementsByClassName("dot");
          for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
          }
          slideIndex++;
          if (slideIndex > slides.length) {slideIndex = 1}
          for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
          }
          slides[slideIndex-1].style.display = "block";
          dots[slideIndex-1].className += " active";
          setTimeout(showSlides, 10000); // Change image every 10 seconds
        }
        </script>

        </body>
        </html>

            """,
            height=500,
        )
        st.write('<div style="text-align: center; '
                 'font-size: 24px;"'
                 '>Search for recipes:</div>',
                 unsafe_allow_html=True)

    # Create a two-column layout
    col1, col2 = st.columns(2)

    with col1:
        type_selection = st.selectbox("Select Type:",
                                      ["Liquor", "Mixer", "Garnish", "Glass"],
                                      index=None)

    if not type_selection:
        with col2:
            st.selectbox("Please select a type of ingredient:", [], index=None)

    # Create the second box for selecting specific types(minor)
    # based on the first selection
    if type_selection == "Liquor":
        with col2:

            query1 = "SELECT DISTINCT sprt_name FROM Spirit;"
            cursor.execute(query1)
            liquor_items = cursor.fetchall()

            selected_spirit = st.selectbox("Select Liquor:",
                                           [str(liquor[0]) for liquor
                                            in liquor_items],
                                           index=None)

        col_1, col_2, col_3 = st.columns([1, 4, 1])
        with col_2:

            query2 = (
                f"SELECT Favorite, drnk_name as Drinks, "
                f"AlcContent as [Alcohol Content], "
                f"sprt_name || ', ' || Garnish_name || ', ' "
                f"|| mix_name || ', ' || glass_name as [Ingredients], "
                f"description as Description FROM DrinkRecipe WHERE"
                f" sprt_name = '{selected_spirit}';")
            df = pd.read_sql_query(query2, connect)
            if selected_spirit and df.empty:
                st.write(
                    "<p style='text-align:center;'>"
                    "No recipe with this ingredient. "
                    "Please select another ingredient.</p>",
                    unsafe_allow_html=True)
            elif selected_spirit:
                st.write("Recipes:")
                de1 = st.data_editor(df, column_config={
                    "Favorite": st.column_config.
                                     CheckboxColumn("Favorite",
                                                    default=False)},
                                     disabled=["Drinks", "Alcohol Content",
                                               "Ingredients", "Description"],
                                     hide_index=True,
                                     use_container_width=True)
                with col_3:
                    st.write("")
                    st.write("")
                    st.write("")
                    if st.button("Update Favorites"):
                        # Get the updated data
                        updated_data1 = st.session_state

                        for index, row in de1.iterrows():
                            favorite_value = 1 if row["Favorite"] else 0
                            update_query = (f"update DrinkRecipe SET "
                                            f"Favorite = {favorite_value} "
                                            f"WHERE drnk_name "
                                            f"= '{row['Drinks']}'")
                            cursor.execute(update_query)

                            connect.commit()
                        st.success("Favorites updated successfully!")

    elif type_selection == "Mixer":
        with col2:

            query1 = "SELECT DISTINCT mix_name FROM Mixer;"
            cursor.execute(query1)
            mixer_items = cursor.fetchall()

            selected_mixer = st.selectbox("Select Mixer:",
                                          [str(mixer[0])
                                           for mixer in mixer_items],
                                          index=None)

        col_1, col_2, col_3 = st.columns([1, 4, 1])
        with col_2:

            query2 = (
                f"SELECT Favorite, drnk_name as Drinks, "
                f"AlcContent as [Alcohol Content], "
                f"sprt_name || ', ' || Garnish_name || ', ' "
                f"|| mix_name || ', ' || glass_name as [Ingredients], "
                f"description as Description FROM DrinkRecipe WHERE"
                f" mix_name = '{selected_mixer}';")
            df = pd.read_sql_query(query2, connect)
            if selected_mixer and df.empty:
                st.write(
                    "<p style='text-align:center;'>"
                    "No recipe with this ingredient. "
                    "Please select another ingredient.</p>",
                    unsafe_allow_html=True)
            elif selected_mixer:
                st.write("Recipes:")
                de2 = st.data_editor(df, column_config={
                    "Favorite": st.column_config.
                                     CheckboxColumn("Favorite",
                                                    default=False)},
                                     disabled=["Drinks", "Alcohol Content",
                                               "Ingredients", "Description"],
                                     hide_index=True, use_container_width=True)
                with col_3:
                    st.write("")
                    st.write("")
                    st.write("")
                    if st.button("Update Favorites"):
                        # Get the updated data
                        updated_data2 = st.session_state

                        for index, row in de2.iterrows():
                            favorite_value = 1 if row["Favorite"] else 0
                            update_query = (f"update DrinkRecipe SET Favorite "
                                            f"= {favorite_value} "
                                            f"WHERE drnk_name "
                                            f"= '{row['Drinks']}'")
                            cursor.execute(update_query)

                            connect.commit()
                        st.success("Favorites updated successfully!")

    elif type_selection == "Garnish":
        with col2:

            query1 = "SELECT DISTINCT Garnish_name FROM Garnish;"
            cursor.execute(query1)
            garnish_items = cursor.fetchall()

            selected_garnish = st.selectbox("Select Garnish:",
                                            [str(garnish[0])
                                             for garnish in garnish_items],
                                            index=None)

        col_1, col_2, col_3 = st.columns([1, 4, 1])
        with col_2:

            query2 = (
                f"SELECT Favorite, drnk_name as Drinks, "
                f"AlcContent as [Alcohol Content], sprt_name || ', ' "
                f"|| Garnish_name || ', ' || mix_name "
                f"|| ', ' || glass_name as [Ingredients], "
                f"description as Description"
                f" FROM DrinkRecipe WHERE"
                f" Garnish_name = '{selected_garnish}';")
            df = pd.read_sql_query(query2, connect)
            if selected_garnish and df.empty:
                st.write(
                    "<p style='text-align:center;'>"
                    "No recipe with this ingredient. "
                    "Please select another ingredient.</p>",
                    unsafe_allow_html=True)
            elif selected_garnish:
                st.write("Recipes:")
                de3 = st.data_editor(df, column_config={
                    "Favorite": st.column_config.
                                     CheckboxColumn("Favorite",
                                                    default=False)},
                                     disabled=["Drinks", "Alcohol Content",
                                               "Ingredients", "Description"],
                                     hide_index=True, use_container_width=True)
                with col_3:
                    st.write("")
                    st.write("")
                    st.write("")
                    if st.button("Update Favorites"):
                        # Get the updated data
                        updated_data3 = st.session_state

                        for index, row in de3.iterrows():
                            favorite_value = 1 if row["Favorite"] else 0
                            update_query = (f"update DrinkRecipe SET "
                                            f"Favorite = {favorite_value} "
                                            f"WHERE drnk_name = "
                                            f"'{row['Drinks']}'")
                            cursor.execute(update_query)

                            connect.commit()
                        st.success("Favorites updated successfully!")

    elif type_selection == "Glass":
        with col2:

            query1 = "SELECT DISTINCT glass_name FROM GlassType;"
            cursor.execute(query1)
            glass_items = cursor.fetchall()

            selected_glass = st.selectbox("Select Glass:",
                                          [str(glass[0])
                                           for glass in glass_items],
                                          index=None)

        col_1, col_2, col_3 = st.columns([1, 4, 1])
        with col_2:

            query2 = (
                f"SELECT Favorite, drnk_name as Drinks,"
                f" AlcContent as [Alcohol Content]"
                f", sprt_name || ', ' "
                f"|| Garnish_name || ', ' || "
                f"mix_name || ', ' || glass_name "
                f"as [Ingredients], "
                f"description as Description "
                f"FROM DrinkRecipe WHERE"
                f" glass_name = '{selected_glass}';")
            df = pd.read_sql_query(query2, connect)
            if selected_glass and df.empty:
                st.write(
                    "<p style='text-align:center;'>"
                    "No recipe with this ingredient."
                    " Please select another ingredient.</p>",
                    unsafe_allow_html=True)
            elif selected_glass:
                st.write("Recipes:")
                de4 = st.data_editor(df, column_config={
                    "Favorite": st.column_config.
                                     CheckboxColumn("Favorite",
                                                    default=False)},
                                     disabled=["Drinks", "Alcohol Content",
                                               "Ingredients", "Description"],
                                     hide_index=True, use_container_width=True)
                with col_3:
                    st.write("")
                    st.write("")
                    st.write("")
                    if st.button("Update Favorites"):
                        # Get the updated data
                        updated_data4 = st.session_state

                        for index, row in de4.iterrows():
                            favorite_value = 1 if row["Favorite"] else 0
                            update_query = (f"update DrinkRecipe "
                                            f"SET Favorite = {favorite_value} "
                                            f"WHERE drnk_name = "
                                            f"'{row['Drinks']}'")
                            cursor.execute(update_query)

                            connect.commit()
                        st.success("Favorites updated successfully!")

    else:
        pass

    connect.close()


def all_recipes():
    """
    This function stores all the code/data for the all recipes tab
    in the streamlit application. Essentially the same functionality as
    the Home page, but has a more in depth filtering system that has been
    implemented. There is also no drop down menu that is used in this
    function.

    Returns: None
    """
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
            st.sidebar.write(f"{selected_difficulties[0]}"
                             f" and {selected_difficulties[1]}"
                             f" selected")
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
            st.sidebar.write(f"{selected_colors[0]}"
                             f" and {selected_colors[1]} "
                             f"selected")

    # -------------------------------------------------------#

    sql_query = ("SELECT Favorite, drnk_name as Drinks,"
                 " AlcContent as [Alcohol Content], "
                 "sprt_name || ', ' || Garnish_name || ', ' "
                 "|| mix_name || ', ' || glass_name as [Ingredients], "
                 "description as Description FROM DrinkRecipe")

    selected_filters = []

    if selected_liquors:
        selected_filters.append("(" + " OR ".
                                join([f"sprt_name = '{liq}'"
                                      for liq in selected_liquors]) + ")")

    if selected_mixers:
        selected_filters.append("(" + " OR ".
                                join([f"mix_name = '{mix}'"
                                      for mix in selected_mixers]) + ")")

    if selected_garnishes:
        selected_filters.append("(" + " OR ".
                                join([f"Garnish_name = '{gar}'"
                                      for gar in selected_garnishes]) + ")")

    if selected_glasses:
        (selected_filters.append("(" + " OR ".
                                 join([f"glass_name = '{gla}'"
                                       for gla in selected_glasses]) + ")"))

    if selected_difficulties:
        selected_filters.append("(" + " OR ".
                                join([f"Difficulty = '{diff}'"
                                      for diff in
                                      selected_difficulties]) + ")")

    if selected_colors:
        selected_filters.append("(" + " OR ".
                                join([f"Color_Of_Drink = '{clr}'"
                                      for clr in selected_colors]) + ")")

    if selected_filters:
        sql_query += " WHERE " + " AND ".join(selected_filters)

    # Execute SQL query
    df = pd.read_sql_query(sql_query, connect)

    # ---------------------------------------------------------------------------------------#

    # Display DataFrame
    ar_de5 = st.data_editor(df, column_config={
        "Favorite": st.column_config.
                            CheckboxColumn("Favorite",
                                           default=False)},
                            disabled=["Drinks", "Alcohol Content",
                                      "Ingredients", "Description"],
                            hide_index=True,
                            use_container_width=True)

    ar_col1, ar_col2 = st.columns([1, 5])
    with ar_col1:
        if st.button("Update Favorites"):
            ar_updated_data = st.session_state

            for index, row in ar_de5.iterrows():
                favorite_value = 1 if row["Favorite"] else 0
                update_query = (f"update DrinkRecipe SET Favorite ="
                                f" {favorite_value} "
                                f"WHERE drnk_name = "
                                f"'{row['Drinks']}'")
                cursor.execute(update_query)

                connect.commit()
            with ar_col2:
                st.success("Favorites updated successfully!")

    connect.close()


def favorites():
    """
    This function appends favorite values to a new table
    that will be displayed if a button has been clicked
    on from the user.

    Returns: None
    """
    connect = sqlite3.connect('Liquor_Database.db')
    cursor = connect.cursor()

    st.write('<div style="text-align: center; '
             'font-size: 24px;">'
             'Your favorite recipes:</div>',
             unsafe_allow_html=True)

    fv_qu = ("SELECT Favorite, drnk_name as Drinks,"
             " AlcContent as [Alcohol Content], "
             "sprt_name || ', ' || Garnish_name || ', ' ||"
             " mix_name || ', ' || glass_name as [Ingredients], "
             "description as Description FROM"
             " DrinkRecipe WHERE favorite = True")
    cursor.execute(fv_qu)
    favs = cursor.fetchall()

    if favs:
        df = pd.read_sql_query(fv_qu, connect)
        st.data_editor(df, column_config={
            "Favorite": st.column_config.
                       CheckboxColumn("Favorite",
                                      default=False)},
                       disabled=["Drinks", "Alcohol Content",
                                 "Ingredients", "Description"],
                       hide_index=True,
                       use_container_width=True)

    _, exp_col, _ = st.columns([1, 3, 1])
    if not favs:
        with exp_col:
            st.write("<p style='text-align:center;"
                     "'>No favorite recipes found!</p>",
                     unsafe_allow_html=True)

    connect.close()


# -----------------------------------------------------------------------#

connect = sqlite3.connect('Liquor_Database.db')
cursor = connect.cursor()

st.markdown("<h2 style='text-align: center; color:"
            " black;'>Liquor Recipe Ingredient Search System</h2>",
            unsafe_allow_html=True)

col1, col2, col3 = st.columns([4, 1, 1])

with col2:
    reset_button = st.button("Reset Favorites")
if reset_button:
    reset_qur = "UPDATE DrinkRecipe SET favorite = False"
    cursor.execute(reset_qur)
    connect.commit()

with col3:
    fav_button = st.button("Show Favorites")

if fav_button:
    favorites()
    with col1:
        back_button = st.button("Go Back")

with col1:
    if not fav_button:
        selected_page = st.radio("Pages:", ["Home", "All Recipes"])

if not fav_button:
    if selected_page == "Home":
        home_page()
    elif selected_page == "All Recipes":
        all_recipes()

connect.close()
