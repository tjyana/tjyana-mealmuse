import streamlit as st
from utils.functions import final_recipes, combinations_of_two, data_query, final_recipes, muse_comb, recipe_generator, image_generator
import pandas as pd
import pickle





#--------------------

# Set page session states
if 'page1' not in st.session_state:
    st.session_state['page1'] = False
if 'page2' not in st.session_state:
    st.session_state['page2'] = True
if 'page3' not in st.session_state:
    st.session_state['page3'] = False


# ##############################################################
# 1 Title Page
# ##############################################################

if st.session_state['page1']:

    # Set columns for page 1
    col1, col2, col3 = st.columns([1, 4, 1])

    # Mealmuse header
    col2.markdown("<h1 style='text-align: center; color: black; font-size:60px'>Mealmuse</h1>", unsafe_allow_html=True)

    # Mealmuse subheader (Turn What..)
    col2.markdown("<h2 style='text-align: center; color: grey; font-size:20px'>Turn What You have to What You Crave &#128512; </h2>", unsafe_allow_html=True)

    # Set center image
    col2.image('mealmuse_images/people4.png')
    start_button = col2.button('START')

    # Images left, right and title background
    st.image('mealmuse_images/circleobjectleft.png')
    st.image('mealmuse_images/circleobjectright.png')
    st.image('mealmuse_images/centerobjects.png')

    # Start button styles
    st.markdown("""
    <style>
    div.stButton {
            text-align:center;
                }
    </style>""", unsafe_allow_html=True)

    st.markdown("""
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button{
            background-color: #FEBA21;
            border-radius: 12px;
            cursor: pointer;
            padding: 10px 15px;
            text-align: center;
            transition: 200ms;
            width: 50%;
            box-sizing: border-box;
            border: 0;
            touch-action: manipulation;
            }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button:not(:disabled):hover,
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button:not(:disabled):focus{
            outline: 0;
            background: #D94F00;
            box-shadow: 0 0 0 2px rgba(0,0,0,.2), 0 3px 8px 0 rgba(0,0,0,.15);
            }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button:not(:disabled):disabled{
            filter: saturate(0.2) opacity(0.5);
            -webkit-filter: saturate(0.2) opacity(0.5);
            cursor: not-allowed;
            }

        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button > div > p{
            color: white;
            font-size: 20px;
            font-weight: bold;
            }
    </style>""", unsafe_allow_html=True)

    # left background image styles
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(2) > div > div{
            position: fixed;
            left: 0px;
            bottom: 0px;

    }
    </style>""", unsafe_allow_html=True)

    # right background image styles
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(3) > div > div{
        position: fixed;
        right: -65px;
        bottom: 0px;
    }
    </style>""", unsafe_allow_html=True)

    # center background image styles
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(4) > div > div{
        position: absolute;
        left:0px;
        top:-700px;
        }
    </style>""", unsafe_allow_html=True)

    # Go to page 2
    if start_button:
        st.session_state['page2'] = True
        st.session_state['page1'] = False
        st.rerun()



# ##############################################################
# 2 Input Page
# Takes user input and sends it as-is to Output Page.
# ##############################################################

if st.session_state['page2']:

    # Set columns for page 2
    col1, col2, col3 = st.columns([1, 4, 1])

    # Mealmuse header
    col2.markdown("<h1 style='text-align: center; color: black; font-size:60px'>Mealmuse</h1>", unsafe_allow_html=True)
    # Mealmuse subheader (Turn What..)
    col2.markdown("<h2 style='text-align: center; color: grey; font-size:20px'>Turn What You have to What You Crave &#128512; </h2>", unsafe_allow_html=True)


    st.session_state['ingredients'] = col2.text_input('', help='Enter the list of ingredients:')

    evaluate_button = col2.button('Recipes Muse')

    col2.markdown("<h3 style='text-align: center; color: grey; font-size:20px'>An AI-powered recipe generator that utilizes Machine Learning to offer customized cooking suggestions based on avalable ingredients</h3>", unsafe_allow_html=True)

    # Images left, right and title background
    st.image('mealmuse_images/circleobjectleft.png')
    st.image('mealmuse_images/circleobjectright.png')
    st.image('mealmuse_images/centerobjects.png')

    # evaluate button
    st.markdown("""
    <style>
    div.stButton {
            text-align:center;
                }
    </style>""", unsafe_allow_html=True)

    st.markdown("""
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button{
            background-color: #FEBA21;
            border-radius: 12px;
            cursor: pointer;
            padding: 10px 15px;
            text-align: center;
            transition: 200ms;
            width: 50%;
            box-sizing: border-box;
            border: 0;
            touch-action: manipulation;
            }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button:not(:disabled):hover,
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button:not(:disabled):focus{
            outline: 0;
            background: #D94F00;
            box-shadow: 0 0 0 2px rgba(0,0,0,.2), 0 3px 8px 0 rgba(0,0,0,.15);
            }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button:not(:disabled):disabled{
            filter: saturate(0.2) opacity(0.5);
            -webkit-filter: saturate(0.2) opacity(0.5);
            cursor: not-allowed;
            }

        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button > div > p{
            color: white;
            font-size: 20px;
            font-weight: bold;
            }
    </style>""", unsafe_allow_html=True)



     # left background image styles
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(2) > div > div{
            position: fixed;
            left: 0px;
            bottom: 0px;

    }
    </style>""", unsafe_allow_html=True)

     # right background image styles
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(3) > div > div{
        position: fixed;
        right: -65px;
        bottom: 0px;
    }
    </style>""", unsafe_allow_html=True)

     # center background image styles
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(4) > div > div{
        position: absolute;
        left:0px;
        top:-550px;
        }
    </style>""", unsafe_allow_html=True)



    # main paragraph at the middle
    st.markdown("""
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(5) > div{
        padding-top: 40px;
    }
    </style>""", unsafe_allow_html=True)

    # footer
    st.markdown("""
        <style>
        .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: black;
        text-align: center;
        }
        </style>
        <div class="footer">
        <p>Developed with ❤️ by <a style='display: block; text-align: center;' href="https://github.com/annaloanlin/Mealmuse-Workspace.git" target="_blank">Mealmuse Team</a></p>
        </div>
        </style>""", unsafe_allow_html=True)

    # Go to page 3
    if evaluate_button:
        st.session_state['page3'] = True
        st.session_state['page2'] = False
        st.rerun()




# ##############################################################
# 3 Output Page
# Takes user input as a string from Input Page.
# Outputs ingredients, instructions, and image.
# Compatibility functions and the model are here.
# ##############################################################


if st.session_state['page3']:

    @st.cache_data
    def get_model():
        with open("utils/model.pickle", "rb") as f:
            model = pickle.load(f)
        return model

    model = get_model()

    df = pd.read_parquet('data/Halved-DF.parquet.gzip')


    # set user input as ingredients
    # bringing over from page 2s
    # needs to be in st.session_state format
    ingredients = st.session_state['ingredients']

    # FUNCTIONS MAP:
    # combinations_of_two(ingredients_input) > ingredients_combinations
    # data_query(df, ingredients_combinations) > df_comb
    # muse_comb(data_query, df) > ingredients_list

    ingredients_combinations = combinations_of_two(ingredients)
    df_comb = data_query(ingredients_combinations)
    ingredients_list = muse_comb(df_comb)
    recipe = recipe_generator(ingredients_list)

    # we need to figure out what recipe is returning

    contents, titles, ingredients = [], [], []
    contents1, titles1, ingredients1, scores = [], [], [], []  ##<==== changed the variables a bit so the variables below will not be affected


    recipe_direction = []
    for single_recipe in recipe:
        if 'directions' in single_recipe:
            recipe_direction.append(single_recipe['directions'])
        else:
            recipe_direction.append("")

    scores = []
    for direction in recipe_direction:
        scores.append(model.predict_proba([direction])[0][1])

    titles1 = [n['title'] for n in recipe] # list of titles
    ingredient1 = [n['ingredients'] for n in recipe] # list of ingredients
    contents1 = [n['directions'] for n in recipe] # list of directions

    recipe_dict = {'title': titles1, 'ingredients': ingredients1, 'directions': contents1}
    final_recipe = final_recipes(recipe, scores, model) ##<===added the regenerator and reassigned the titles, ingredients, and contents variables to reflect the final recipes
    titles.append(final_recipe["Title"])
    ingredients.append(final_recipe["Ingredients"])
    contents.append(final_recipe["Directions"])



    # Columns
    col1, col2, col3 = st.columns([1, 4, 1])

    # Mealmuse header
    col2.markdown("<h1 style='text-align: center; color: black; font-size:60px'>Mealmuse</h1>", unsafe_allow_html=True)
    # Mealmuse subheader (Turn What..)
    col2.markdown("<h2 style='text-align: center; color: grey; font-size:20px'>Turn What You have to What You Crave &#128512; </h2>", unsafe_allow_html=True)
    #col2.markdown("<h3 style='text-align: center; color: black; font-size:10px'>Enter Your Ingredients</h3>", unsafe_allow_html=True)

    # Background images
    st.image('mealmuse_images/circleobjectleft.png')
    st.image('mealmuse_images/circleobjectright.png')
    st.image('mealmuse_images/centerobjects.png')

    # left background image styles
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(2) > div > div{
            position: fixed;
            left: 0px;
            bottom: 0px;

    }
    </style>""", unsafe_allow_html=True)

    # right background image styles
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(3) > div > div{
        position: fixed;
        right: -65px;
        bottom: 0px;
    }
    </style>""", unsafe_allow_html=True)

    # center background image styles
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(4) > div > div{
        position: absolute;
        left:0px;
        top:-250px;
        }
    </style>""", unsafe_allow_html=True)


# WE NEED THIS ##############################################
    # img_list = []
    # for title in st.session_state['titles']:
    #     if title != None:
    #         img = image_generator(title)
    #         img_list.append(img)



    with st.container():

        dishes = [f'Dish {n+1}' for n in range(len(titles))]
        for index, tab in enumerate(st.tabs(dishes)):


            with tab:
                st.subheader(titles[index])

                col1, col2, col3 = st.columns([1, 2, 1])
                with col1:
                    st.subheader('Ingredients')
                    if index < len(ingredients):
                        st.write(ingredients[index])
                with col2:
                    st.subheader('Instructions')
                    if index < len(contents):
                        st.write(contents[index])
                with col3:
                    st.subheader('Image')
                    # if index < len(img_list):
                    #     st.image(img_list[index], width=200)


    # tab styles
    st.markdown("""
    <style>
        .stTabs [data-baseweb="tab-list"] {
            gap: 2px;
        }

        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: #FEBA21;
            border-radius: 999px;
            gap: 1px;
            color: white;
            padding: 10px 20px 10px 20px;
        }

        .stTabs [aria-selected="true"] {
            background-color: #D94F00;
        }

        .stTabs [data-baseweb="tab-highlight"] {
            background-color: transparent;
        }

        #tabs-bui2-tab-0 > div > p {
            color: white;
            font-size: 15px;
            font-weight: bold;
            }
        #tabs-bui2-tab-1 > div > p {
            color: white;
            font-size: 15px;
            font-weight: bold;
            }
        #tabs-bui2-tab-2 > div > p {
            color: white;
            font-size: 15px;
            font-weight: bold;
            }
        #tabs-bui4-tabpanel-0 > div > div > div > div > div:nth-child(3) > div > div > div > div:nth-child(2) > div > div > div > img{
            border-radius: 30px;
            -webkit-filter: drop-shadow(12px 12px 7px rgba(217,79,0,0.5));
            }
        #tabs-bui4-tabpanel-1 > div > div > div > div > div:nth-child(3) > div > div > div > div:nth-child(2) > div > div > div > img{
            border-radius: 30px;
            -webkit-filter: drop-shadow(12px 12px 7px rgba(217,79,0,0.5));
            }
        #tabs-bui4-tabpanel-2 > div > div > div > div > div:nth-child(3) > div > div > div > div:nth-child(2) > div > div > div > img{
            border-radius: 30px;
            -webkit-filter: drop-shadow(12px 12px 7px rgba(217,79,0,0.5));
            }
    </style>""", unsafe_allow_html=True)

    #footer
    st.markdown("""
        <style>
        .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: black;
        text-align: center;
        }
        </style>
        <div class="footer">
        <p>Developed with ❤️ by <a style='display: block; text-align: center;' href="https://github.com/annaloanlin/Mealmuse-Workspace.git" target="_blank">Mealmuse Team</a></p>
        </div>
        </style>""", unsafe_allow_html=True)
